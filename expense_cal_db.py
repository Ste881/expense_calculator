import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='expense_cal'
)

mycursor = db.cursor()

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
    insert_data_query = '''
        INSERT INTO expenses (user_id, expensetype, amount)
        VALUES (%s, %s, %s)
    '''
    data = (user_id, expensetype, amount)
    mycursor.execute(insert_data_query, data)
    db.commit()
    print('Expense inserted')

# Close the connection
def close_connection():
    if db.is_connected():
        mycursor.close()
        db.close()
        print('Connection closed')

if __name__ == '__main__':
    create_expenses_table()

    user_id_1 = 1
    user_id_2 = 2

    # Sample expenses for user 1
    expenses_user_1 = [
        ('Food', 50.25),
        ('Utilities', 100.75)
    ]

    # Sample expenses for user 2
    expenses_user_2 = [
        ('Food', 30.50),
        ('Travel', 200.00)
    ]

    for expensetype, amount in expenses_user_1:
        insert_expense(user_id_1, expensetype, amount)

    for expensetype, amount in expenses_user_2:
        insert_expense(user_id_2, expensetype, amount)

    close_connection()