pipeline {
    agent {
        docker {
            image 'python:3.9-bullseye'
            args '-p 3000:3000'
        }
    }
    stages {
        stage('cek versi python') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Jalankan Script') { 
            steps {
                echo 'ini menjalankan Script' 
            }
        }
    }
}