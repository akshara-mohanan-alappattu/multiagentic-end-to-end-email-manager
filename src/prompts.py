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
        "data_retreival_required":<data_retreival_required>
        "query_for_retreival":<query_for_retreival>
    }
        ''') 
    return prompt

def AcademicPrompt():
    prompt=SystemMessage(content='''You are an intelligent email drafter. 
                             You have summary of an email and data required to answer the mail.
                             Draft a reply email to this mail keeping formal tone.''')
    return prompt

def GeneralPrompt():
    prompt=SystemMessage(content='''You are a professional email drafter.
                                    Draft a reply email to the input email based on its summary.  ''')
    return prompt

        