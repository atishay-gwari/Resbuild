pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/atishay-gwari/Resbuild.git']]])
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                script {
                    // Execute the Docker Compose build and run commands
                    sh 'docker-compose down -v'
                    sh 'docker-compose up --build -d'
                }
            }
        }
    }
}
