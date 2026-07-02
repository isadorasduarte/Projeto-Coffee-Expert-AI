# ☕ Base de Conhecimento - Coffee Expert AI

## 📦 Dados Utilizados

| Arquivo | Formato | Para que serve no Coffee Expert AI |
|----------|--------|-------------------------------------|
| conteudo_cafe.json | JSON | Contém informações principais sobre café (tipos, bebidas e preparo) |

---

## 🧠 Adaptações nos Dados

A base de conhecimento foi simplificada para focar apenas no universo do café, priorizando perguntas comuns como:

- O que é café?
- Diferença entre cappuccino e latte
- Como preparar café coado
- O que é espresso

O objetivo foi manter o conteúdo **simples, didático e acessível**, evitando termos muito técnicos para facilitar o uso por iniciantes.

---

## ⚙️ Estratégia de Integração

### Como os dados são carregados?

Os dados são carregados diretamente em Python a partir do arquivo JSON:

```python
import json

with open('./data/conhecimento.json', 'r', encoding='utf-8') as f:
    base_cafe = json.load(f)
```

---

### Como os dados são usados no prompt?

Para simplificar o projeto, os dados são **injetados diretamente no prompt do LLM**, garantindo que o modelo sempre tenha contexto suficiente para responder corretamente.

---

## ☕ BASE DE CONHECIMENTO (data/conhecimento.json)

```json
[
  {
    "tema": "O que é café?",
    "conteudo": "O café é uma bebida feita a partir dos grãos torrados da planta do café. É uma das bebidas mais consumidas do mundo e pode ser preparada de várias formas diferentes."
  },
  {
    "tema": "Quais são os tipos de café?",
    "conteudo": "Os principais tipos de café são: espresso, cappuccino, latte, café coado e café com leite."
  },
  {
    "tema": "O que é espresso?",
    "conteudo": "Espresso é um café concentrado feito sob pressão, com sabor intenso e encorpado."
  },
  {
    "tema": "O que é cappuccino?",
    "conteudo": "Cappuccino é uma bebida feita com espresso, leite vaporizado e espuma de leite."
  },
  {
    "tema": "O que é latte?",
    "conteudo": "Latte é uma bebida feita com espresso e bastante leite vaporizado, com pouca espuma."
  },
  {
    "tema": "Como fazer um cappuccino?",
    "conteudo": "Prepare um espresso, adicione leite vaporizado e finalize com espuma de leite em proporções equilibradas."
  },
  {
    "tema": "Como fazer um café coado?",
    "conteudo": "Coloque o café moído em um filtro, despeje água quente lentamente e aguarde a filtragem completa."
  },
  {
    "tema": "Como fazer um café com leite?",
    "conteudo": "Misture café pronto com leite quente na proporção desejada."
  },
  {
    "tema": "Qual a diferença entre cappuccino e latte?",
    "conteudo": "O cappuccino tem mais espuma e equilíbrio entre café, leite e espuma. O latte tem mais leite e menos espuma."
  },
  {
    "tema": "Qual café é mais forte?",
    "conteudo": "O espresso é considerado mais forte por ser mais concentrado e intenso."
  }
]
```

---

## 💬 Exemplo de Contexto Montado

Este é o formato final enviado ao LLM (Ollama), já resumido e estruturado:

```
DADOS DO USUÁRIO:
- Nome: Usuário
- Interesse: Café
- Objetivo: Aprender sobre tipos de café e formas de preparo
- Nível: Iniciante

BASE DE CONHECIMENTO (CAFÉ):

- O que é café: bebida feita a partir de grãos torrados da planta do café
- Tipos de café: espresso, cappuccino, latte, café coado, café com leite
- Espresso: café concentrado, forte e encorpado
- Cappuccino: espresso + leite vaporizado + espuma
- Latte: espresso + bastante leite + pouca espuma
- Cappuccino vs Latte: cappuccino tem mais espuma; latte tem mais leite
- Café mais forte: espresso
- Café coado: preparo com filtro e água quente
- Café com leite: mistura de café pronto com leite quente
```
