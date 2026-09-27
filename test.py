from src.state import AgentState,IdentifierState,InputEmail,DataRetreivalState

from src.nodes.academic_drafter_node import academic_email_drafter

test_state=AgentState(
    input=InputEmail(    
        email_body="I want to apply for Applied Data Science offered by ANS institute. Kindly let me know the opening date to apply?",
        email_sender="sender@gmail.com",
        email_recipients=["recipient@gmail.com"],
        email_sub="opening date to apply for Applied Data Science course"),
    contents_identified=IdentifierState(
        category="ACADEMICS",
        summary= "what is the opening date to apply for the Applied Data Science program",
        data_retreival_required=True,
        query_for_retreival= "Starting date to apply Applied Data Science program"
    ),
    retreive_data=DataRetreivalState(
        retreived_data=['converting foundational theoretical knowledge into industry-ready data science expertise.\nCourse Duration: 1 Year (Full-time, Residential)\nCourse Fee: ₹  3,000,000 (3 Lakhs) + GST\nApplication Start Date: 20 January 2027']
    )
)

result=academic_email_drafter(test_state)
print(result["draft"])