pipeline {
    agent {
        docker {
            image 'python:3.11.5-bullseye'
            args '-p 3000:3000'
        }
    }
    stages {
        stage('cek versi python') {
            steps {
                sh 'python --version'
            }
        }
        stage('Jalankan Script Python') {
            steps {
                script {
                    // Jalankan skrip Python dengan argumen 3 dan 11
                    sh 'python python_script.py 3 11'
                }
            }
        }
        stage('Set Jawaban') {
            steps {
                script {
                    env.JAWABAN = input message: 'Masukkan jawaban:', parameters: [string(defaultValue: '', description: 'Jawaban')]
                }
            }
        }
    }
}
