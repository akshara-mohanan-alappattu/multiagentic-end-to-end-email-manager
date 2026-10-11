from src.state import AgentState
from src.prompts import AcademicPrompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm_at_drafter=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3
        )

def academic_email_drafter(state:AgentState):
    try:
        email_summary=state.contents_identified.summary
        data_for_drafting=state.retreive_data.retreived_data[0]
        if state.review:
            recommendations=state.review.recommendations
        else:
            recommendations=""
        if state.human_approval:
            feedback=state.human_approval.human_feedback
        else:
            feedback=""
        prompt=AcademicPrompt()
        academic_llm_input=[prompt,email_summary,data_for_drafting,recommendations,feedback]
        response_at_academic=llm_at_drafter.invoke(academic_llm_input)
        return{"draft":{
            "draft_email":response_at_academic.content
        }
        } 
    except Exception as e:
        print(f"error while drafting :{e}")
        raise
