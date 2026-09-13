# condition No.1 : at identifier, the graph goes academic drafter if category is "academic" 
# and programme drafter if category is "programme"

from src.state import AgentState
def condition_at_identifier(state:AgentState):
    try:
        category=state.classify_and_summarise.category
        if category=="ACADEMICS":
            return "route_to_academic_drafter"
        elif category=="PROGRAMME":
            return "route_to_programme_drafter"
        else:
            return "undefined"
    except Exception as e:
        print("The category of email returned by identifier node is improper. Check at identifier node")
        print(f"error while routing :{e}")
        raise

# condition No.2 : condition at human approval, 
# if draft email is approved, graph ends there and if rejected,then goes to reviewer node.

def condition_at_approval(state:AgentState):
    try:
        approval_status=state.human_approval.approval_status
        if approval_status=="Approved":
            return "proceed_to_send_email"
        elif approval_status=="Rejected":
            return "proceed_to_reviewer"
        else:
            raise ValueError(f"unexpected approval status:{approval_status}")
    except Exception as e:
        print(f"error while routing :{e}")
        raise

# condition No.3 : condition at reviewer, the reviewer direct the email with recommendations to corresponding node
def condition_at_reviewer(state:AgentState):
    try:
        category=state.classify_and_summarise.category
        if category=="ACADEMICS":
            return "back_to_academic_drafter"
        else:
            return "back_to_programme_drafter"
    except Exception as e:
        print(f"error while routing :{e}")
        raise