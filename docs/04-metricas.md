# ☕ Avaliação e Métricas - Coffee Expert AI

## 🧪 Como Foi Avaliado o Agente

A avaliação do Coffee Expert AI foi feita de duas formas complementares:

- Testes estruturados com perguntas pré-definidas
- Feedback qualitativo de usuários

O objetivo é validar se o agente responde corretamente sobre café, mantém coerência e evita respostas fora do escopo.

---

# 📏 Métricas de Qualidade

## ☕ Assertividade
Avalia se o agente responde corretamente às perguntas sobre café com base na base de conhecimento.

**Exemplo:**
Pergunta: O que é cappuccino?  
Esperado: Explicação correta sobre espresso + leite + espuma

---

## 🛡️ Segurança
Avalia se o agente evita inventar respostas e reconhece quando não sabe algo.

**Exemplo:**
Pergunta: Quem inventou o café no Brasil?  
Esperado: Informar que não possui essa informação ou que não sabe

---

## 🧠 Coerência
Avalia se as respostas fazem sentido dentro do tema café e seguem o tom definido.

**Exemplo:**
Pergunta: Qual café é mais forte?  
Esperado: Explicação coerente sobre espresso ser mais intenso

---

# 🧪 Cenários de Teste

---

## ☕ Teste 1: Conceito básico

**Pergunta:**  
O que é café?

**Resposta esperada:**  
Explicação simples sobre café como bebida feita de grãos torrados.

**Resultado:**  
[X] Correto  [ ] Incorreto

---

## ☕ Teste 2: Preparação

**Pergunta:**  
Como fazer um café coado?

**Resposta esperada:**  
Explicação do uso de filtro e água quente passando pelo pó.

**Resultado:**  
[X] Correto  [ ] Incorreto

---

## ☕ Teste 3: Comparação

**Pergunta:**  
Qual a diferença entre latte e cappuccino?

**Resposta esperada:**  
Latte tem mais leite e menos espuma; cappuccino é equilibrado com mais espuma.

**Resultado:**  
[X] Correto  [ ] Incorreto

---

## 🚫 Teste 4: Fora do escopo

**Pergunta:**  
Quem ganhou a Copa do Mundo?

**Resposta esperada:**  
Agente informa que só responde sobre café.

**Resultado:**  
[X] Correto  [ ] Incorreto

---


# 📈 Resultados da Avaliação

## ✔️ O que funcionou bem

- Respostas claras e simples sobre café
- Boa consistência nas explicações
- Bom controle de escopo 
- Linguagem acessível para iniciantes

---

## ⚠️ O que pode melhorar

- Expandir a base de conhecimento com mais tipos de café
- Adicionar memória de conversa
- Melhorar respostas mais detalhadas para usuários avançados
- Incluir sugestões automáticas de aprendizado

---
