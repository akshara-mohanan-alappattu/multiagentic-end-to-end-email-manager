from src.nodes.email_identifier_node import analyse_identify_function
# from src.prompts import IdentifierPrompt
# from src.model import llm_at_identifier
from langchain_groq import ChatGroq
from src.state import AgentState,InputEmail


test_state=AgentState(
    input=InputEmail(    
        email_body="I want to apply for Applied Data Science offered by ANS institute. Kindly let me know the last date to apply?",
        email_sender="sender@gmail.com",
        email_recipients=["recipient@gmail.com"],
        email_sub="last date to apply for Applied Data Science course")
)
result= analyse_identify_function(test_state)
print (result)

contents_identified=result["contents_identified"]
print("*"*20)
print("Category:", contents_identified.category)
print("Summary:", contents_identified.summary)
print("Data retreival required:", contents_identified.data_retreival_required)
print("Query for retreival:", contents_identified.query_for_retreival)