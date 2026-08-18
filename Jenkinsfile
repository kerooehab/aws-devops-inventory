pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Backend Test') {
            steps {
                sh '''
                    python3 -m venv .venv-ci
                    . .venv-ci/bin/activate
                    pip install -r backend/requirements.txt
                    pytest backend/tests
                '''
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                    docker build \
                      -t inventory-backend:${BUILD_NUMBER} \
                      ./backend
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                    docker build \
                      -t inventory-frontend:${BUILD_NUMBER} \
                      ./frontend
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }

        failure {
            echo 'CI pipeline failed.'
        }
    }
}
