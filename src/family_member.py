import streamlit as st
from db_connection import get_db_connection

def add_family_member(name):
    """Add a new family member to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FamilyMembers (Name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_family_members():
    """Retrieve all family members from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FamilyMembers")
    members = cursor.fetchall()
    conn.close()
    return members

# Dummy function for GitHub activity
def generate_member_names():
    """Dummy function to generate random member names for testing."""
    names = ["Alex", "Jamie", "Taylor"]
    for name in names:
        print(f"Generated dummy name: {name}")
