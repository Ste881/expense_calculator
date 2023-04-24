import sys
expense=[0, 0, 0, 0, 0, 0, 0, 0]
print(f"expense array={expense}")

n=7
default_menu={1:'Food', 2:'Medication', 3:'Entertainment', 4:'Groceries', 5:'Travel', 6:'Clothing', 7:'Makeup'}

expense_type=0
def Existing_menu():
  while expense_type < 9 :
    # print("Choose the type of expense: ")
    # print("1. Food")
    # print("2. Medication")
    # print("3. Entertainment")
    # print("4. Groceries")
    # print("5. Travel")
    # print("6. Clothing")
    # print("7. Makeup")
    # print("8. Other:")
    print("b.back")

    
  #for loop dictionary
    expense_type=int(input("Enter the type of expense: ")) 
    
    if str(expense_type)==b:
      return
    if expense_type>8:
      break
     
 #if condn for 8
  expense_amount=float(input("Enter the amount: "))
  
  exp_report(expense_type, expense_amount)




def exp_report(exp_type, exp_amount):
  if exp_type <= 7:
    expense[exp_type-1]=expense[exp_type-1]+exp_amount
    print(f"expense array={expense}")
  else:
    print("not valid")


while true:

  print("Choose an option: ")
  #menu_dic={'a':{'':{1: 'Food', 2: 'Medication', 3:'Entertainment', 4:'Groceries', 5:'Travel', 6:'Clothing', 7:'Makeup'}}, 'b':{'Add new menu':''}, 'c':'exit'}
  print("a. Existing menu")
  print("b. Add new category")
  print("c. Exit")

  x=input("Enter the letter: ")
  if x==a:
    Existing_menu()
  elif x==b:
   new_cat_name=input("Enter new category name: ")
   default_menu[n+1]=new_cat_name
   n=n+1
  else:
     sys.exit()