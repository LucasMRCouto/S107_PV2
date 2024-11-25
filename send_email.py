import os
import requests

def send_email():
    # Captura o e-mail do autor do último commit
    email_recipient = os.popen("git log -1 --pretty=format:'%ae'").read().strip()

    if not email_recipient:
        print("Erro: Não foi possível capturar o e-mail do autor do commit.")
        exit(1)

    # Mailgun API Key e URL
    mailgun_api_key = os.getenv("MAILGUN_API_KEY")  # API Key do Mailgun
    mailgun_domain = os.getenv("MAILGUN_DOMAIN")  # Domínio Mailgun
    mailgun_url = f"https://api.mailgun.net/v3/{mailgun_domain}/messages"

    # Detalhes do e-mail
    from_email = "no-reply04@sandboxb1d4be8e79454fdcb42de699e1f4374a.mailgun.org"  # O e-mail de envio (pode ser qualquer e-mail associado ao Mailgun)
    subject = "CI/CD Pipeline"
    body = "Pipeline executado com sucesso!"

    # Enviar o e-mail usando Mailgun
    response = requests.post(
        mailgun_url,
        auth=("api", mailgun_api_key),
        data={
            "from": from_email,
            "to": email_recipient,
            "subject": subject,
            "text": body
        })

    if response.status_code == 200:
        print(f"E-mail enviado para {email_recipient}")
    else:
        print(f"Erro ao enviar e-mail: {response.status_code} - {response.text}")


if __name__ == '__main__':
    send_email()
