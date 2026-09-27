from src.state import AgentState
from src.helper_function import connect_to_weaviate
def data_retreiver_function(state:AgentState):
    """
    Retriever determines WHERE/HOW to obtain it.
    The Data Retriever decides how to obtain the information, 
    that is required to answer the email.
    """
    query_for_retreival=state.contents_identified.query_for_retreival
    client=connect_to_weaviate()
    print("*"*40+"Data retreival function initiated"+"*"*40)
    try:
        get_collection=client.collections.get("p3_data")
        response=get_collection.query.near_text(
            query=query_for_retreival,
            limit=1
            )
        if response.objects:
            retreived_content=response.objects[0].properties["content"]
        else:
            retreived_content=None
        return{
            "retreive_data":[retreived_content] if retreived_content else []
        }

    finally:
        client.close()