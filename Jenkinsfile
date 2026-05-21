pipeline {
    agent any

    environment {
        APP_NAME = 'hello-app'
        VERSION = '1.0.0'
        ENVIRONMENT = 'dev'
    }

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

        stage('Jenkins Env Info') {
            steps {
                sh 'echo "Build number: $BUILD_NUMBER"'
                sh 'echo "Job name: $JOB_NAME"'
                sh 'echo "Workspace: $WORKSPACE"'
            
            }
        }   

        stage('App Info') {
            steps {
                sh 'echo "App name: $APP_NAME"'
                sh 'echo "Version: $VERSION"'
                sh 'echo "Environment: $ENVIRONMENT"'
                sh 'echo "Artifact name: $APP_NAME-$VERSION-$BUILD_NUMBER.txt"'
            }
        }
    
    }
}