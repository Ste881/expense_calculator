import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='expense_cal'
)

mycursor = db.cursor()

# Create a table
def create_table():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            expensetype VARCHAR(50) NOT NULL,
            amount FLOAT NOT NULL
        )
    '''
    mycursor.execute(create_table_query)
    db.commit()
    print('Table created')

# Insert data into the table
def insert_data():
    insert_data_query = '''
        INSERT INTO expenses (expensetype, amount)
        VALUES (%s, %s)
    '''
    data = [
        ('Groceries', 50.25),
        ('Utilities', 100.75)
    ]
    mycursor.executemany(insert_data_query, data)
    db.commit()
    print('Data inserted')

# Close the connection
def close_connection():
    if db.is_connected():
        mycursor.close()
        db.close()
        print('Connection closed')

if __name__ == '__main__':
    create_table()
    insert_data()
    close_connection()