from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from dotenv import load_dotenv

load_dotenv()

cliente = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

template_prompts = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático."),
    ("placeholder", "{historico}"),
    ("human", "{query}")
])

cadeia = template_prompts | cliente | StrOutputParser()

perguntas = [ 
            "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
            "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
            
]

memoria_sessoes = {}

def obter_historico_por_sessao(session_id:str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)

session_id = "usuario_1"

for pergunta in perguntas:
    print(f"Pergunta: {pergunta}")
    resposta = cadeia_com_memoria.invoke(
        {"query": pergunta},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"Resposta: {resposta}\n")
