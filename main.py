import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Template for generating a lay summary (LayCTD) for clinical trials
# This template will be filled with specific trial information for generating draft summaries.
layctd_template = (
    "Generate a lay summary for a clinical trial. "
    "Purpose: {purpose}. Demographics: {demographics}. Expected outcomes: {outcomes}."
)

# Initialize the ChatOpenAI model (GPT-4) for use in LangChain
# Note: Ensure that the API key is stored securely and not hard-coded in production environments
# You can add your api key inside ChatOpenAI: api_key="your_key"
llm = ChatOpenAI(model="gpt-4")

# Sidebar for document type selection - offers user a choice of document type
st.sidebar.title("Create my Draft")
doc_type = st.sidebar.selectbox("Select Document Type", ["LayCTD", "ICF"])

# Main title for the app's interface
st.title("Clinical Trial Document Draft Generator")

# Document-specific input fields
if doc_type == "LayCTD":
    # Input fields specific to LayCTD documents
    purpose = st.text_input("Trial Purpose", help="Briefly describe the main purpose of the trial.")
    demographics = st.text_input("Patient Demographics", help="Describe the participant demographics (age, condition, etc.).")
    outcomes = st.text_input("Expected Outcomes", help="What are the expected outcomes for this trial?")

    # Button to trigger generation of the LayCTD draft
    if st.button("Generate LayCTD Draft"):
        # Use PromptTemplate to insert user-provided values into the lay summary template
        layctd_prompt = PromptTemplate(
            input_variables=["purpose", "demographics", "outcomes"],
            template=layctd_template
        )
        # Format the template with user inputs to create the final prompt
        prompt = layctd_prompt.format(purpose=purpose, demographics=demographics, outcomes=outcomes)
        
        # Call the language model to generate the draft based on the prompt
        draft = llm.invoke(prompt)
        
        # Display the generated draft on the Streamlit interface
        st.write(draft.content)

elif doc_type == "ICF":
    # Define a template specific for generating Informed Consent Forms (ICF)
    icf_template = (
        "Generate an informed consent form for a clinical trial. "
        "Information: {info}. Risks: {risks}. Benefits: {benefits}. Duration: {duration}."
    )
    
    # Input fields specific to ICF documents
    info = st.text_input("Participant Information", help="General information about the participant eligibility and criteria.")
    risks = st.text_input("Study Risks", help="Outline any known or potential risks associated with the study.")
    benefits = st.text_input("Study Benefits", help="What benefits might participants experience?")
    duration = st.text_input("Study Duration", help="State the total duration of the study (e.g., 6 months).")

    # Button to trigger generation of the ICF draft
    if st.button("Generate ICF Draft"):
        # Use PromptTemplate to insert user-provided values into the ICF template
        icf_prompt = PromptTemplate(
            input_variables=["info", "risks", "benefits", "duration"],
            template=icf_template
        )
        # Format the template with user inputs to create the final prompt
        prompt = icf_prompt.format(info=info, risks=risks, benefits=benefits, duration=duration)
        
        # Call the language model to generate the draft based on the prompt
        draft = llm.invoke(prompt)
        
        # Display the generated draft on the Streamlit interface
        st.write(draft.content)
