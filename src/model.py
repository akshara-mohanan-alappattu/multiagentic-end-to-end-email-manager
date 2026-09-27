from langchain_groq import ChatGroq
from src.state import IdentifierState


def call_llm():
    call_llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
     )
    return call_llm

def llm_at_identifier():
    llm=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3
        )
    llm_at_identifier=llm.with_structured_output(IdentifierState)
    return llm_at_identifier


