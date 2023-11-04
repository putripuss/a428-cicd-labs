pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-p 3000:3000'
        }
    }
    stages {
        stage('Cek versi python') {
            steps {
                sh 'python --version'
            }
        }
        stage('Jalankan Script') { 
            steps {
                sh 'python dihibrida.py' 
            }
        }
    }
}
