# Usando a imagem base do Jenkins
FROM jenkins/jenkins:lts

# Definir o usuário root para instalar pacotes
USER root

# Atualizar pacotes e instalar Python 3, pip, venv e outras dependências básicas, incluindo zip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    mailutils \
    zip \
    && rm -rf /var/lib/apt/lists/*

# Retornar para o usuário padrão do Jenkins
USER jenkins

# Expor a porta do Jenkins
EXPOSE 8080
