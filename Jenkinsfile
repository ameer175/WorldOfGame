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
        stage('Run')
        {
            steps
            {
                bat 'dir'
            }
        }
    }
}