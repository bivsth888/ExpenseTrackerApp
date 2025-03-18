from db_connection import get_db_connection
from family_member import get_family_members  # Import get_family_members

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

# Function to get expenses (with optional filters)
def get_expenses(filter_member=None, filter_month=None, exp_id=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM Expenses"
    conditions = []
    params = []

    if filter_member and filter_member != "All":
        family_members = get_family_members()
        conditions.append("family_member_id = ?")
        params.append([member[0] for member in family_members if member[1] == filter_member][0])

    if filter_month and filter_month != "All":
        month_map = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
            "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
        }
        conditions.append("MONTH(date) = ?")
        params.append(month_map[filter_month])

    if exp_id:
        conditions.append("id = ?")
        params.append(exp_id)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, params)
    expenses = cursor.fetchall()
    conn.close()
    return expenses

# Function to delete an expense
def delete_expense(exp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Expenses WHERE id = ?", (exp_id,))
    conn.commit()
    conn.close()

# Function to update an expense
def update_expense(exp_id, amount, category, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
    """, (amount, category, description, exp_id))
    conn.commit()
    conn.close()
