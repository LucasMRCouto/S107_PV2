# CI/CD Pipeline - S107_PV2

Este projeto implementa um pipeline de CI/CD com **Jenkins**, **Python** e **Docker** para executar testes automatizados e enviar notificações por email.

## Alunos

- Frederico Flauzino Wlassow
- Lucas Mendes Ribeiro do Couto


### Pré-requisitos

- **Docker** (para rodar o Jenkins).
- **Python 3.8 ou superior**.
- **Gmail**: Configure uma senha de aplicativo para o envio de notificações.

## Instalação e Execução

1. Clone o repositório e vá até o diretório do projeto:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instalar as Dependências (localmente, já que o Jenkins faz automático na execução do pipeline):
   ```bash
   pip install -r requirements.txt
   npm install nodemailer dotenv
   ```

3. Executar os Testes Python:
   ```bash
   python -m unittest discover -s app/tests
   ```

4. Envie notificações por email (localmente para testes):
   ```bash
   export EMAIL_USERNAME="seu_email@gmail.com"
   export EMAIL_PASSWORD="sua_senha_de_aplicativo"
   export EMAIL_TO_NOTIFY="destinatario@example.com"
   node send_email.js
   ```

## Configuração do Pipeline Jenkins
- Faça o download da imagem no docker hub:
   ```bash
   docker pull lucasmrcouto/jenkins-python
   ```

- Suba o container Jenkins+Python com Docker:
   ```bash
   docker run -d -p 8080:8080 -p 50000:50000 lucasmrcouto/jenkins-python
   ```
- Configure as seguintes variáveis de ambiente no Jenkinsfile:
   ```bash
   EMAIL_USERNAME: O e-mail do remetente.  
   EMAIL_PASSWORD: A senha de aplicativo do Gmail.  
   EMAIL_TO_NOTIFY: O email do autor do último commit (definido dinamicamente no pipeline)
   ```

### Ao executar o pipeline, ele irá:

- Instalar dependências.  
- Rodar testes automatizados.  
- Enviar notificações por email com o status do pipeline.  
