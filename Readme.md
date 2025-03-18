# Expense Tracker App

## Description
The Expense Tracker is a simple application built using Streamlit and SQL Server. It allows users to track their expenses, categorize them by family members, amount, and date. The app provides functionalities to add family members, record expenses, and view them with filters for family members and months.

## Purpose
The purpose of this project is to provide a user-friendly interface for families to track and manage their expenses. It aims to simplify expense recording by associating each expense with a family member and providing easy-to-use features for managing data.

## Value
This app helps families gain better control over their finances by tracking all the expenditures. Users can filter expenses based on family members and months, enabling them to understand where their money is being spent and make informed financial decisions.

## Technologies Used
- **Streamlit**: A Python library used for creating web applications for data science and machine learning.
- **Python**: The main programming language used for backend logic.
- **SQL Server**: Used for storing family member and expense data.
- **pyodbc**: A Python package for connecting to SQL Server databases.
- **pandas**: For displaying and manipulating data in tables.

## Setup Instructions

### Prerequisites

1. Python 3.x installed on your machine.
2. SQL Server running locally or remotely.
3. Required Python libraries installed. You can install them by running:
    ```bash
    pip install -r requirements.txt
    ```

### SQL Table Setup

To set up the database, execute the following SQL queries to create the necessary tables:

```sql
CREATE TABLE FamilyMembers (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Expenses (
    id INT PRIMARY KEY IDENTITY(1,1),
    family_member_id INT,
    date DATE,
    amount DECIMAL(18,2),
    category VARCHAR(50),
    description TEXT,
    FOREIGN KEY (family_member_id) REFERENCES FamilyMembers(id)
);
```
## Usage
Running the Application
After setting up the SQL tables, you can run the app by executing the following command in the project directory:

streamlit run app.py
The app will open in your default web browser, and you will be able to:

- Add family members
- Add expenses for each family member
- View and filter expenses based on family member or month
- Update and delete expenses

## Adding Family Members and Expenses
- Use the Add Family Member form to enter the names of family members.
- Use the Add Expense form to enter expenses, choosing a family member, date, amount, category, and description.
- View and filter expenses based on family member and month. You can also update or delete any existing expense by providing its ID.

## Contributing
1. Fork the repository to your own GitHub account.
2. Create a new branch for your changes (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add feature').
4. Push your branch (git push origin feature-branch).
5. Open a pull request on the original repository.