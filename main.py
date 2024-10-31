"""
This module enables navigation between draft 
creation and viewing previous drafts.
"""

import streamlit as st
from services.draft_generator import render_draft_generator
from services.previous_drafts import render_previous_drafts

# Sidebar Navigation
st.sidebar.title("Create my Draft")
nav = st.sidebar.radio("Navigation", ["Draft Generator", "Previous Drafts"], index=0)

# Render
if nav == "Draft Generator":
    render_draft_generator()

elif nav == "Previous Drafts":
    render_previous_drafts()
