from src.state import AgentState,IdentifierState
from src.prompts import IdentifierPrompt
# from src.model import llm_at_identifier
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3
        )
llm_at_identifier=llm.with_structured_output(IdentifierState)

def analyse_identify_function(state:AgentState):
    """
        Identifier determines WHAT information is needed.
        What category is this email?
        What is the email about?
        What information is needed to answer it?
        Is external/internal data actually required?
    """
    try:
        email=state.input.email_body
        indentifier_prompt=IdentifierPrompt()
        identifier_llm_input=[indentifier_prompt,email]
        response_at_identifier=llm_at_identifier.invoke(identifier_llm_input)
        return {"contents_identified":response_at_identifier}
    except Exception as e:
        print(f"error while identifying :{e}")
        raise

