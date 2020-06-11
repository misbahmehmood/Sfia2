pipeline {
    agent any

    stages{

            stage('Make script executable'){
                steps{
                    sh 'chmod +x ./script/*'
                    
                }
            }

            stage('Use and install ansible'){
                steps{
                    sh '.script/ansible_installation.sh'
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
