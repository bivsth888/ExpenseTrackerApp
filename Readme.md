# Expense Tracker App

This project is an Expense Tracker application built with Streamlit, SQL Server, and Python.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [SQL Table Setup](#sql-table-setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview
The Expense Tracker allows users to track their expenses and categorize them by family member, amount, and date. It supports adding, updating, and deleting expenses, as well as filtering by family member and month.



## Features
- Add Family Member
- Add Expense
- View and Filter Expenses by Family Member/Month
- Update and Delete Expenses

## Installation

### Prerequisites

Before running the application, make sure you have the following installed:
- Python 3.x
- SQL Server

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project folder:
    ```bash
    cd your-repository
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your SQL Server database (see **SQL Table Setup**).

## SQL Table Setup

Run the following SQL queries to create the necessary tables in your SQL Server database:

```sql
CREATE TABLE FamilyMembers (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Expenses (
    id INT PRIMARY KEY IDENTITY(1,1),
    family_member_id INT,
    date DATE,
    amount DECIMAL(18,2)
```
## Usage

After setting up your SQL tables, follow these steps to run the app:

## Running the Application

To start the application, run the following command in the project directory:

streamlit run app.py
This will open the app in your browser, where you can add family members, expenses, and view them.

## SQL Table Setup
Make sure that you have created the FamilyMembers and Expenses tables as shown in the SQL Table Setup section. These tables are crucial for the proper functioning of the app.

## Adding Family Members
Once the app is running, use the interface to add family members. The add_family_member() function in family_member.py handles this.

## Adding Expenses
You can add expenses associated with family members by selecting them from a dropdown and entering the amount, category, date, and description.

## Viewing Expenses
The app allows you to view all expenses, filtered by family member and month. You can also update or delete expenses.

## Updating and Deleting Expenses
To update or delete an expense:

## Enter the Expense ID
Update the necessary fields or delete the expense