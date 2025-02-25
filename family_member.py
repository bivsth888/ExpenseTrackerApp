from db_connection import get_db_connection

# Function to fetch all family members
def get_family_members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM FamilyMembers")
    family_members = cursor.fetchall()
    conn.close()
    return [(member[0], member[1]) for member in family_members]

# Function to add a new family member
def add_family_member(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FamilyMembers (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
