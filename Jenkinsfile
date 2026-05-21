pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'qa', 'prod'],
            description: 'Choose environment'
        )

        string(
            name: 'VERSION',
            defaultValue: '1.0.0',
            description: 'Application version'
        )
    }

    stages {

        stage('Show Params') {
            steps {
                sh 'echo "Environment: $ENV"'
                sh 'echo "Version: $VERSION"'
            }
        }

        stage('Build Artifact') {
            steps {
                sh 'mkdir -p build'
                sh 'echo "artifact for $ENV version $VERSION" > build/info.txt'
                sh 'cat build/info.txt'
            }
        }

        stage('Quality Checks') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'echo "Running unit tests"'
                        sh 'sleep 5'
                        sh 'echo "Unit tests passed"'
                    }
                }

                stage('Lint') {
                    steps {
                        sh 'echo "Running lint"'
                        sh 'sleep 5'
                        sh 'echo "Lint passed"'
                    }
                }

                stage('Security Scan') {
                    steps {
                        sh 'echo "Running security scan"'
                        sh 'sleep 5'
                        sh 'echo "Security scan passed"'
                    }
                }
            }
        }
        
        stage('Production Approval') {

            when {
                expression {
                    ENV == 'prod'
                }
            }

            steps {
                input message: 'Approve deployment to production?'
            }
        }

        stage('Production Deploy') {

            when {
                expression {
                    ENV == 'prod'
                }
            }

            steps {
                sh 'echo "Deploying to PRODUCTION"'
            }
        }
            }

    post {

        always {
            echo 'Pipeline finished'
        }

        success {
            echo 'Pipeline succeeded'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}