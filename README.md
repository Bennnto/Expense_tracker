# Expense Tracker
  Expense Tracker is a command line interface program write in python3 using simple logic and built-in python modules and store your expenses data
  in json file (local storage).
  - Files
    1. Expense.py
    2. Main.py
  - How to use
    - Download Expense.py and Main.py and save its to the same directory
    - Execute python by ```Python or Python3 Main.py```
  - Amendment
    You can adjust category to fit with your personal use by
    - Go to Expense.py find ```def input_expense():```
    - Make change from ```line 37 - 43``` you will see category matching with number
    - Don't forget to change ```line 23``` Display category list to easy input when you use program

## Functions

| No. | Name | Function                        |
|-----|------|---------------------------------|
|1.   | Add  | Add Expense to json file storage |
|     |      | data = date, amount, category, description|
|2.   | List | List all expense data in storange |
|3.   | Delete | Delete expense data that user selected |
