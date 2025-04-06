import pyodbc

# Set up the connection string
def get_db_connection():
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ExpenseTracker;Trusted_Connection=yes;"
    return pyodbc.connect(connection_string)

# Dummy function for GitHub activity
def test_connection():
    """function to test database connection."""
    print("Pretend testing DB connection...")

