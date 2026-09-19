from src.state import AgentState
from src.prompts import IdentifierPrompt
from src.model import LlmCall
from src.helper_function import json_content_extractor
import json

def analyse_identify_function(state:AgentState):
    """
        Identifier determines WHAT information is needed.
        What category is this email?
        What is the email about?
        What information is needed to answer it?
        Is external/internal data actually required?
    """
    try:
        email=state.input.email_body
        indentifier_prompt=IdentifierPrompt()
        identifier_llm_input=[indentifier_prompt,email]
        response_at_identifier=LlmCall.invoke(identifier_llm_input)
        extracted_content=json_content_extractor(response_at_identifier)
        identifier_output=json.loads(extracted_content)
        return {"summary":identifier_output["summary_generated"],
                "category":identifier_output["category"],
                "data_retreival_required":identifier_output["data_retreival_required"],
                "query_for_retreival":identifier_output["query_for_retreival"]
                }
    except Exception as e:
        print(f"error while identifying :{e}")
        raise

