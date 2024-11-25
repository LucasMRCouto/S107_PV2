#!/bin/bash

# Captura o e-mail do autor do último commit
EMAIL_RECIPIENT=$(git log -1 --pretty=format:'%ae')

# Verifica se o e-mail foi capturado corretamente
if [ -z "$EMAIL_RECIPIENT" ]; then
    echo "Erro: Não foi possível capturar o e-mail do autor do commit."
    exit 1
fi

# Usando Python para enviar o e-mail via Gmail
python3 <<EOF
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Pipeline executado com sucesso!")
msg['Subject'] = "CI/CD Pipeline"
msg['From'] = "seu_email@gmail.com"
msg['To'] = "$EMAIL_RECIPIENT"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("seu_email@gmail.com", "sua_senha")
    server.send_message(msg)

print("E-mail enviado para $EMAIL_RECIPIENT")
EOF
