pipeline {
    agent any

    stages{

            stage('Dependencies'){
                steps{
                    sh 'chmod +x ./script/*'
                    sh 'bash ./script/before_installation.sh'
                    
                }
            }

            stage('Deploying Docker Stack'){
                steps{
                    sh 'chmod +x ./script/*'
                    sh './script/docker.sh'
                }
            }
        }
    }