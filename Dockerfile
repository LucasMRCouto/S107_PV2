# Use uma imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia as dependências para dentro do container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o container
COPY . .

# Define o comando padrão para rodar os testes
CMD ["python", "-m", "unittest", "discover", "-s", "app/tests"]
