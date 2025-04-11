from db_connection import get_db_connection
from family_member import get_family_members  # Import get_family_members
from datetime import datetime

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
def get_expenses(filter_member="All", filter_month="All"):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT id, family_member_id, date, amount, category, description FROM Expenses"
    conditions = []
    params = []

    if filter_member != "All":
        conditions.append("family_member_id = ?")
        # You’ll need to convert name -> ID here; assuming you already handled that earlier
        from family_member import get_family_members
        member_id = [member[0] for member in get_family_members() if member[1] == filter_member][0]
        params.append(member_id)

    if filter_month != "All":
        month_num = datetime.strptime(filter_month, "%B").month
        conditions.append("MONTH(date) = ?")
        params.append(month_num)

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

# Dummy function for GitHub activity
def expense_analysis():
    """function for future expense trend analysis."""
    sample_expenses = [100, 200, 300]
    average = sum(sample_expenses) / len(sample_expenses)
    print(f"Average dummy expense: {average}")

