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
        stage('Set Jawaban') {
            steps {
                script {
                    env.JAWABAN = input message: 'Masukkan jawaban:', parameters: [string(defaultValue: '', description: 'Jawaban')]
                }
            }
        }
        // ... Tahap lainnya
    }
}
