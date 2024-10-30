"""
Streamlit app for creating and saving clinical trial document drafts 
(LayCTD and ICF) with customizable details and tone.
"""

import streamlit as st
from database import save_layctd_draft, save_icf_draft
from template import layctd_template, icf_template
from generate import generate_draft
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI model (GPT-4) for use in LangChain
# Note: Ensure that the API key is stored securely and not hard-coded in production environments
# You can add your api key inside ChatOpenAI: api_key="your_key"
llm = ChatOpenAI(model="gpt-4")

# Sidebar for document type selection - offers user a choice of document type
st.sidebar.title("Create my Draft")
doc_type = st.sidebar.selectbox("Select Document Type", ["LayCTD", "ICF"])

# Sidebar dropdown for selecting tone/complexity
tone = st.sidebar.selectbox(
    "Select Tone/Complexity",
    ["Simplified Language", "Technical Details", "Detailed Explanations"]
)

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
        # Generate the LayCTD draft
        draft = generate_draft(
            llm, layctd_template, {"purpose": purpose, "demographics": demographics, "outcomes": outcomes, "tone": tone}
        )
        
        # Display the generated draft on the Streamlit interface
        st.write(draft.content)

        # Save LayCTD draft to the database
        save_layctd_draft(tone, purpose, demographics, outcomes, draft.content)

elif doc_type == "ICF":
    # Input fields specific to ICF documents
    info = st.text_input("Participant Information", help="General information about the participant eligibility and criteria.")
    risks = st.text_input("Study Risks", help="Outline any known or potential risks associated with the study.")
    benefits = st.text_input("Study Benefits", help="What benefits might participants experience?")
    duration = st.text_input("Study Duration", help="State the total duration of the study (e.g., 6 months).")

    # Button to trigger generation of the ICF draft
    if st.button("Generate ICF Draft"):
        # Generate the ICF draft
        draft = generate_draft(
            llm, icf_template, {"info": info, "risks": risks, "benefits": benefits, "duration": duration, "tone": tone}
        )
        
        # Display the generated draft on the Streamlit interface
        st.write(draft.content)

        # Save ICF draft to the database
        save_icf_draft(tone, info, risks, benefits, duration, draft.content)
