import sys
from expense_cal_db import create_expenses_table, delete_expense_particular, delete_all_expense, insert_expense, update_expense, close_connection

# Define existing_menu, default_menu, and expense as provided

def existing_menu():
    while True:
        x = 0
        for i in default_menu:
            if len(default_menu[i]) > x:
                x = len(default_menu[i])
        print("No.   " + "Expense Type".ljust(x + 4, ' ') + "Amount")
        for i in default_menu:
            print(str(i) + ".    " + default_menu[i].ljust(x + 4, ' ') + str(expense[i - 1]))

        print("press 't' for total")
        print("press 'b' to go back")

        expense_type = input("Enter the type of expense: ")

        if expense_type == 't':
            el = len(expense)
            total = 0
            for i in range(el):
                total = total + expense[i]
            print(f"Total expense is: {total}")
            return

        if expense_type == 'b':
            return

        if int(expense_type) > n or expense_type.isalpha():
            print("Not valid")
        else:
            expense_amount = float(input("Enter the amount: "))
            exp_report(int(expense_type), expense_amount)

def exp_report(exp_type, exp_amount):
    if expense[exp_type-1]==0:
     expense[exp_type-1]=expense[exp_type-1]+exp_amount
     insert_expense(3, default_menu[exp_type], exp_amount)
    else:
      expense[exp_type-1]=expense[exp_type-1]+exp_amount
      update_expense(default_menu[exp_type], expense[exp_type-1])

def show_savings(total_income):
    total_expense = sum(expense)
    savings = total_income - total_expense
    print(f"Total savings is: {savings}")


default_menu = {1: 'Food', 2: 'Medication', 3: 'Entertainment', 4: 'Groceries', 5: 'Travel', 6: 'Clothing', 7: 'Makeup'}
n = len(default_menu)
expense = [0] * n
expense_type = 0

if __name__ == '__main__':
    create_expenses_table()


    while True:
        print("Choose an option: ")
        print("a. Default menu")
        print("b. Add new category")
        print("c. Delete particular category")
        print("d. Delete all category")
        print("e. View savings")
        print("f. Exit")

        x = input("Enter the letter: ")
        if x == 'a':
            existing_menu()

        elif x == 'b':
            new_cat_name = input("Enter new category name: ")
            default_menu[n + 1] = new_cat_name
            expense.append(0)
            n = n + 1

        elif x == 'c':
            x = 0
            for i in default_menu:
                if len(default_menu[i]) > x:
                    x = len(default_menu[i])
            print("No.   " + "Expense Type".ljust(x + 4, ' ') + "Amount")
            for i in default_menu:
                print(str(i) + ".    " + default_menu[i].ljust(x + 4, ' ') + str(expense[i - 1]))
            specific_eli = input("Enter the type of expense you wanna delete or click 'b' to cancel: ")
            if specific_eli == 'b':
                continue
            delete_expense_particular(default_menu[int(specific_eli)])
            del default_menu[int(specific_eli)]
            

        elif x == 'd':
            default_menu.clear()
            delete_all_expense()

        elif x == 'e':
            total_income = float(input("Enter your total income: "))
            show_savings(total_income)

        elif x == 'f':
            close_connection()
            sys.exit()

        else:
            print("Invalid option. Please try again.")

        