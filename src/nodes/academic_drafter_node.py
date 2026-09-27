from src.state import AgentState
from src.prompts import AcademicPrompt
from src.model import call_llm
llm_at_drafter=call_llm()
def academic_email_drafter(state:AgentState):
    email_summary=state.contents_identified.summary
    prompt=AcademicPrompt()
    academic_llm_input=[prompt,email_summary]
    response_at_academic=llm_at_drafter.invoke(academic_llm_input)
    return response_at_academic
