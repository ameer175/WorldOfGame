pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('Scores') {
                    bat 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                dir('Scores') { 
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                dir('tests') {
                    bat 'python3 e2e.py'
                }
            }
        }

        
        }
    }
}
