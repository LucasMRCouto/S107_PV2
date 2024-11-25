pipeline {

    agent any

    environment {
        EMAIL_RECIPIENT = "${env.EMAIL}"  // Defina a variável de ambiente para o e-mail
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies...'
                script {
                    // Instalar as dependências do Python usando o pip dentro do ambiente virtual
                    sh '''
                        python3 -m venv venv
                        ./venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Tests...'
                script {
                    // Rodar os testes unitários usando o ambiente virtual
                    sh '''
                        ./venv/bin/python -m unittest discover -s app/tests > result.log || true
                    '''
                    // Arquivar os resultados dos testes
                    archiveArtifacts artifacts: 'result.log', allowEmptyArchive: true
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building Project...'
                script {
                    // Criar um arquivo zip com o código-fonte e dependências (excluindo venvs e diretorios git)
                    sh '''
                        mkdir -p build
                        zip -r build/project.zip . -x "venv/*" "*.git/*" "build/*"
                    '''
                    // Arquivar o pacote gerado
                    archiveArtifacts artifacts: 'build/project.zip', fingerprint: true
                }
            }
        }

        stage('Notification') {
            steps {
                echo 'Sending Notification...'
                script {
                    // Enviar e-mail com o status da execução
                    sh './send_email.sh'
                }
            }
        }
    }
}
