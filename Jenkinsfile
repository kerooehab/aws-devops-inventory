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

        stage('Push Images to ECR') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                     credentialsId: 'aws-ecr-credentials']
                ]) {
                    sh '''
                        aws ecr get-login-password --region eu-north-1 | \
                        docker login --username AWS --password-stdin \
                        579302404833.dkr.ecr.eu-north-1.amazonaws.com

                        docker tag inventory-backend:${BUILD_NUMBER} \
                        579302404833.dkr.ecr.eu-north-1.amazonaws.com/aws-cloud-devops:backend-${BUILD_NUMBER}

                        docker tag inventory-frontend:${BUILD_NUMBER} \
                        579302404833.dkr.ecr.eu-north-1.amazonaws.com/aws-cloud-devops:frontend-${BUILD_NUMBER}

                        docker push \
                        579302404833.dkr.ecr.eu-north-1.amazonaws.com/aws-cloud-devops:backend-${BUILD_NUMBER}

                        docker push \
                        579302404833.dkr.ecr.eu-north-1.amazonaws.com/aws-cloud-devops:frontend-${BUILD_NUMBER}
                    '''
                }
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
