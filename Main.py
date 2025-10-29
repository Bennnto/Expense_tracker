from Expense import Expense, input_expense, list_expense, delete_expense
import sys

def main () :
    print("Expense Tracker!")
    print("---- Main ----")
    print("A. Record New Expense")
    print("B. List Expense Record")
    print("C. Delete Expense Record")
    print("D. Exit Program")
    while True:
        try:
            user_input = input ("select from menu A-D > ")
            #to upper easy validate upper lower character
            user_input = user_input.upper()
            #Validate input
            if user_input in ('A', 'B', 'C', 'D'):
                break
            else :
                print("Invalid input try again")
        except ValueError :
            print("Invalid Input Value Error")

    if user_input == 'A':
        input_expense()
        main()
    elif user_input == 'B':
        list_expense()
        main()
    elif user_input == 'C':
        delete_expense()
        main()
    elif user_input == 'D':
        print('Exit Program')
        sys.exit()

if __name__ == "__main__":
    main()
