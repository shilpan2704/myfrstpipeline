pipeline {
    agent any 
    stages {
        stage('Build ') { 
            steps {
              print("hello world");
            }
        }
        stage('Test') { 
            steps {
                
               print("Hi, this is shilpa from PES UNIVERSITY");
            }
        }
        stage('Deploy') { 
            steps {
                echo 'shilpa'
            }
        }
    }


