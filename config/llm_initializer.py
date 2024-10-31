"""
Initializes the ChatOpenAI model for use in LangChain.
Returns an instance of the ChatOpenAI model with GPT-4.
"""

from langchain_openai import ChatOpenAI

def initialize_llm():
    # Note: Ensure the key is stored securely and not hard-coded in production environments
    api_key = open("open_api_key.txt").read().strip()
    
    return ChatOpenAI(model="gpt-4", api_key=api_key)
