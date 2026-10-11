from src.state import AgentState, ReviewState
from langchain_groq import ChatGroq
from src.prompts import ReviewPrompt 

llm=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3
        )
llm_at_reviewer=llm.with_structured_output(ReviewState)

def call_reviewer(state:AgentState):
    """
    Reviewer determines WHAT needs to be corrected.
    Its job is to analyze why the draft was rejected and provide actionable feedback.
    """
    try:
        # email_summary=state.contents_identified.summary
        email_drafted=state.draft.draft_email
        feedback_received=state.human_approval.human_feedback
        # data_used=state.retreive_data.retreived_data

        review_prompt=ReviewPrompt()
        review_input=[review_prompt,email_drafted,feedback_received]
        response_at_llm=llm_at_reviewer.invoke(review_input)
        return {"review":response_at_llm}
    except Exception as e:
        print(f"error while identifying :{e}")
        raise





     