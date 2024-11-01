"""
This module provides functionality to generate and saves clinical trial drafts 
for LayCTD and ICF documents using user inputs and our language model.
"""

import streamlit as st
from config.database import save_layctd_draft, save_icf_draft
from services.generate import generate_draft
from config.llm_initializer import initialize_llm
from services.templates import layctd_template, icf_template

llm = initialize_llm()

def render_draft_generator():
    doc_type = st.sidebar.selectbox("Select Document Type", ["LayCTD", "ICF"])

    # Sidebar dropdown for selecting tone/complexity
    tone = st.sidebar.selectbox(
        "Select Tone/Complexity",
        ["Simplified Language", "Technical Details", "Detailed Explanations"]
    )

    st.title("Clinical Trial Document")

    # Document-specific input fields
    if doc_type == "LayCTD":
        # Input fields specific to LayCTD documents
        purpose = st.text_input("Purpose", value="", help="Briefly describe the main purpose of the trial.", label_visibility="visible")
        demographics = st.text_input("Demographics", value="", help="Describe the participant demographics (age, condition, etc.).", label_visibility="visible")
        outcomes = st.text_input("Outcomes", value="", help="What are the expected outcomes for this trial?", label_visibility="visible")

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
        info = st.text_input("Information", value="", help="General information about the participant eligibility and criteria.", label_visibility="visible")
        risks = st.text_input("Risks", value="", help="Outline any known or potential risks associated with the study.", label_visibility="visible")
        benefits = st.text_input("Benefits", value="", help="What benefits might participants experience?", label_visibility="visible")
        duration = st.text_input("Duration", value="", help="State the total duration of the study (e.g., 6 months).", label_visibility="visible")
        
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
