"""
We use this script to set up and manage SQLite storage for clinical trial drafts (LayCTD and ICF).
Defines schema and functions to insert drafts with key attributes in separate tables.
"""

import sqlite3
from datetime import datetime

# Connect to the SQLite database (or create it if it doesn’t exist)
def get_connection():
    conn = sqlite3.connect("drafts.db")
    return conn

# Function to set up the database with separate tables for LayCTD and ICF documents
def setup_database():
    conn = get_connection()
    with conn:
        # Create LayCTD drafts table
        conn.execute('''CREATE TABLE IF NOT EXISTS layctd_drafts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tone TEXT,
            purpose TEXT,
            demographics TEXT,
            outcomes TEXT,
            content TEXT,
            created_at TIMESTAMP
        )''')

        # Create ICF drafts table
        conn.execute('''CREATE TABLE IF NOT EXISTS icf_drafts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tone TEXT,
            info TEXT,
            risks TEXT,
            benefits TEXT,
            duration TEXT,
            content TEXT,
            created_at TIMESTAMP
        )''')

# Save a LayCTD draft to the database
def save_layctd_draft(tone, purpose, demographics, outcomes, content):
    conn = get_connection()
    with conn:
        conn.execute(
            '''INSERT INTO layctd_drafts (tone, purpose, demographics, outcomes, content, created_at)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (tone, purpose, demographics, outcomes, content, datetime.now())
        )

# Save an ICF draft to the database
def save_icf_draft(tone, info, risks, benefits, duration, content):
    conn = get_connection()
    with conn:
        conn.execute(
            '''INSERT INTO icf_drafts (tone, info, risks, benefits, duration, content, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (tone, info, risks, benefits, duration, content, datetime.now())
        )
