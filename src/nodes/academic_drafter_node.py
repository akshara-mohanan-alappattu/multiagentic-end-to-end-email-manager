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
        data_str="\n".join(
    f"- {item}" for item in data_for_drafting
            )
        if state.review:
            recommendations=state.review.recommendations
            recommendations_str="\n".join(
    f"- {item}" for item in recommendations
            )
        else:
            recommendations=None
            recommendations_str=None
        if state.human_approval:
            feedback=state.human_approval.human_feedback
            feedback_str = "\n".join(
    f"- {item}" for item in feedback
            )
        else:
            feedback=None
            feedback_str=None
        prompt=AcademicPrompt()
        academic_llm_input=f"""
        {prompt}
        Email summary:{email_summary}
        Data Required to draft mail: {data_str}
        Feedback received:{feedback_str}
        Recommendation:{recommendations_str}
"""
    
        response_at_academic=llm_at_drafter.invoke(academic_llm_input)
        return{"draft":{
            "draft_email":response_at_academic.content
        }
        } 
    except Exception as e:
        print(f"error while drafting :{e}")
        raise
