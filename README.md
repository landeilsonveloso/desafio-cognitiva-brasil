# Desafio Cognitiva Brasil

## Como Rodar o Projeto

### 1. Clonar o repositório

Clone este repositório em sua máquina local utilizando o comando:

```bash
git clone https://github.com/landeilsonveloso/desafio-cognitiva-brasil.git
```

### 2. Instalar as dependências

Entre no diretório do projeto e instale as dependências necessárias (certifique-se de estar utilizando o Python 3.x):

```bash
cd desafio-cognitiva-brasil
pip install -r requirements.txt
```

### 3. Obter as Chaves de API: OpenAI, Gemini (Google AI) e Mistral AI

#### Como Obter a Chave da API da OpenAI

#### 1. Criar uma conta na OpenAI
1. Acesse [https://platform.openai.com/signup](https://platform.openai.com/signup).
2. Crie uma conta usando seu e-mail, Google ou Microsoft.
3. Verifique seu e-mail e complete o cadastro.

#### 2. Acessar o painel da OpenAI
1. Faça login em [https://platform.openai.com/](https://platform.openai.com/).
2. No canto superior direito, clique no seu perfil e selecione **"View API keys"**.

#### 3. Gerar uma nova chave de API
1. Na página de chaves de API, clique no botão **"Create new secret key"**.  
2. Copie a chave gerada e guarde em um local seguro (não será possível vê-la novamente).

#### Como Obter a Chave da API do Gemini (Google AI)

#### 1. Criar uma Conta no Google Cloud 
1. Acesse o site do Google Cloud:  
   [https://console.cloud.google.com/](https://console.cloud.google.com/)  
2. Faça login com uma conta Google.  
3. Se for seu primeiro acesso, aceite os **Termos de Serviço** e **habilite o faturamento** (é necessário, mas a Google oferece um crédito inicial gratuito).  

#### 2. Criar um Novo Projeto
1. No menu superior, clique em **"Selecione um projeto"**.  
2. Clique em **"Novo projeto"**.  
3. Escolha um nome para o projeto e clique em **"Criar"**.  
4. Aguarde alguns instantes até o projeto ser criado.  

#### 3. Ativar a API do Gemini (Google AI)
1. Acesse o site do **Google AI Studio**:  
   [https://makersuite.google.com/](https://makersuite.google.com/)  
2. Faça login com sua conta Google.  
3. No canto superior direito, clique em **"Get API Key"**.  
4. Aceite os termos e permissões necessárias.

#### 4. Copiar e Armazenar a Chave da API
1. Após aceitar os termos, a Google gerará uma **chave secreta de API**.
2. **Copie a chave** e armazene-a em um local seguro (não será possível visualizá-la novamente).

#### Como Obter a Chave da API do Mistral AI

#### 1. Criar uma conta na Mistral AI
1. Acesse o site oficial da Mistral AI:  
   [https://mistral.ai/](https://mistral.ai/)
2. Clique em **"Get Started"** no canto superior direito.
3. Faça login com seu e-mail ou crie uma nova conta.
4. Confirme seu e-mail, se necessário.

#### 2. Acessar o Painel de API
1. Após fazer login, vá até o **Painel de Controle**.
2. No menu lateral, clique na aba **"API"**.

#### 3. Gerar uma Chave de API
1. Dentro da aba **"API"**, clique no botão **"Create API Key"**.
2. Um identificador será gerado automaticamente.
3. **Copie a chave de API** e **guarde em um local seguro** (você não poderá visualizá-la novamente).

### 4. Crie um arquivo .env na raiz do projeto e adicione as chaves

```bash
API_KEY_CHATGPT=YOUR_API_KEY
API_KEY_GEMINI=YOUR_API_KEY
API_KEY_MISTRALAI=YOUR_API_KEY
```

### 4. Rodar o projeto

Para rodar o projeto, basta executar o seguinte comando:

```bash
python main.py
```
