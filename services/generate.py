"""
Generates a draft document using a language model 
based on a predefined template and user inputs
"""

from langchain.prompts import PromptTemplate

# Function to generate a draft based on the provided template and inputs
def generate_draft(llm, template, inputs):
    # Use PromptTemplate to insert user-provided values into the template
    prompt_template = PromptTemplate(input_variables=list(inputs.keys()), template=template)
    # Format the template with user inputs to create the final prompt
    prompt = prompt_template.format(**inputs)
    # Call the language model to generate the draft based on the prompt
    draft = llm.invoke(prompt)
    return draft
