import streamlit as st
import pandas as pd
from family_member import get_family_members
from expense import add_expense, get_expenses, update_expense, delete_expense
from datetime import datetime

# Streamlit form to add a family member
st.title("Expense Tracker")

# Tabs for different views
tabs = st.sidebar.radio("Select Tab", ["Add Family Member", "Add Expense", "View Expenses", "Update or Delete Expense"])

if tabs == "Add Family Member":
    st.header("Add Family Member")
    with st.form(key='add_family_member_form'):
        family_member_name = st.text_input("Family Member Name")
        submit_button = st.form_submit_button(label='Add Family Member')

        if submit_button:
            if family_member_name:
                add_family_member(family_member_name)
                st.success(f"Family member '{family_member_name}' added successfully!")
            else:
                st.error("Please enter a valid name.")

elif tabs == "Add Expense":
    st.header("Add Expense")
    with st.form(key='add_expense_form'):
        # Fetch family members from the database
        family_members = get_family_members()
        family_member_options = [member[1] for member in family_members]
        family_member_name = st.selectbox("Select Family Member", family_member_options)
        
        # Get family member ID based on the name selected
        family_member_id = [member[0] for member in family_members if member[1] == family_member_name][0]

        # Date input for the expense
        expense_date = st.date_input("Expense Date", value=datetime.today())
        
        # Amount input for the expense
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        
        # Category input for the expense
        category = st.selectbox("Category", ["Food", "Transport", "Bills", "Other"])
        
        # Description input for the expense
        description = st.text_area("Description", "")

        submit_button = st.form_submit_button(label='Add Expense')

        if submit_button:
            if amount > 0:
                add_expense(family_member_id, expense_date, amount, category, description)
                st.success(f"Expense of {amount} for {category} added successfully for {family_member_name}!")
            else:
                st.error("Please enter a valid amount.")

elif tabs == "View Expenses":
    st.header("View All Expenses")

    # Filters for expenses (optional)
    st.subheader("Filter by Family Member or Month")
    family_members = get_family_members()
    family_member_options = [member[1] for member in family_members]
    selected_member = st.selectbox("Select Family Member", ["All"] + family_member_options)

    month_filter = st.selectbox("Filter by Month", ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

    # Fetch expenses based on filters
    expenses = get_expenses(filter_member=selected_member, filter_month=month_filter)

    # Display expenses in a table
    st.subheader("Expenses")
    expense_data = []
    for expense in expenses:
        family_member_name = [member[1] for member in family_members if member[0] == expense[1]][0]
        expense_data.append([expense[0], family_member_name, expense[2], expense[3], expense[4], expense[5]])

    expense_df = pd.DataFrame(expense_data, columns=["ID", "Family Member", "Date", "Amount", "Category", "Description"])
    st.dataframe(expense_df)

elif tabs == "Update or Delete Expense":
    st.header("Update or Delete Expense")

    # Select the expense ID
    expense_id = st.number_input("Enter Expense ID to Update or Delete", min_value=1)

    # Fetch the expense details
    expense = get_expenses(exp_id=expense_id)

    if expense:  # Ensure there is data
        expense = expense[0]  # Get the first (and only) expense returned

        # Display the expense details for updating
        st.subheader(f"Expense ID: {expense[0]}")
        updated_amount = st.number_input("Updated Amount", value=float(expense[3]), min_value=0.01, format="%.2f")
        updated_category = st.selectbox("Updated Category", ["Food", "Transport", "Bills", "Other"], index=["Food", "Transport", "Bills", "Other"].index(expense[4]))
        updated_description = st.text_area("Updated Description", expense[5])

        # Update the expense if the submit button is pressed
        if st.button("Update Expense"):
            update_expense(expense_id, updated_amount, updated_category, updated_description)
            st.success(f"Expense ID {expense_id} updated successfully!")

        # Option to delete the expense
        if st.button("Delete Expense"):
            delete_expense(expense_id)
            st.success(f"Expense ID {expense_id} deleted successfully!")
    else:
        st.error("Expense ID not found. Please check the ID and try again.")
