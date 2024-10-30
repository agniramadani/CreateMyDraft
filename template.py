"""
This script generates draft documents for clinical trials, specifically Lay Summaries (LayCTD) 
and Informed Consent Forms (ICF). It uses templates with placeholders for trial-specific details.
"""

# Define a template specific for generating Lay Summaries (LayCTD) 
layctd_template = (
    "Generate a lay summary for a clinical trial. "
    "Purpose: {purpose}. Demographics: {demographics}. Expected outcomes: {outcomes}. "
    "Tone: {tone}."
)

# Define a template specific for generating Informed Consent Forms (ICF)
icf_template = (
    "Generate an informed consent form for a clinical trial. "
    "Information: {info}. Risks: {risks}. Benefits: {benefits}. Duration: {duration}. "
    "Tone: {tone}."
)
