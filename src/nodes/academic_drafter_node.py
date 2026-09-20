from src.state import AgentState
from src.prompts import AcademicPrompt
from src.model import call_llm

def academic_email_drafter(state:AgentState):
    email_summary=state.contents_identified.summary
    prompt=AcademicPrompt()
    academic_llm_input=[prompt,email_summary]
    response_at_academic=call_llm.invoke(academic_llm_input)
    return response_at_academic
