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

        stage('Break Pipeline') {
            steps {
                sh 'echo "Breaking pipeline..."'
                sh 'exit 1'
            }
        }
        
        stage('Build Artifact') {
            steps {
                sh 'mkdir -p build'
                sh 'echo "artifact for $ENV version $VERSION" > build/info.txt'
                sh 'cat build/info.txt'
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