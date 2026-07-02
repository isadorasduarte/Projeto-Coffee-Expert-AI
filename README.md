# ☕ Coffee Expert AI

Um assistente virtual inteligente especializado em café, capaz de responder dúvidas sobre tipos de café, métodos de preparo e diferenças entre bebidas, utilizando uma base de conhecimento própria e modelo local via Ollama.

---

## 🚀 Sobre o Projeto

O **Coffee Expert AI** é um chatbot desenvolvido com Python, Streamlit e Ollama que atua como um barista virtual.

Ele foi criado com o objetivo de:

- Ensinar conceitos sobre café de forma simples e didática ☕
- Explicar diferenças entre bebidas como espresso, latte e cappuccino
- Responder apenas perguntas relacionadas ao universo do café
- Evitar respostas inventadas utilizando uma base de conhecimento estruturada

---

## 🧠 Como funciona

1. O usuário faz uma pergunta no chat
2. O sistema carrega a base de conhecimento (`conteudo_cafe.json`)
3. O contexto é enviado para o modelo local via Ollama
4. O modelo gera uma resposta baseada apenas no contexto fornecido
5. A resposta é exibida na interface do Streamlit

---

## 📚 Base de Conhecimento

O arquivo `conteudo_cafe.json` contém informações como:

- O que é café
- Tipos de café
- Espresso
- Cappuccino
- Latte
- Métodos de preparo
- Diferenças entre bebidas

---

## ⚙️ Tecnologias Utilizadas

- Python 🐍
- Streamlit 🎨
- Requests 🌐
- Ollama 🤖
- LLM 

---

## ▶️ Como Executar o Projeto

### 1. Instalar dependências

```bash
pip install streamlit requests
```

---

### 2. Instalar o Ollama

Baixe em: https://ollama.com

Depois instale um modelo leve:

```bash
ollama pull llama3.2:3b
```

---

### 3. Rodar o modelo

```bash
ollama run llama3.2:3b
```

---

### 4. Executar a aplicação

```bash
streamlit run app.py
```

---

## 💬 Exemplo de Uso

**Usuário:**
> O que é cappuccino?

**Coffee Expert AI:**
> Cappuccino é uma bebida feita com espresso, leite vaporizado e espuma de leite em proporções equilibradas...

---

## ⚠️ Limitações

- O assistente responde apenas sobre café ☕
- Não fornece informações fora da base de conhecimento
- Depende do modelo local do Ollama estar rodando

---

## 🎯 Objetivo

Este projeto demonstra como construir um assistente virtual simples utilizando:

- IA local (Ollama)
- Base de conhecimento estruturada
- Interface web com Streamlit
- Controle de respostas via prompt engineering

---
