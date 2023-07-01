import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='expense_cal'
)

mycursor = db.cursor()

# Drop the existing 'expenses' table (if it exists)
drop_table_query = '''
    DROP TABLE IF EXISTS expenses
'''
mycursor.execute(drop_table_query)
db.commit()

# Create a table to store all expenses
def create_expenses_table():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            expensetype VARCHAR(50) NOT NULL,
            amount FLOAT NOT NULL,
            UNIQUE KEY unique_expense (user_id, expensetype)
        )
    '''
    mycursor.execute(create_table_query)
    db.commit()
    print('Table expenses created')

# Insert data into the expenses table
def insert_expense(user_id, expensetype, amount):
    insert_expense_query = '''
        INSERT INTO expenses (user_id, expensetype, amount)
        VALUES (%s, %s, %s)
    '''
    data = (user_id, expensetype, amount)
    mycursor.execute(insert_expense_query, data)
    db.commit()
    print('Expense inserted successfully')

# Close the database connection
def close_connection():
    db.close()
    print('Database connection closed')