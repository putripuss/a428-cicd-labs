pipeline {
    agent {
        docker {
            image 'node:18.17.1' // Menggunakan gambar Node.js versi 18
            args '-p 3000:3000'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'node --version' // Menampilkan versi Node.js
                sh 'npm install' // Menginstal dependensi proyek
            }
        }
        stage('Test') { 
            steps {
                sh 'npm test' // Menjalankan skrip pengujian
            }
        }
        stage('Hybridize') {
            steps {
                sh 'node hibridize.js' // Menjalankan skrip hibridize
            }
        }
    }
}
