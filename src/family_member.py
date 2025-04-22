import streamlit as st
from db_connection import get_db_connection  # Import function to establish DB connection

# ============================
# ADD A NEW FAMILY MEMBER
# ============================
def add_family_member(name):
    """
    Add a new family member to the database.

    Parameters:
    - name (str): The name of the family member to be added.
    """
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor()      # Create a cursor object to execute SQL
    cursor.execute(
        "INSERT INTO FamilyMembers (Name) VALUES (?)", (name,)
    )  # Add the family member to the FamilyMembers table
    conn.commit()               # Save changes to the database
    conn.close()                # Close the database connection

# ============================
# GET ALL FAMILY MEMBERS
# ============================
def get_family_members():
    """
    Retrieve all family members from the database.

    Returns:
    - List of tuples: Each tuple contains (ID, Name) of a family member.
    """
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor()      # Create a cursor object
    cursor.execute("SELECT * FROM FamilyMembers")  # Fetch all rows from FamilyMembers table
    members = cursor.fetchall()  # Store the results
    conn.close()                 # Close the connection
    return members               # Return list of members
