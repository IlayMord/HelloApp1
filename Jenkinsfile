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