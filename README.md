Automação de Disparo de E-mails com Python e Pandas

Este script em Python automatiza o envio de e-mails personalizados em lote a partir de uma lista estruturada em um arquivo .csv. Ele extrai automaticamente o primeiro nome de cada destinatário, formata a inicial em letra maiúscula e insere um link personalizado do Google Forms no corpo da mensagem.

🛠️ Tecnologias e Dependências

Para executar este script, você precisará ter o Python instalado em sua máquina, juntamente com a biblioteca Pandas para manipulação dos dados.

Instalação da Dependência

No seu terminal ou prompt de comando, execute:

pip install pandas


📁 Estrutura do Arquivo CSV

O script espera encontrar um arquivo .csv (que pode ser convertido a partir da lista fornecida em formato .docx pelo professor) contendo pelo menos duas colunas principais:

nome: Nome completo do destinatário.

email: Endereço de e-mail do destinatário.

Exemplo de estrutura do arquivo CSV:

nome,email
GUSTAVO SILVA,gustavo@exemplo.com
MARIANA SOUZA,mariana@exemplo.com


⚙️ Como Configurar o Script

Abra o arquivo enviar_email.py e altere a seção de CONFIGURAÇÕES no início do código:

# ==================== CONFIGURAÇÕES ====================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "seu_email@gmail.com"
SENDER_PASSWORD = "sua_senha_de_aplicativo"  # Veja o passo a passo abaixo

# Caminho do arquivo CSV (ex: "lista_alunos.csv")
ARQUIVO_CSV = "NOME_DO_ARQUIVO.csv"

# Link do Google Forms
link_forms = "https://forms.gle/SEU_LINK"
# ========================================================


🔐 Como Obter a Senha de Aplicativo do Gmail

Por motivos de segurança, o Google não permite que você utilize sua senha principal do Gmail diretamente em scripts de automação. É necessário gerar uma Senha de Aplicativo (App Password) específica.

Siga o passo a passo abaixo para criá-la:

Acesse a sua Conta Google em myaccount.google.com.

No menu lateral esquerdo, clique em Segurança.

Na seção "Como fazer login no Google", certifique-se de que a Verificação em duas etapas está ativada (etapa obrigatória para gerar senhas de app).

Ainda na página de Segurança, procure pela barra de pesquisa ou clique diretamente na opção Senhas de app.

Dê um nome para identificar o seu aplicativo (por exemplo: AutomacaoPython) e clique em Gerar.

O Google exibirá uma senha de 16 caracteres. Copie essa senha.

Cole os 16 caracteres dentro das aspas da variável SENDER_PASSWORD no script Python.

🚀 Como Executar

Com o arquivo CSV na mesma pasta do script e as configurações devidamente preenchidas, execute o comando no terminal:

python enviar_email.py


O console exibirá o progresso da leitura dos dados, a conexão com o servidor SMTP e uma mensagem de confirmação para cada e-mail disparado com sucesso!
