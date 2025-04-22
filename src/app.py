import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
from family_member import get_family_members, add_family_member
from expense import add_expense, get_expenses, update_expense, delete_expense
from decimal import Decimal

# ===============================
# PAGE TITLE AND NAVIGATION MENU
# ===============================
st.title("Expense Tracker")
tabs = st.sidebar.radio("Navigate", ["Add Data", "View Expenses", "Visualize Expenses"])

# ========================================
# TAB 1: ADD FAMILY MEMBER AND ADD EXPENSE
# ========================================
if tabs == "Add Data":
    st.header("Add Family Member")

    # ---- Form to Add Family Member ----
    with st.form(key='add_family_member_form'):
        family_member_name = st.text_input("Family Member Name")
        submit_button = st.form_submit_button(label='Add Family Member')
        if submit_button:
            if family_member_name:
                add_family_member(family_member_name)
                st.success(f"Family member '{family_member_name}' added successfully!")
            else:
                st.error("Please enter a valid name.")

    st.header("Add Expense")

    # ---- Form to Add Expense ----
    with st.form(key='add_expense_form'):
        family_members = get_family_members()
        family_member_options = [member[1] for member in family_members]
        family_member_name = st.selectbox("Select Family Member", family_member_options)

        # Get family member ID based on name selected
        family_member_id = [member[0] for member in family_members if member[1] == family_member_name][0]

        expense_date = st.date_input("Expense Date", value=datetime.today())
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        category = st.selectbox("Category", ["Food", "Transport", "Bills", "Other"])
        description = st.text_area("Description", "")
        submit_button = st.form_submit_button(label='Add Expense')

        # Save expense if valid
        if submit_button:
            if amount > 0:
                add_expense(family_member_id, expense_date, float(amount), category, description)
                st.success(f"Expense of {amount} for {category} added successfully for {family_member_name}!")
            else:
                st.error("Please enter a valid amount.")

# ===================================
# TAB 2: VIEW, SEARCH, EDIT EXPENSES
# ===================================
elif tabs == "View Expenses":
    st.header("View All Expenses")

    # ---- Filter Options ----
    st.subheader("Filter by Family Member or Month")
    family_members = get_family_members()
    family_member_options = [member[1] for member in family_members]
    selected_member = st.selectbox("Select Family Member", ["All"] + family_member_options)
    month_filter = st.selectbox("Filter by Month", ["All", "January", "February", "March", "April", "May", "June",
                                                    "July", "August", "September", "October", "November", "December"])

    expenses = get_expenses(filter_member=selected_member, filter_month=month_filter)

    # ---- Description Search Box ----
    st.subheader("Search by Description")
    search_text = st.text_input("Enter keyword to search in descriptions")

    # ---- Prepare Expense Data ----
    expense_data = []
    for expense in expenses:
        family_member_name = [member[1] for member in family_members if member[0] == expense[1]][0]
        expense_data.append([expense[0], family_member_name, expense[2], float(expense[3]), expense[4], expense[5]])

    # ---- Filter based on Description ----
    if search_text:
        expense_data = [exp for exp in expense_data if search_text.lower() in exp[5].lower()]

    if expense_data:
        # ---- Show Filtered Table ----
        expense_df = pd.DataFrame(expense_data, columns=["ID", "Family Member", "Date", "Amount", "Category", "Description"])
        st.dataframe(expense_df)

        # ---- Select Expense ID for Update/Delete ----
        st.subheader("Update or Delete Expense by ID")
        expense_ids = expense_df["ID"].tolist()
        selected_id = st.selectbox("Select Expense ID", expense_ids)
        expense = expense_df[expense_df["ID"] == selected_id].values[0]

        # ---- Update/Delete Form ----
        with st.form("update_delete_form"):
            updated_amount = st.number_input("Updated Amount", value=float(expense[3]), min_value=0.01, format="%.2f")

            # Ensure current category is in the list
            default_categories = ["Food", "Transport", "Bills", "Other"]
            if expense[4] not in default_categories:
                default_categories.append(expense[4])
            updated_category = st.selectbox("Updated Category", default_categories, index=default_categories.index(expense[4]))

            updated_description = st.text_area("Updated Description", value=expense[5])

            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("Update"):
                    update_expense(selected_id, float(updated_amount), updated_category, updated_description)
                    st.success("Expense updated successfully.")
            with col2:
                if st.form_submit_button("Delete"):
                    delete_expense(selected_id)
                    st.success("Expense deleted successfully.")
    else:
        st.info("No expenses found for the selected filter.")

# ========================================
# TAB 3: VISUALIZATION - PIE CHART REPORTS
# ========================================
elif tabs == "Visualize Expenses":
    st.header("Visualize Expenses")

    # ---- View Mode: All or By Month ----
    view_mode = st.selectbox("Select View Mode", ["All Time", "By Month"])

    if view_mode == "By Month":
        filter_month = st.selectbox("Select Month", [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        month_num = datetime.strptime(filter_month, "%B").month
        expenses = get_expenses(filter_month=filter_month)
    else:
        expenses = get_expenses()

    if not expenses:
        st.warning("No data found for the selected view.")
        st.stop()

    # ---- Clean Data for Plotting ----
    cleaned_expenses = []
    for exp in expenses:
        cleaned_expenses.append([
            exp[0],  # ID
            exp[1],  # Family Member ID
            exp[2].strftime("%Y-%m-%d") if isinstance(exp[2], date) else exp[2],  # Date
            float(exp[3]) if isinstance(exp[3], Decimal) else exp[3],  # Amount
            exp[4],  # Category
            exp[5],  # Description
        ])

    df = pd.DataFrame(cleaned_expenses, columns=["ID", "Family Member ID", "Date", "Amount", "Category", "Description"])

    # ---- Add Family Member Names ----
    family_members = get_family_members()
    member_dict = {member[0]: member[1] for member in family_members}
    df["Family Member"] = df["Family Member ID"].map(member_dict)

    # ---- Pie Chart by Category ----
    st.subheader("Expenses by Category")
    category_summary = df.groupby("Category")["Amount"].sum()
    fig1, ax1 = plt.subplots()
    ax1.pie(category_summary, labels=category_summary.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    # ---- Pie Chart by Family Member ----
    st.subheader("Expenses by Family Member")
    member_summary = df.groupby("Family Member")["Amount"].sum()
    fig2, ax2 = plt.subplots()
    ax2.pie(member_summary, labels=member_summary.index, autopct="%1.1f%%", startangle=90)
    ax2.axis("equal")
    st.pyplot(fig2)
