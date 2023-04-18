pipeline {
    agent any # Use any available agent to run the pipeline

    stages { # Define the stages in the pipeline
        stage('Build') { # First stage: Build
            steps {
                dir('Scores') { # Change to the 'Scores' directory
                    bat 'docker-compose build' # Build the Docker images defined in the docker-compose.yml file
                }
            }
        }

        stage('Run') { # Second stage: Run
            steps {
                dir('Scores') { # Change to the 'Scores' directory
                    bat 'docker-compose up -d' # Start the containers in detached mode (-d)
                }
            }
        }

        stage('Test') { # Third stage: Test
            steps {
                dir('tests') { # Change to the 'tests' directory
                    bat 'python3 e2e.py' # Run an end-to-end test using Python
                }
            }
        }

        stage('Finalize') { # Fourth stage: Finalize
            steps {
                dir('Scores') { # Change to the 'Scores' directory
                    bat 'docker-compose down' # Stop and remove the containers
                    bat 'docker-compose push' # Push the built images to a Docker registry
                }
            }
        }
    }
}