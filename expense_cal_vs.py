import sys
from expense_cal_db import (
    create_users_table, create_expenses_table,
    register_user, login_user, insert_expense, update_expense,
    delete_expense_particular, delete_all_expense, close_connection
)

default_menu = {1: 'Food', 2: 'Medication', 3: 'Entertainment', 4: 'Groceries', 5: 'Travel', 6: 'Clothing', 7: 'Makeup'}
n = len(default_menu)
expense = [0] * n

def existing_menu(user_id):
    while True:
        max_length = max(len(name) for name in default_menu.values())
        print("\nNo.   " + "Expense Type".ljust(max_length + 4) + "Amount")
        for i in default_menu:
            print(f"{i}.    {default_menu[i].ljust(max_length + 4)}{expense[i - 1]}")

        print("\nOptions:")
        print("t. Show total expenses")
        print("b. Back to main menu")

        expense_type = input("Enter the type of expense: ")

        if expense_type == 't':
            print(f"Total expense is: {sum(expense)}")
            return
        elif expense_type == 'b':
            return
        elif not expense_type.isdigit() or int(expense_type) > n:
            print("Invalid input. Try again.")
        else:
            expense_amount = float(input("Enter the amount: "))
            exp_report(user_id, int(expense_type), expense_amount)

def exp_report(user_id, exp_type, exp_amount):
    if expense[exp_type - 1] == 0:
        expense[exp_type - 1] += exp_amount
        insert_expense(user_id, default_menu[exp_type], exp_amount)
    else:
        expense[exp_type - 1] += exp_amount
        update_expense(user_id, default_menu[exp_type], expense[exp_type - 1])

def show_savings(total_income):
    total_expense = sum(expense)
    print(f"Total savings: {total_income - total_expense}")

def show_inflation_adjusted_savings(total_income, inflation_rate):
    total_expense = sum(expense)
    adjusted_savings = round((total_income - total_expense) / (1 + inflation_rate), 2)
    print(f"Inflation-adjusted savings: {adjusted_savings}")

if __name__ == '__main__':
    create_users_table()
    create_expenses_table()

    print("Welcome to Expense Calculator!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register_user(username, password)
        print("Registration successful. Please log in.")
        sys.exit()

    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_id = login_user(username, password)
        if not user_id:
            print("Invalid username or password.")
            sys.exit()
    else:
        print("Invalid choice.")
        sys.exit()

    while True:
        print("\nMain Menu:")
        print("a. Default menu")
        print("b. Add new category")
        print("c. Delete a category")
        print("d. Delete all expenses")
        print("e. Show savings")
        print("f. Show inflation-adjusted savings")
        print("g. Exit")

        option = input("Enter your choice: ")
        if option == 'a':
            existing_menu(user_id)
        elif option == 'b':
            new_category = input("Enter new category name: ")
            default_menu[n + 1] = new_category
            expense.append(0)
            n += 1
        elif option == 'c':
            print("\nChoose a category to delete:")
            for i in default_menu:
                print(f"{i}. {default_menu[i]}")
            category_to_delete = input("Enter the category number: ")
            if category_to_delete.isdigit() and int(category_to_delete) in default_menu:
                delete_expense_particular(user_id, default_menu[int(category_to_delete)])
                del default_menu[int(category_to_delete)]
            else:
                print("Invalid input.")
        elif option == 'd':
            delete_all_expense(user_id)
            default_menu.clear()
            print("All expenses deleted.")
        elif option == 'e':
            total_income = float(input("Enter your total income: "))
            show_savings(total_income)
        elif option == 'f':
            total_income = float(input("Enter your total income: "))
            inflation_rate = float(input("Enter the inflation rate (e.g., 0.03 for 3%): "))
            show_inflation_adjusted_savings(total_income, inflation_rate)
        elif option == 'g':
            close_connection()
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Try again.")
