import mysql.connector
from mysql.connector import Error

# Connect to MySQL server
db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='expense_cal'
)

mycursor = db.cursor()

def create_users_table():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(50) NOT NULL
        )
    '''
    mycursor.execute(create_table_query)
    db.commit()

def register_user(username, password):
    try:
        insert_user_query = '''
            INSERT INTO users (username, password)
            VALUES (%s, %s)
        '''
        mycursor.execute(insert_user_query, (username, password))
        db.commit()
        print('User registered successfully.')
    except Error as e:
        print(f"Error registering user: {e}")

def login_user(username, password):
    login_query = '''
        SELECT id FROM users WHERE username = %s AND password = %s
    '''
    mycursor.execute(login_query, (username, password))
    result = mycursor.fetchone()
    if result:
        return result[0]
    return None

def create_expenses_table():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            expensetype VARCHAR(50) NOT NULL,
            amount FLOAT NOT NULL,
            UNIQUE KEY unique_expense (user_id, expensetype),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    '''
    mycursor.execute(create_table_query)
    db.commit()

def insert_expense(user_id, expensetype, amount):
    insert_expense_query = '''
        INSERT INTO expenses (user_id, expensetype, amount)
        VALUES (%s, %s, %s)
    '''
    mycursor.execute(insert_expense_query, (user_id, expensetype, amount))
    db.commit()

def update_expense(expensetype, amount):
    update_expense_query = '''
        UPDATE expenses 
        SET amount = %s
        WHERE expensetype = %s
    '''
    mycursor.execute(update_expense_query, (amount, expensetype))
    db.commit()

def delete_expense_particular(expensetype):
    delete_expense_query = '''
        DELETE FROM expenses WHERE expensetype = %s
    '''
    mycursor.execute(delete_expense_query, (expensetype,))
    db.commit()

def delete_all_expense():
    delete_all_expense_query = '''
        DELETE FROM expenses
    '''
    mycursor.execute(delete_all_expense_query)
    db.commit()

def close_connection():
    db.close()
