from pydantic import BaseModel, Field
from typing import Literal

class InputEmail(BaseModel):
    email_body:str
    email_sender:str
    email_recipients:list[str]= Field(default_factory=list)
    email_sub:str

class IdentifierState(BaseModel):
    category:Literal["ACADEMICS","PROGRAMME","GENERAL"]| None= None
    summary:str| None= None
    data_retreival_required:bool= False
    query_for_retreival:str |None= None

class DataRetreivalState(BaseModel):
    retreived_data:list= Field(default_factory=list)

class DrafterState(BaseModel):
    draft:str| None= None
    draft_version:int= 1

class ApprovalState(BaseModel):
    approval_status:Literal["Pending","Approved","Rejected"]| None= None
    feedback:str| None= None

class ReviewState(BaseModel):
    review_required:bool= False
    issues:list[str]= Field(default_factory=list)
    recommendations:list[str]= Field(default_factory=list)
    rejection_type:Literal["DATA_ISSUE","DRAFT_ISSUE"] |None= None
    review_count:int= Field(
        ge=0,
        le=3,
        description="This is the number of times the human reject the draft email and reviewer reviews it for improvement"
        )

class ExecutionState(BaseModel):
    status:str="processing"
    retry_count:int=0
    sent:bool=False

class AgentState(BaseModel):
    # mailbox:str
    input:InputEmail
    contents_identified:IdentifierState |None = None
    retreive_data:DataRetreivalState |None= None
    draft:DrafterState | None= None
    human_approval:ApprovalState | None= None
    review:ReviewState | None= None
    execution:ExecutionState=Field(default_factory=ExecutionState)

    
    
