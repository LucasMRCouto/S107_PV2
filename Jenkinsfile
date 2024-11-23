pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }
    environment {
        EMAIL_RECIPIENT = "${env.EMAIL}"
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'python -m unittest discover -s app/tests > result.log || true'
                    archiveArtifacts artifacts: 'result.log', allowEmptyArchive: true
                }
            }
        }
        stage('Build') {
            steps {
                sh 'zip -r app.zip app/'
                archiveArtifacts artifacts: 'app.zip', fingerprint: true
            }
        }
        stage('Notify') {
            steps {
                sh './send_email.sh'
            }
        }
    }
}
