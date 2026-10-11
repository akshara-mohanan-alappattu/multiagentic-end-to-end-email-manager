from src.state import AgentState,InputEmail
from src.nodes.email_identifier_node import analyse_identify_function
from src.nodes.data_retreiver_node import data_retreiver_function
from src.nodes.academic_drafter_node import academic_email_drafter
from src.nodes.programme_drafter_node import programme_email_drafter
from src.nodes.general_drafter import general_email_drafter
from src.nodes.human_approval_node import call_human_approval
from src.nodes.reveiwer_node import call_reviewer
from src.nodes.send_email_node import send_email_function
from src.conditions import condition_at_approval,condition_at_identifier,condition_at_reviewer,condition_at_data_retreiver

from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt,Command
from langgraph.checkpoint.memory import InMemorySaver
graph=StateGraph(state_schema=AgentState)

graph.add_node("identifier",analyse_identify_function)
graph.add_node("data_retreiver",data_retreiver_function)
graph.add_node("academic_drafter",academic_email_drafter)
graph.add_node("programme_drafter",programme_email_drafter)
graph.add_node("general_drafter",general_email_drafter )
graph.add_node("approver",call_human_approval)
graph.add_node("reviewer",call_reviewer)
graph.add_node("send_email",send_email_function)

graph.add_edge(START, "identifier")
graph.add_conditional_edges("identifier",condition_at_identifier,
                            {
                               "route_to_data_retreiver": "data_retreiver",
                               "route_to_general_drafter":"general_drafter",
                            },
                            )
graph.add_conditional_edges("data_retreiver", condition_at_data_retreiver,
                            {
                                "route_to_academic_drafter":"academic_drafter",
                                "route_to_programme_drafter":"programme_drafter",
                                "undefined":END
                            },
                            )

graph.add_edge("academic_drafter","approver")
graph.add_edge("programme_drafter","approver")
graph.add_edge("general_drafter","approver")
graph.add_conditional_edges("approver",condition_at_approval,
                            {
                               "proceed_to_send_email":"send_email",
                               "proceed_to_reviewer":"reviewer",
                            },
                            )

graph.add_edge("send_email",END)
graph.add_conditional_edges("reviewer",condition_at_reviewer,
                            {
                                "back_to_academic_drafter":"academic_drafter",
                                "back_to_programme_drafter":"programme_drafter",
                                "back_to_retreiver":"data_retreiver"
                            },
                            )

checkpointer=InMemorySaver()

app=graph.compile(checkpointer=checkpointer)

config={
    "configuarable":{
        "thread_id":"email_001"
    }
}

test_state=AgentState(
    input=InputEmail(    
        email_body="I want to apply for Applied Data Science offered by ANS institute. Kindly let me know the opening date to apply?",
        email_sender="sender@gmail.com",
        email_recipients=["recipient@gmail.com"],
        email_sub="opening date to apply for Applied Data Science course"))

result=app.invoke(test_state,config=config)

while "__interrupt__" in result:
    interrupt_info=result["__interrupt__"][0]
    interrupt_data=interrupt_info.value
    print("-"*80)
    print("Human Approval Required")
    print("-"*80)
    print("\nPlease check the following draft email:")
    print(interrupt_data["draft"])
    print("\n=====================================================================")
    print(interrupt_data["question"])
    print("\n=====================================================================")
    print(interrupt_data["instructions"])
    print("\n=====================================================================")
    while True:
        decision=input("\nEnter Your Decision Here: Approved or Rejected").strip().lower()
        if decision in ["approved","rejected"]:
            break
        else:
            print("Invalid Output")
    feedback=input("Suggest any feedback for improvement").strip()
    if feedback=="":
        feedback=None

    result=app.invoke(
        Command(
            resume={
                "decision":decision,
                "feedback":feedback
            }
        ),
        config=config
    )
print("\n======================================================================================")
print(result)

