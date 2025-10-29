import os
import json
from datetime import datetime

class Expense() :
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%a, %d, %b, %Y %H:%M")

    def show_expense(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
        }

def input_expense() :
    filename = 'expense.json'
    input_amount = input("amount > ")
    print("Category list : 1. Personal | 2. Home/Family | 3. Food/Grocery | 4. Other | 5. default : Unnecessary")
    while True:
        try:
            input_category = int(input("category > "))
            if 1 <= input_category <= 5 :
                break
            else :
                print("please input only 1-4")
        except ValueError:
                print("Please enter a number")

    input_description = input("description > ")
    #Case input_category to int easy to assign category
    input_category = int(input_category)
    if input_category == 1 :
        category = 'Personal'
    elif input_category == 2 :
        category = 'Home/Family'
    elif input_category == 3 :
        category = 'Food/Grocery'
    elif input_category == 4 :
        category = 'Other'
    else:
        category ='Unnecessary'
    #create class Expense Object
    expense = Expense(input_amount, category, input_description)
    #Use Class method show_expense
    expense = Expense.show_expense(expense)
    print(expense)
    #check if file exist
    if not os.path.exists(filename) or os.path.getsize(filename) == 0 :
        #Create list for first time
        expenses = [expense]
        save_expense(expenses)
    else :
        append_expense(expense)
    return expense

def save_expense(expense):
    filename = 'expense.json'
    with open(filename, 'w') as f :
        #save file as json (data, f, indent=4)
        json.dump(expense, f, indent=4)

def append_expense(expense):
    filename = 'expense.json'
    with open(filename, 'r') as f :
        data = json.load(f)
    #read json to append
        data.append(expense)
    #save json back to file
    with open(filename, 'w') as f :
        json.dump(data, f, indent=4)

def list_expense():
    filename = 'expense.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    #display in readable format
    for i, expense in enumerate(data, 1):
        print(f"\n{i}. Date : {expense['date']}")
        print(f"Amount : ${expense['amount']}")
        print(f"Category : {expense['category']}")
        print(f"Description : {expense['description']}")

def delete_expense():
    #Open and read file with show input to let user select by number
    filename = 'expense.json'
    with open (filename, 'r') as f:
        data = json.load(f)
    for i, expense in enumerate(data, 1):
        print(f"\n{i}. Date : {expense['date']}")
        print(f"Amount : ${expense['amount']}")
        print(f"Category : {expense['category']}")
        print(f"Description : {expense['description']}")

    user_select = int(input("Which number of expense u would like to delete ? >"))
    #List start at 0 but enumerate start at 1 that why index = user_select -1
    index = user_select - 1
    if user_select == 0 :
        print('No Delete')
        return
    elif 1 <= user_select <= len(data) :
        delete = data.pop(index)
        print("Expense Deleted!")
        with open (filename, 'w') as f:
            json.dump(data, f, indent=4)
    else :
        print('Invalid Number')

if __name__ == "__main__":
    input_expense()


