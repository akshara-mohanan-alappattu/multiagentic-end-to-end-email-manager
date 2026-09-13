from src.state import AgentState
from src.nodes import email_identifier_node, academic_drafter_node, programme_drafter_node, human_approval_node, reveiwer_node,send_email_node
from src.conditions import condition_at_approval,condition_at_identifier,condition_at_reviewer

from langgraph.graph import StateGraph, START, END
graph=StateGraph(state_schema=AgentState)

graph.add_node("identifier",email_identifier_node)
graph.add_node("academic_drafter",academic_drafter_node)
graph.add_node("programme_drafter",programme_drafter_node)
graph.add_node("approver",human_approval_node)
graph.add_node("reviewer",reveiwer_node)
graph.add_node("send_email",send_email_node)

graph.add_edge(START, "identifier")
graph.add_conditional_edges("identifier", condition_at_identifier,
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
                            },
                            )
