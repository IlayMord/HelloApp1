pipeline {
    agent any

    stages {

        stage('Checkout Info') {
            steps {
                echo 'Pipeline from Git is running'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Python Check') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build') {
            steps {
                sh 'mkdir -p build'
                sh 'echo "build artifact" > build/app.txt'
                sh 'cat build/app.txt'
            }
        }
    }
}