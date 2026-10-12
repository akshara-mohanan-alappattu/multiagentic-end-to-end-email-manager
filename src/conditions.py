# condition No.1 : at identifier, the graph goes to the data retreiver 
# if data is required to be retreived, other wise goes to general drafter

from src.state import AgentState
def condition_at_identifier(state:AgentState):
    try:
        data_retreival_required=state.contents_identified.data_retreival_required
       
        if data_retreival_required==True:
            return "route_to_data_retreiver"
        else:
            return "route_to_general_drafter"
    except Exception as e:
        print(f"error while routing :{e}")
        raise

# condition No.2 : condition at data retreiver, 
# the graph goes academic drafter if category is "academic" and
#  programme drafter if category is "programme"

def condition_at_data_retreiver(state:AgentState):
    try:
        category=state.contents_identified.category
        if category=="ACADEMICS":
            return "route_to_academic_drafter"
        elif category=="PROGRAMME":
            return "route_to_programme_drafter"
        else:
            return "undefined"
    except Exception as e:
        print(f"error while routing :{e}")
        raise

# condition No.3 : condition at human approval, 
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

# condition No.4 : condition at reviewer, the reviewer direct the email with recommendations to corresponding node
def condition_at_reviewer(state:AgentState):
    try:
        category=state.contents_identified.category
        rejection_type=state.review.rejection_type
        if rejection_type=="DATA_ISSUE":
            return "back_to_retreiver"
        else:
            if category=="ACADEMICS":
                return "back_to_academic_drafter"
            else:
                return "back_to_programme_drafter"
    except Exception as e:
        print(f"error while routing :{e}")
        raise