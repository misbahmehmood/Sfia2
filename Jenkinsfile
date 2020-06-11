pipeline {
    agent any

    stages{

            stage('Make script executable'){
                steps{
                    sh 'chmod +x ./script/*'
                    
                }
            }

            stage('Use ansible'){
                steps{

                    sh './script/ansible.sh'
                    
                }
            }

            stage('Deploying docker swarm'){
                steps{
                    sh './script/docker.sh'
                }
            }
        }
    }
