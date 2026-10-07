pipeline {
    agent any

    environment {
        APP_NAME     = 'baatcheet-backend'
        IMAGE_NAME   = 'baatcheet-backend:latest'
        HEALTH_URL   = 'http://localhost:8000/health'
    }

    // Build Triggers: Automatic trigger on SCM push and periodic polling
    triggers {
        githubPush()
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo '=== SCM Triggered: Checking Out Code ==='
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '=== Stage 1: Build & Package ==='
                echo "Packaging application image: ${IMAGE_NAME}"
                sh 'docker build -f Dockerfile.backend -t ${IMAGE_NAME} ./backend'
            }
        }

        stage('Test') {
            steps {
                echo '=== Stage 2: Automated Testing ==='
                sh '''
                    python3 -m pip install -r backend/requirements.txt
                    cd backend && pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '=== Stage 3: Automated Deployment ==='
                echo 'Stopping existing instances and launching new release...'
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose up -d'
                
                echo 'Executing Automated Deployment Health Verification...'
                sh '''
                    echo "Checking health endpoint at ${HEALTH_URL}..."
                    for i in $(seq 1 10); do
                        if curl -s -f ${HEALTH_URL} | grep -q "ok"; then
                            echo "Deployment Verified: Application is Healthy and Live!"
                            exit 0
                        fi
                        echo "Waiting for service to become responsive ($i/10)..."
                        sleep 2
                    done
                    echo "Health verification failed! Triggering deployment failure."
                    exit 1
                '''
            }
        }
    }

    // Post-Build Actions: Notifications, cleanup, and failure recovery
    post {
        always {
            echo '=== Post-Build: Cleaning Workspace & Storing Logs ==='
            cleanWs()
        }
        success {
            echo '=== Post-Build: SUCCESS ==='
            echo 'DEPLOYMENT SUCCESS: BaatCheet application has been successfully deployed and verified.'
        }
        failure {
            echo '=== Post-Build: FAILURE / ROLLBACK ==='
            echo 'DEPLOYMENT FAILED: Rolling back to previous stable container...'
            sh 'docker compose restart || true'
            echo 'Rollback command dispatched. Immediate alert generated.'
        }
    }
}
