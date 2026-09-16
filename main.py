from src.state import AgentState
from src.nodes.email_identifier_node import analyse_identify_function
from src.nodes.data_retreiver_node import data_retreiver_function
from src.nodes.academic_drafter_node import academic_email_drafter
from src.nodes.programme_drafter_node import programme_email_drafter
from src.nodes.human_approval_node import call_human_approval
from src.nodes.reveiwer_node import call_reviewer
from src.nodes.send_email_node import send_email_function
from src.conditions import condition_at_approval,condition_at_identifier,condition_at_reviewer,condition_at_data_retreiver

from langgraph.graph import StateGraph, START, END
graph=StateGraph(state_schema=AgentState)

graph.add_node("identifier",analyse_identify_function)
graph.add_node("data_retreiver",data_retreiver_function)
graph.add_node("academic_drafter",academic_email_drafter)
graph.add_node("programme_drafter",programme_email_drafter)
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
                            },
                            )

graph.add_edge("academic_drafter","approver")
graph.add_edge("programme_drafter","approver")
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
                                "back_to_retreiver":"reviewer"
                            },
                            )
