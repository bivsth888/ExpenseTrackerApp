from db_connection import get_db_connection

# Function to add an expense
def add_expense(family_member_id, expense_date, amount, category, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Expenses (family_member_id, date, amount, category, description)
        VALUES (?, ?, ?, ?, ?)
    """, (family_member_id, expense_date, amount, category, description))
    conn.commit()
    conn.close()
