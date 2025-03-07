﻿# Desafio Cognitiva Brasil

## Como Rodar o Projeto

### 1. Clonar o repositório

Clone este repositório em sua máquina local utilizando o comando:

```bash
git clone https://github.com/landeilsonveloso/desafio-cognitiva-brasil.git
```

### 2. Instalar as dependências

Entre no diretório do projeto e instale as dependências necessárias (certifique-se de estar utilizando o Python -x):

```bash
cd desafio-cognitiva-brasil
pip install -r requirements.txt
```

### 3. Obter as Chaves de API: OpenAI, Gemini (Google AI) e Mistral AI

#### Como Obter a Chave da API da OpenAI

#### Criar uma conta na OpenAI
- Acesse [https://platform.openai.com/signup](https://platform.openai.com/signup).
- Crie uma conta usando seu e-mail, Google ou Microsoft.
- Verifique seu e-mail e complete o cadastro.

#### Acessar o painel da OpenAI
- Faça login em [https://platform.openai.com/](https://platform.openai.com/).
- No canto superior direito, clique no seu perfil e selecione **"View API keys"**.

#### Gerar uma nova chave de API
- Na página de chaves de API, clique no botão **"Create new secret key"**.  
- Copie a chave gerada e guarde em um local seguro (não será possível vê-la novamente).

#### Como Obter a Chave da API do Gemini (Google AI)

#### Criar uma Conta no Google Cloud 
- Acesse o site do Google Cloud:  
   [https://console.cloud.google.com/](https://console.cloud.google.com/)  
- Faça login com uma conta Google.  
- Se for seu primeiro acesso, aceite os **Termos de Serviço** e **habilite o faturamento** (é necessário, mas a Google oferece um crédito inicial gratuito).  

#### Criar um Novo Projeto
- No menu superior, clique em **"Selecione um projeto"**.  
- Clique em **"Novo projeto"**.  
- Escolha um nome para o projeto e clique em **"Criar"**.  
- Aguarde alguns instantes até o projeto ser criado.  

#### Ativar a API do Gemini (Google AI)
- Acesse o site do **Google AI Studio**:  
   [https://makersuite.google.com/](https://makersuite.google.com/)  
- Faça login com sua conta Google.  
- No canto superior direito, clique em **"Get API Key"**.  
- Aceite os termos e permissões necessárias.

#### Copiar e Armazenar a Chave da API
- Após aceitar os termos, a Google gerará uma **chave secreta de API**.
- **Copie a chave** e armazene-a em um local seguro (não será possível visualizá-la novamente).

#### Como Obter a Chave da API do Mistral AI

#### Criar uma conta na Mistral AI
- Acesse o site oficial da Mistral AI:  
   [https://mistral.ai/](https://mistral.ai/)
- Clique em **"Get Started"** no canto superior direito.
- Faça login com seu e-mail ou crie uma nova conta.
- Confirme seu e-mail, se necessário.

#### Acessar o Painel de API
- Após fazer login, vá até o **Painel de Controle**.
- No menu lateral, clique na aba **"API"**.

#### Gerar uma Chave de API
- Dentro da aba **"API"**, clique no botão **"Create API Key"**.
- Um identificador será gerado automaticamente.
- **Copie a chave de API** e **guarde em um local seguro** (você não poderá visualizá-la novamente).

### 4. Crie um arquivo .env na raiz do projeto e adicione as chaves

```bash
OPENAI_API_KEY=YOUR_API_KEY
GEMINI_API_KEY=YOUR_API_KEY
MISTRALAI_API_KEY=YOUR_API_KEY
```

### 5. Rodar o projeto

Para rodar o projeto, basta executar o seguinte comando:

```bash
python src/main.py
```
