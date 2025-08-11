from logic.bank_account import BankAccount
from logic.income import Income
from logic.expense import Expense
from datetime import datetime

'''
Notes:
- merge bank accounts

*String is the default data type of python*
'''

def get_and_validate_date():
    while True:
        date_str = input('Enter the date (YYYY-MM-DD, leave blank for today): ')
        if not date_str:
            return datetime.today().date()
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    print('Welcome to your Financial Planner')

    account_name = input('Enter the account name: ')
    account_id = input('Enter account ID: ')
    account = BankAccount(account_name, account_id)

    while True:
        print('Menu:')
        print('1. Show Balance')
        print('2. Enter Income')
        print('3. Enter Expense')
        print('4. Show all Incomes')
        print('5. Show all Expenses')
        print('6. Exit')

        user_input = input('Please choose an option: ')

        if user_input == '1':
            print(f'Current Balance: {account.balance:.2f}')

        elif user_input == '2':
            amount = float(input('Enter the amount: '))
            date = get_and_validate_date()
            category = input('Enter category: ') or None
            description = input('Enter description: ') or None

            new_income = Income(amount, date, category, description)
            account.add_income(new_income)

        elif user_input == '3':
            amount = float(input('Enter the amount: '))
            date = get_and_validate_date()
            category = input('Enter category: ') or None
            description = input('Enter description: ') or None

            new_expense = Expense(amount, date, category, description)
            account.add_expense(new_expense)

        elif user_input == '4':
            for i, inc in enumerate(account.get_incomes(), 1):
                print(f'{i}. {inc}')

        elif user_input == '5':
            for i, exp in enumerate(account.get_expenses(), 1):
                print(f'{i}. {exp}')

        elif user_input == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()


# SKELETON APPLICATION

# # 1. Define a custom frame (main window)
# class MainWindow(wx.Frame):
#     def __init__(self, parent, title):
#         super(MainWindow, self).__init__(parent, title=title, size=(1000, 500))

#         # LOCAL VARIABLES:
#         # 2. Panel to hold UI elements
#         panel = wx.Panel(self)

#         # INSTANCE VARIABLES: (methods from the parent class wx.Frame)
#         # 3. Static text label
#         self.label = wx.StaticText(panel, label="Welcome to Financial Planner", pos=(20, 20)) # Provide the window, name and position

#         # 4. Button with click event
#         self.button = wx.Button(panel, label="Test Button", pos=(20, 60)) # Provide the window, name and position
#         self.button.Bind(wx.EVT_BUTTON, self.on_click) # Provide the actuator(event) and the response(handler)

#         self.Centre()  # Center the window
#         self.Show()    # Show the window

#     # 5. Event handler for button
#     def on_click(self, event):
#         print("Working")  # Test output to console
#         self.label.SetLabel("Button clicked!")  # Update label text


# # 6. Start the application
# if __name__ == "__main__": # Simply used as a safe way to start the program
#     app = wx.App(False) # Create the actual app
#     frame = MainWindow(None, title="Financial Planner") # Create the frame object (not the actual app)
#     app.MainLoop() # Loop to check for events