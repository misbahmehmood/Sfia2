pipeline {
    agent any

    stages{

            stage('Dependencies'){
                steps{
                    sh 'chmod +x ./script/*'
                    
                }
            }

            stage('Deploying Docker'){
                steps{
                    sh './script/docker.sh'
                }
            }
        }
    }