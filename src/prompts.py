from langchain_core.messages import SystemMessage
def IdentifierPrompt():
    prompt=SystemMessage(content='''You are assigned 2 tasks:
    1. Categorise the email into 2 categories strictly based on the content.
        (1)Academic: This category includes everything related to the 2 courses provided by the ANS institution.The courses are ADS [Applied Data Science] and PNB[Professional Networking Branch] for graduates.
        (2)Programmes: This category includes everything retaled to the training programmes offered by ANS institution for bank employees.
    2. Generate a summary of the email input. 
        (1)Summary should contain the crux of the email.
        (2)Lenghth of Summary is maximum 50 words
    The final output should be a dictionary with "category" and the "summary_generated" as the keys.
    
    Example
    {
        "category": <category>
        "summary_generated": <summary_generated>
    }
        ''') 
    return prompt