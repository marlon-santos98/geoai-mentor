# GeoAI Mentor

Assistente conversacional para apoiar geocientistas na transicao para Ciencia de Dados, com foco em orientacao de carreira e sugestoes praticas de estudos e portfolio.

## Problema Resolvido

Uma chamada simples a LLM responde perguntas isoladas, mas nao sustenta contexto entre turnos. Neste projeto, o GeoAI Mentor evolui de um Q&A basico para um assistente com estado de conversa por sessao.

## Tecnologias

- Python 3.10+
- LangChain Core
- LangChain Groq
- Python Dotenv

## Estrutura do Projeto

- chatbot_mentor.py: fluxo completo de prompt, chamada ao modelo e memoria por sessao.
- .env: variaveis sensiveis (nao versionar).

## Configuracao do Ambiente

1. Criar e ativar ambiente virtual:

Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

2. Instalar dependencias:

pip install -r requirements.txt

3. Criar o arquivo .env na pasta do projeto com a chave da Groq:

GROQ_API_KEY=sua_chave_aqui

## Como Executar

Na pasta do projeto, execute:

python chatbot_mentor.py

## Exemplo de Interacao

### Antes (sem memoria)

Pergunta 1: Eu sou geofisico e quero migrar para a area de dados. Qual linguagem devo aprender primeiro?
Resposta: Python e uma boa primeira linguagem para Ciencia de Dados.

Pergunta 2: E que tipo de projeto de portfolio eu poderia criar usando essa linguagem?
Resposta: Voce pode criar um projeto de analise de dados.

Observacao: sem memoria, a segunda resposta tende a ser generica e nao retoma o contexto detalhado da primeira.

### Depois (com memoria por sessao)

Pergunta 1: Eu sou geofisico e quero migrar para a area de dados. Qual linguagem devo aprender primeiro?
Resposta: Python, principalmente com pandas, numpy e visualizacao.

Pergunta 2: E que tipo de projeto de portfolio eu poderia criar usando essa linguagem?
Resposta: Como voce vem da geofisica, crie um projeto com dados geoespaciais/sismicos: limpeza, analise exploratoria, previsao simples e dashboard.

Observacao: com memoria, a segunda resposta aproveita o contexto da conversa e fica mais personalizada.

## Arquitetura

Fluxo principal da cadeia:

Prompt Template -> Modelo LLM -> Parser de Saida

- ChatPromptTemplate: define persona, placeholder de historico e pergunta atual.
- ChatGroq: gera a resposta do modelo.
- StrOutputParser: devolve apenas o texto final.

Adicao de estado:

- RunnableWithMessageHistory envolve a cadeia base.
- InMemoryChatMessageHistory guarda as mensagens por session_id.
- obter_historico_por_sessao implementa singleton por sessao.


## Aprendizados

- ChatPromptTemplate foi essencial para definir persona e padrao de resposta.
- RunnableWithMessageHistory resolveu o desafio de manter contexto entre turnos.
- A diferenca entre IA sem estado e com estado fica clara na qualidade da segunda resposta.
- Organizar cadeia e memoria em blocos separados facilitou manutencao e evolucao.

