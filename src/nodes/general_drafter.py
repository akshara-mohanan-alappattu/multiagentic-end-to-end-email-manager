from src.state import AgentState
from src.prompts import GeneralPrompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm_at_drafter=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3
        )

def general_emai_drafter(state:AgentState):
    try:
        email_summary=state.contents_identified.summary
        prompt=GeneralPrompt()
        general_llm_input=[prompt,email_summary]
        response=llm_at_drafter.invoke(general_llm_input)
        return{"draft":response.content} 
    except Exception as e:
        print(f"error while drafting :{e}")
        raise
