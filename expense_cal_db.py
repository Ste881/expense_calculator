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

    users = []

    while True:
        user_id = int(input("Enter the user ID (0 to stop): "))
        if user_id == 0:
            break
        user_name = input("Enter the user's name: ")
        users.append({'id': user_id, 'name': user_name})

    for user in users:
        print(f"Processing expenses for {user['name']}")
        while True:
            expensetype = input("Enter the expense type (press Enter to stop): ")
            if not expensetype:
                break
            amount = float(input("Enter the amount: "))
            insert_expense(user['id'], expensetype, amount)

    close_connection()
