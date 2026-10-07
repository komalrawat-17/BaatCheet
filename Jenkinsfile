pipeline {
    agent any

    environment {
        APP_NAME     = 'baatcheet-backend'
        IMAGE_NAME   = 'baatcheet-backend:latest'
        PYTHON_VER   = '3.12'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest source code from repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '=== Stage 1: Build ==='
                echo "Building application container image: ${IMAGE_NAME}"
                sh 'docker build -f Dockerfile.backend -t ${IMAGE_NAME} ./backend'
            }
        }

        stage('Test') {
            steps {
                echo '=== Stage 2: Test ==='
                echo 'Running unit and integration tests...'
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r backend/requirements.txt
                    cd backend && pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '=== Stage 3: Deploy ==='
                echo 'Deploying BaatCheet service stack using Docker Compose...'
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose up -d'
                echo 'Services deployed successfully.'
                echo 'Health Check endpoint: http://localhost:8000/health'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
            cleanWs()
        }
        success {
            echo 'SUCCESS: BaatCheet CI/CD Pipeline executed successfully!'
        }
        failure {
            echo 'FAILURE: Pipeline run failed. Please check stage console logs.'
        }
    }
}
