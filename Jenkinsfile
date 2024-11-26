pipeline {

    agent any

    environment {
        EMAIL_RECIPIENT = "${env.EMAIL}"  // Defina a variável de ambiente para o e-mail
        MAILGUN_API_KEY = "9f1551a672dd388c7f89c3304a6e3e2a-c02fd0ba-0513bfdc"  // Chave da API do Mailgun (substitua pela sua chave)
        MAILGUN_DOMAIN = "sandboxb1d4be8e79454fdcb42de699e1f4374a.mailgun.org"  // Seu domínio Mailgun (exemplo: sandboxXXXX.mailgun.org)

        EMAIL_USERNAME = "s107pv2@gmail.com"  // E-mail remetente
        EMAIL_PASSWORD = "projetos107"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies...'
                script {
                    // Instalar Node.js
                    sh '''
                        curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
                        apt-get install -y nodejs
                        node --version
                        npm --version
                    '''

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
                    sh '''
                        npm install nodemailer dotenv
                        export EMAIL_TO_NOTIFY=$(git log -1 --pretty=format:'%ae')
                        node send_email.js
                    '''
                }
            }
        }
    }
}
