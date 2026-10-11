from src.state import AgentState,ApprovalState
from langgraph.types import interrupt
def call_human_approval(state: AgentState):
    draft=state.draft.draft_email
    human_decision=interrupt({
        "question":"Approve or Reject the draft given below:",
        "draft":draft,
        "instructions":("enter decision as 'approved' or 'rejected',"
                        "along with any feedback.")
    })

    decision=human_decision["decision"].strip().lower()
    feedback=human_decision.get("feedback")

    if decision=="approved":
        return{
            "human_approval":ApprovalState(
                approval_status="Approved",
                human_feedback=feedback,
                review_required=False
            ) 
        }
    elif decision=="rejected":
        return{
            "human_approval":ApprovalState(
                approval_status="Rejected",
                human_feedback=feedback,
                review_required=True
            )
        }
    else:
        raise ValueError(
            "Invalid decision, Enter approved or rejected."
        )