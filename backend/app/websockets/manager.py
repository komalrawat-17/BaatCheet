import json
import asyncio
from typing import Dict, Set
from uuid import UUID
from fastapi import WebSocket
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.message import Message


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        self.redis: Redis = None
        self.pubsub_tasks: Dict[str, asyncio.Task] = {}

    async def init_redis(self):
        if not self.redis:
            self.redis = Redis.from_url(settings.get_redis_url(), decode_responses=True)

    async def connect(self, websocket: WebSocket, room_id: str, user_id: str):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = set()
        self.active_connections[room_id].add(websocket)

        await self.init_redis()
        # Set online presence with 30s TTL
        await self.redis.set(f"user:presence:{user_id}", "online", ex=30)
        
        # Subscribe to room pub/sub if first connection on this worker instance
        if room_id not in self.pubsub_tasks:
            task = asyncio.create_task(self._redis_subscribe_loop(room_id))
            self.pubsub_tasks[room_id] = task

    async def disconnect(self, websocket: WebSocket, room_id: str, user_id: str):
        if room_id in self.active_connections:
            self.active_connections[room_id].discard(websocket)
            if not self.active_connections[room_id]:
                del self.active_connections[room_id]
                if room_id in self.pubsub_tasks:
                    self.pubsub_tasks[room_id].cancel()
                    del self.pubsub_tasks[room_id]
        
        if self.redis:
            await self.redis.delete(f"user:presence:{user_id}")

    async def heartbeat(self, user_id: str):
        if self.redis:
            await self.redis.set(f"user:presence:{user_id}", "online", ex=30)

    async def publish_message(self, room_id: str, data: dict):
        await self.init_redis()
        await self.redis.publish(f"chat:room:{room_id}", json.dumps(data))

    async def _redis_subscribe_loop(self, room_id: str):
        await self.init_redis()
        pubsub = self.redis.pubsub()
        await pubsub.subscribe(f"chat:room:{room_id}")
        try:
            async for message in pubsub.listen():
                if message["type"] == "message":
                    payload = message["data"]
                    await self._broadcast_to_local_room(room_id, payload)
        except asyncio.CancelledError:
            await pubsub.unsubscribe(f"chat:room:{room_id}")
            await pubsub.close()

    async def _broadcast_to_local_room(self, room_id: str, raw_json: str):
        if room_id in self.active_connections:
            for connection in list(self.active_connections[room_id]):
                try:
                    await connection.send_text(raw_json)
                except Exception:
                    self.active_connections[room_id].discard(connection)


manager = ConnectionManager()
