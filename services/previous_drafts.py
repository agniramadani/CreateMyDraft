"""
This module displays previous clinical trial document drafts,
allowing users to select and view details for LayCTD or ICF drafts.
"""

import streamlit as st
from config.database import get_layctd_drafts, get_icf_drafts

def render_previous_drafts():
    doc_type = st.sidebar.selectbox("Select Document Type", ["LayCTD", "ICF"])
    st.title(f"Previous Drafts for {doc_type}")

    if doc_type == "LayCTD":
        drafts = get_layctd_drafts()
        
        for draft in drafts:
            st.write(f"**Tone:** {draft[1]}")
            st.write(f"**Purpose:** {draft[2]}")
            st.write(f"**Demographics:** {draft[3]}")
            st.write(f"**Outcomes:** {draft[4]}")
            st.write(f"**Content:**\n{draft[5]}")
            # Separate display of date (YYYY-MM-DD) and time (HH:MM:SS)
            date_str, time_str = draft[6].split()
            time_str = time_str[:5]
            st.write(f"**Date Created:** {date_str} **Time:** {time_str}")
            st.markdown("---")

    else:
        drafts = get_icf_drafts()
        
        for draft in drafts:
            st.write(f"**Tone:** {draft[1]}")
            st.write(f"**Participant Information:** {draft[2]}")
            st.write(f"**Risks:** {draft[3]}")
            st.write(f"**Benefits:** {draft[4]}")
            st.write(f"**Duration:** {draft[5]}")
            st.write(f"**Content:**\n{draft[6]}")
            # Separate display of date (YYYY-MM-DD) and time (HH:MM:SS)
            date_str, time_str = draft[7].split()
            time_str = time_str[:5]
            st.write(f"**Date Created:** {date_str} **Time:** {time_str}")
            st.markdown("---")
