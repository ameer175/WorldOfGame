pipeline {
    agent any

    stages
    {
        stage('Build')
        {
            steps
            {

                bat 'docker-compose build'

            }
        }
        stage('Run docker-compose')
        {
            steps
            {

                bat 'docker-compose up -d'

            }
        }
        stage('Test')
        {
            steps
            {
                dir('tests')
                {
                    bat 'python e2e.py'
                }
            }
        }
        stage('Finalize')
        {
            steps
            {
                dir('tests')
                {
                    bat 'docker-compose down'
                    bat 'docker-compose push'
                }
            }
        }
    }
}