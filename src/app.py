import json
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

with open('./data/conteudo_cafe.json', 'r', encoding='utf-8') as f:
    base_conhecimento = json.load(f)


conhecimento_texto = "\n".join(
    [f"{item['tema']}: {item['conteudo']}" for item in base_conhecimento]
)


contexto = f"""
BASE DE CONHECIMENTO SOBRE CAFÉ:

{conhecimento_texto}
"""


SYSTEM_PROMPT = """
Você é o Coffee Expert AI, um barista virtual especialista em café.

OBJETIVO:
Ensinar tudo sobre café de forma simples, clara e didática.

REGRAS:
- Responda APENAS perguntas relacionadas a café;
- Use somente a base de conhecimento fornecida;
- Não invente informações;
- Se não souber, diga: "Não encontrei essa informação na minha base de conhecimento sobre café.";
- Linguagem simples e amigável;
- Explique como para iniciantes;
- Respostas curtas e objetivas (máximo 3 parágrafos);
- Nunca saia do tema café.

TOM:
- Amigável ☕
- Didático 📚
- Simples 🧠
"""


def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO:
{contexto}

PERGUNTA DO USUÁRIO:
{msg}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


st.set_page_config(page_title="Coffee Expert AI ☕")

st.title("☕ Coffee Expert AI")
st.caption("Seu barista virtual para aprender tudo sobre café")

if "chat" not in st.session_state:
    st.session_state.chat = []


for role, text in st.session_state.chat:
    st.chat_message(role).write(text)


if pergunta := st.chat_input("Pergunte algo sobre café..."):
    st.session_state.chat.append(("user", pergunta))
    st.chat_message("user").write(pergunta)

    with st.spinner("Pensando... ☕"):
        resposta = perguntar(pergunta)

    st.session_state.chat.append(("assistant", resposta))
    st.chat_message("assistant").write(resposta)
