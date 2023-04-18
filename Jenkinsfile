pipeline {
    agent any

    stages
    {
        stage('Build')
        {
            steps
            {
                dir('tests') {
                    bat 'docker-compose build'
                }
            }
        }
        stage('Run docker-compose')
        {
            steps
            {
                dir('tests') {
                    bat 'docker-compose up -d'
                }
            }
        }
    }
}