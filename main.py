from src.state import AgentState
from src.nodes import email_identifier_node, academic_drafter_node, programme_drafter_node, human_approval_node, reveiwer_node


from langgraph.graph import StateGraph, START, END
graph=StateGraph(state_schema=AgentState)

graph.add_node("identifier",email_identifier_node)
graph.add_node("academic_drafter",academic_drafter_node)
graph.add_node("pragramme_drafter",programme_drafter_node)
graph.add_node("approver",human_approval_node)
graph.add_node("reviewer",reveiwer_node)

graph.add_edge(START, "identifier")
# add conditional edge from identifier to academic and programme
graph.add_edge("academic_drafter","approver")
graph.add_edge("approver",)
