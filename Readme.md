# Expense Tracker App

This is an Expense Tracker application built using **Streamlit** and **SQL Server**. The app allows users to add family members and track their expenses. It supports features such as filtering by family member, month, and sorting by amount, along with the ability to update and delete expenses.

## Features

- **Add Family Members:** Users can add family members to the database.
- **Add Expenses:** Users can add expenses linked to family members, specifying details such as date, category, amount, and description.
- **View Expenses:** Users can view all expenses, with options to filter by family member or month.
- **Update Expenses:** Users can update the amount, category, description, or date for existing expenses.
- **Delete Expenses:** Users can delete any expense from the system.
- **Sorting:** Expenses can be sorted in ascending or descending order by amount.

## Technologies Used

- **Streamlit:** For the frontend UI.
- **SQL Server:** For database management and storing expenses and family member data.
- **pyodbc:** For connecting to the SQL Server database from Python.
  
## Prerequisites

Before running the application, make sure you have the following installed:

1. Python (3.x)
2. Streamlit (`pip install streamlit`)
3. pyodbc (`pip install pyodbc`)
4. SQL Server

You will also need an **SQL Server** instance running with the appropriate tables set up. Below are the SQL queries to create the necessary tables.

### SQL Table Setup

#### FamilyMembers Table
```sql
CREATE TABLE FamilyMembers (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100) NOT NULL
);

Expenses Table

CREATE TABLE Expenses (
    id INT PRIMARY KEY IDENTITY(1,1),
    family_member_id INT,
    date DATE,
    amount DECIMAL(10, 2),
    category VARCHAR(50),
    description VARCHAR(255),
    FOREIGN KEY (family_member_id) REFERENCES FamilyMembers(id)
);

Setup
Clone the repository:


git clone https://github.com/your-username/ExpenseTrackerApp.git
cd ExpenseTrackerApp
Install required dependencies:

Install Streamlit and pyodbc using pip:


pip install streamlit pyodbc
Configure the database connection:

Update the database connection string in the db_connection.py file to reflect your local SQL Server setup.


connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ExpenseTracker;Trusted_Connection=yes;"
Run the application:

After setting up your database and installing dependencies, run the app using Streamlit:


streamlit run app.py
Access the App:

The app will open in your default browser. You can now add family members, add expenses, and view/manage them through the app.

Usage
Add Family Member: Use the "Add Family Member" form to enter the name of a family member.
Add Expense: After adding family members, you can add expenses by selecting the family member, specifying the amount, category, date, and description.
View Expenses: You can view all expenses, filter by family member and/or month, and sort them.
Update Expense: Click the ID of an expense to edit its details.
Delete Expense: Click the ID of an expense to delete it from the system.