from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas as pd 

# ==================== CONFIGURAÇÕES ====================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "SEU_EMAIL@gmail.com"
SENDER_PASSWORD = (  # noqa: S107
    "SENHA_APLICATIVO"  # Use a senha de aplicativo do Gmail
)

# Caminho do arquivo CSV
ARQUIVO_CSV = "NOME_DO_ARQUIVO" # PEdir para a ia passar para o CSV, o professor deu em docx

# Link do Google Forms
link_forms = "SEU_LINK"
# ========================================================


def enviar_emails():
  try:
    # Lendo o arquivo CSV com pandas
    print(f"Lendo o arquivo '{ARQUIVO_CSV}'...")
    df = pd.read_csv(ARQUIVO_CSV)

    # Verificando se as colunas necessárias existem no CSV
    if "nome" not in df.columns or "email" not in df.columns:
      print(
          "Erro: O arquivo CSV precisa conter exatamente as colunas 'nome' e"
          " 'email'."
      )
      return

    print("Conectando ao servidor SMTP...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("Autenticação realizada com sucesso!\n")

    # Percorrendo cada linha do DataFrame do pandas
    for index, row in df.iterrows():
      # Pega apenas o primeiro nome (ex: "João Silva" vira "João")
      nome_completo = str(row["nome"])
      primeiro_nome = nome_completo.split()[0].capitalize()

      email = row["email"]

      # Criando a estrutura da mensagem
      msg = MIMEMultipart()
      msg["From"] = SENDER_EMAIL
      msg["To"] = email
      msg["Subject"] = "Ajuda com questionário de pesquisa"

      # Corpo do e-mail formatado em HTML
      corpo = f"""
            <p>Bom dia <strong>{primeiro_nome}</strong>, tudo bem?</p>
            <p>Você poderia por gentileza responder o meu questionário?</p>
            <p>O link é: <a href="{link_forms}">{link_forms}</a></p>
            <p>Agradeço muito pela ajuda!</p>
            <br>
            <p>Atenciosamente,</p>
            <p>Seu nome</p>
            """

      msg.attach(MIMEText(corpo, "html", "utf-8"))

      # Enviando o e-mail
      server.sendmail(SENDER_EMAIL, email, msg.as_string())
      print(
          f"E-mail enviado com sucesso para: {primeiro_nome} ({email})"
      )

    server.quit()
    print("\nProcesso concluído! Todos os e-mails foram enviados.")

  except Exception as e:
    print(f"Ocorreu um erro durante o processo: {e}")


if __name__ == "__main__":
  enviar_emails()