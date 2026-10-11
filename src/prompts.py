from langchain_core.messages import SystemMessage
def IdentifierPrompt():
    prompt=SystemMessage(content='''You are assigned 4 tasks:
    1. Categorise the email into 2 categories strictly based on the content.
        (1)Academic: This category includes everything related to the 2 courses provided by the ANS institution.The courses are ADS [Applied Data Science] and PNB[Professional Networking Branch] for graduates.
        (2)Programmes: This category includes everything retaled to the training programmes offered by ANS institution for bank employees.
    2. Generate a summary of the email input. 
        (1)Summary should contain the crux of the email.
        (2)Lenghth of Summary is maximum 50 words
    3. Check if this mail can be answered with your general knowledge or if any additional data required.
       (1)If data is required, answer "Yes". Return "No" otherwise. Only give binary response here.
    4. If additional data is required to answer email, then what is that data it requires. The title of data required has to be specified as query_for_retreival.
    The final output should be a dictionary with "category", "summary_generated", "data_retreival_required" and "query_for_retreival" as the keys.
    Do not retrieve any information yourself.
    
    Example
    {
        "category": <category>
        "summary_generated": <summary_generated>
        "data_retreival_required":<bool>
        "query_for_retreival":<query_for_retreival>
    }
        ''') 
    return prompt

def AcademicPrompt():
    prompt=SystemMessage(content='''You are an intelligent email drafter. 
                             You have summary of an email and data required to answer the mail. If available, use the feedback and recommendations.
                             Draft a reply email in to this mail keeping formal tone in maximum 50 words. 
                             Draft reply should be precise and direct information.
                             Do not add Opinions or commentary''')
    return prompt

def GeneralPrompt():
    prompt=SystemMessage(content='''You are a professional email drafter.
                                    Draft a reply email to the input email based on its summary.
                                    Draft a reply email in to this mail keeping formal tone in maximum 30 words. 
                                    Draft reply should be precise and direct information.
                                    Do not add Opinions or commentary  ''')
    return prompt


def ProgrammePrompt():
    prompt=SystemMessage(content='''You are an intelligent email drafter. 
                             You have summary of an email and data required to answer the mail. If available, use the feedback and recommendations.
                             Draft a reply email in to this mail keeping formal tone in maximum 50 words. 
                             Draft reply should be precise and direct information.
                             Do not add Opinions or commentary''')
    return prompt
def ReviewPrompt():
    prompt=SystemMessage(content='''Your taskes are:
    1. Analyse the email drafted based on the feedback received.Find the issue with the email. 
    2. What are recommendations for improving the drafted email.
    3. Identify the exact reason behind rejecting this email: 
        a. Data issue: Wrong data provided in the draft.
        b. Draft issue: Wrong structuring of draft.
    4. How many time the same mail got rejection.
    The final output should be a dictionary with "issues","recommendations","rejection_type","review_count"
    Example
    {"issues":<issues>,
    "recommendations":<recommendations>,
    "rejection_type":<rejection_type>,
    "review_count":<count>
    }
    ''')
    return prompt