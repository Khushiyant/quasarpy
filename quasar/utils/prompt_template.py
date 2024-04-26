PROMPT_TEMPLATE = """
Suggest the changes to code below while following best industrial coding practices to solve the following detected code smells in the code.
Code Smells given in json format where 0 denotes absense and 1 denotes presence of that particular code smell:
{code_smell}
Code:
{code}

Additional details in json format:
{additional_details}
"""

"\nSuggest the changes to code below while following best industrial coding practices to solve the following detected code smells in the code.\nCode Smells given in json format where 0 denotes absense and 1 denotes presence of that particular code smell:\n{'long_class': 1, 'long_method': 0}\nCode:\n__version__ = '0.1.0'\n\nAdditional details in json format:\n{'loc': 1, 'lloc': 1, 'sloc': 1, 'comments': 0, 'multi': 0, 'blank': 0, 'single_comments': 0, 'h1': 0, 'h2': 0, 'N1': 0, 'N2': 0, 'vocabulary': 0, 'length': 0, 'calculated_length': 0, 'volume': 0, 'difficulty': 0, 'effort': 0, 'time': 0.0, 'bugs': 0.0, 'long_class': 1, 'long_method': 0, 'solution': None}\n"