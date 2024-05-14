PROMPT_TEMPLATE = """
Suggest the changes to code below while following best industrial coding practices to solve the following detected code smells in the code.
Code Smells given in json format where 0 denotes absense and 1 denotes presence of that particular code smell:
{code_smell}
Code:
{code}

Additional details in json format:
{additional_details}
"""
