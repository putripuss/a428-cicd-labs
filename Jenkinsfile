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
                sh 'python --version'
            }
        }
        stage('Jalankan Script') { 
            steps {
                sh 'python python_script.py' 
            }
        }
    }
}