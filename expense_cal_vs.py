import sys

default_menu={1:'Food', 2:'Medication', 3:'Entertainment', 4:'Groceries', 5:'Travel', 6:'Clothing', 7:'Makeup'}
n=len(default_menu)

expense=[0]*n

expense_type=0
def existing_menu():
  while True :
    x=0
    for i in default_menu:
      if len(default_menu[i])>x:
        x=len(default_menu[i])
    print("No.   "+"Expense Type".ljust(x+4,' ')+ "Amount")
    for i in default_menu:
      print(str(i)+".    "+default_menu[i].ljust(x+4,' ')+str(expense[i-1]))

    print("b.back")
   
    expense_type=input("Enter the type of expense: ")
    
    if expense_type=='b':
      return
    if int(expense_type)>n or expense_type.isalpha():
      print("Not valid")
    else:
      expense_amount=float(input("Enter the amount: "))
      exp_report(int(expense_type), expense_amount)

def exp_report(exp_type, exp_amount):
    expense[exp_type-1]=expense[exp_type-1]+exp_amount
    

while True:

  print("Choose an option: ")
  print("b. Add new category")
  print("c. Exit")

  x=input("Enter the letter: ")
  if x=='a':
    existing_menu()
  elif x=='b':
   new_cat_name=input("Enter new category name: ")
   default_menu[n+1]=new_cat_name
   expense.append(0)
   n=n+1
  else:
     sys.exit()