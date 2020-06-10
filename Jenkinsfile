pipeline {
    agent any

    stages{

            stage('Make script executable'){
                steps{
                    sh 'chmod +x ./script/*'
                    
                }
            }

            stage('Deploying docker swarm'){
                steps{
                    sh './script/docker.sh'
                }
            }
        }
    }