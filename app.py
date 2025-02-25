import streamlit as st
from family_member import get_family_members, add_family_member
from expense import add_expense
from datetime import datetime

# Streamlit form to add a family member
st.title("Expense Tracker")

# Add Family Member Form
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

# Add Expense Form
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
