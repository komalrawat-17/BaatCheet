import json
from uuid import UUID
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, Query, status
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import AsyncSessionLocal
from app.api import auth, rooms, messages
from app.websockets.manager import manager
from app.models.message import Message
from app.models.user import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST Routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(rooms.router, prefix=f"{settings.API_V1_STR}/rooms", tags=["rooms"])
app.include_router(messages.router, prefix=f"{settings.API_V1_STR}/messages", tags=["messages"])


@app.get("/health")
async def health_check():
    return {"status": "ok", "app": settings.PROJECT_NAME, "version": settings.VERSION}


@app.websocket("/ws/chat/{room_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_id: str,
    token: str = Query(...)
):
    # Verify JWT Token during handshake
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return
    except JWTError:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    await manager.connect(websocket, room_id, user_id)
    try:
        while True:
            data_str = await websocket.receive_text()
            data = json.loads(data_str)
            msg_type = data.get("type", "message")

            if msg_type == "ping":
                await manager.heartbeat(user_id)
                await websocket.send_text(json.dumps({"type": "pong"}))
            
            elif msg_type == "message":
                content = data.get("content")
                if content:
                    # Save message to DB asynchronously
                    async with AsyncSessionLocal() as db:
                        db_msg = Message(
                            room_id=UUID(room_id),
                            sender_id=UUID(user_id),
                            content=content
                        )
                        db.add(db_msg)
                        await db.commit()
                        await db.refresh(db_msg)

                        # Fetch sender details
                        user_res = await db.get(User, UUID(user_id))
                        sender_username = user_res.username if user_res else "Unknown"

                    # Broadcast to Redis Pub/Sub
                    broadcast_payload = {
                        "type": "message",
                        "id": str(db_msg.id),
                        "room_id": room_id,
                        "sender_id": user_id,
                        "sender_username": sender_username,
                        "content": content,
                        "created_at": db_msg.created_at.isoformat()
                    }
                    await manager.publish_message(room_id, broadcast_payload)

            elif msg_type == "typing":
                # Broadcast typing status
                async with AsyncSessionLocal() as db:
                    user_res = await db.get(User, UUID(user_id))
                    sender_username = user_res.username if user_res else "Unknown"

                await manager.publish_message(room_id, {
                    "type": "typing",
                    "room_id": room_id,
                    "sender_id": user_id,
                    "sender_username": sender_username,
                    "is_typing": data.get("is_typing", True)
                })

    except WebSocketDisconnect:
        await manager.disconnect(websocket, room_id, user_id)
    except Exception:
        await manager.disconnect(websocket, room_id, user_id)
