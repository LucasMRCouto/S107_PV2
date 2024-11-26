const nodemailer = require("nodemailer");
require("dotenv").config(); // Para carregar as variáveis de ambiente, se necessário

// Função para criar o transporte de e-mails
function createTransporter() {
    const email = process.env.EMAIL_USERNAME;
    const password = process.env.EMAIL_PASSWORD;

    if (!email || !password) {
        console.error("Erro: Variáveis de ambiente EMAIL_USERNAME ou EMAIL_PASSWORD não estão configuradas.");
        process.exit(1);
    }

    return nodemailer.createTransport({
        service: "gmail", // ou outro serviço SMTP
        auth: {
            user: email,
            pass: password, // Use uma senha de app para segurança
        },
    });
}

// Função para enviar o e-mail
async function sendEmail(recipient) {
    console.log("Iniciando envio de e-mail...");

    const transporter = createTransporter();
    const subject = "CI/CD Pipeline Notification";
    const text = `Olá,

O pipeline foi executado com sucesso!

Status: Concluído com sucesso
Data: ${new Date().toLocaleString()}

Verifique os detalhes no Jenkins.

Atenciosamente,
Equipe CI/CD`;

    try {
        const info = await transporter.sendMail({
            from: `"Jenkins CI/CD" <${process.env.EMAIL_USERNAME}>`,
            to: recipient,
            subject: subject,
            text: text,
        });

        console.log("E-mail enviado com sucesso para %s (ID: %s)", recipient, info.messageId);
    } catch (error) {
        console.error("Erro ao enviar o e-mail:", error);
        process.exit(1);
    }
}

// Captura o destinatário do último commit e envia o e-mail
(async () => {
    const recipient = process.env.EMAIL_TO_NOTIFY;

    if (!recipient) {
        console.error("Erro: A variável de ambiente EMAIL_TO_NOTIFY não está configurada.");
        process.exit(1);
    }

    await sendEmail(recipient);
})();
