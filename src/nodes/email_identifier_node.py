from src.state import AgentState
from src.prompts import IdentifierPrompt
from src.model import llm_at_identifier
from src.helper_function import json_content_extractor
import json

def classify_and_summarise(state:AgentState):
    try:
        email=state.input.email_body
        classify_summarise_prompt=IdentifierPrompt()
        identifier_llm_input=[classify_summarise_prompt,email]
        response_at_identifier=llm_at_identifier.invoke(identifier_llm_input)
        extracted_content=json_content_extractor(response_at_identifier)
        identifier_output=json.loads(extracted_content)
        return {"summary":identifier_output["summary_generated"],"category":identifier_output["category"]}
    except Exception as e:
        print(f"error while identifying :{e}")
        raise

