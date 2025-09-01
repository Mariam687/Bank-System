
from pickle import TRUE
import pyodbc
import os
import re
from datetime import datetime



# Define the connection string
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-CSHNM6I;'  
    'DATABASE=BankSystem;'
    'Trusted_Connection=yes;'
)


# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()


##########################################################################################
#                                 Customer Menue                                         #
##########################################################################################


def Customer_Menue():

        os.system('clear') 
        print("===========================================")
        print("\t  Customer Screen")
        print("===========================================")
        print("\t[1] Show Customers List.")
        print("\t[2] Show Customer info.")
        print("\t[3] Add New Customer.")
        print("\t[4] Alter Customer Info.")
        print("\t[5] Delete Customer.")
        print("\t[6] Go Back To Main Menue.")
        print("===========================================")

        Customer_Menue_Option = get_user_input() 
        perform_customer_menue_option(Customer_Menue_Option) 


def Show_Customers_List():

    os.system('clear') 

    # Fetch column names

    
    print("=" * 120)
    print('\n')

    print("\t\t\t\t\t\t\t\t\t\t\tCustomers List")
    print("==============================================================================================================================================================================================================")

    # Execute the query to fetch all customers
    cursor.execute('SELECT * FROM Customer')
    customers = cursor.fetchall()
    
    for customer in customers:
        print(f"{'ID:':<4} {customer[0]:<4} "
              f"{'Address:':<8} {customer[1]:<30} "
              f"{'Email:':<6} {customer[2]:<28} "
              f"{'Date Joined:':<12} {customer[3]:} "
              f"{'Phone:':<6} {customer[4]:<15} "
              f"{'First Name:':<10} {customer[5]:<12} "
              f"{'Last Name:':<10} {customer[6]:<12} "
              f"{'ID Number:':<10} {customer[7]:<12}")

    print("==============================================================================================================================================================================================================")

    input("Press Enter to continue...")
    Customer_Menue()




def Show_Customer_Info():

    os.system('clear') 

    print("\t Customer Info List")
    print("======================================")

    customer_id = int(input("Enter Customer ID: "))

    # Retrieve the customer's information from the database
    cursor.execute('''
    SELECT * FROM Customer WHERE Customer_id = ?
    ''', (customer_id))

    # Fetch the result
    customer = cursor.fetchone()

    # Check if the customer exists
    if customer:
        print("Customer Information:")
        print(f"Customer ID: {customer[0]}")
        print(f"First Name: {customer[5]}")
        print(f"Last Name: {customer[6]}")
        print(f"Address: {customer[1]}")
        print(f"Email: {customer[2]}")
        print(f"Date Joined: {customer[3]}")
        print(f"Phone Number: {customer[4]}")
        print(f"Identification Number: {customer[7]}")
    else:
        print("Customer not found.")

    
    input("Press Enter to continue...")
    Customer_Menue()

def is_valid_date(date_string):
    # Regular expression pattern for YYYY-MM-DD
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_string))



def Add_New_Customer():

    os.system('clear') 
    print("======================================")
    print("\tAdd New Customer List")
    print("======================================")

    customer_id = int(input("Enter Customer ID: "))

    # Check if the customer ID already exists
    cursor.execute('SELECT * FROM Customer WHERE Customer_id = ?', (customer_id))
    if cursor.fetchone():
        print("Customer ID already exists.")
    else:
        address = input("Enter Address: ")
        email = input("Enter Email: ")
        while True:
            date_joined = input("Enter Date Joined (YYYY-MM-DD): ")
            if is_valid_date(date_joined):
                print("Valid date format.")
                break  # Exit the loop if the date is valid
            else:
                print("Invalid format. Please enter the date in YYYY-MM-DD format.")
        phone_num = input("Enter Phone Number: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        identification_number = input("Enter Identification Number: ")

        # Insert the data into the Customer table
        cursor.execute('''
        INSERT INTO Customer (Customer_id, Address, Email, Date_joined, Phone_num, First_name, Last_name, Identification_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (customer_id, address, email, date_joined, phone_num, first_name, last_name, identification_number))

        # Commit the transaction and close the connection
        conn.commit()
        print("Customer data inserted successfully!")

    
    input("Press Enter to continue...")
    Customer_Menue()

def Alter_Customer_Info():

    os.system('clear') 
    print("======================================")
    print("\tAlter Customer info List")
    print("======================================")

    
    customer_id = int(input("Enter Customer ID: "))

    cursor.execute('SELECT * FROM Customer WHERE Customer_id = ?', (customer_id))
    if not cursor.fetchone():
        print("Customer ID is not found.")
    else:
        updates = {}
        
        if input("Do you want to update Address? (yes/no): ").lower() == 'yes':
            updates['Address'] = input("Enter Address: ")
        
        if input("Do you want to update Email? (yes/no): ").lower() == 'yes':
            updates['Email'] = input("Enter Email: ")
        
        
        if input("Do you want to update Phone Number? (yes/no): ").lower() == 'yes':
            updates['Phone_num'] = input("Enter Phone Number: ")
        
        if input("Do you want to update First Name? (yes/no): ").lower() == 'yes':
            updates['First_name'] = input("Enter First Name: ")
        
        if input("Do you want to update Last Name? (yes/no): ").lower() == 'yes':
            updates['Last_name'] = input("Enter Last Name: ")
        
        if input("Do you want to update Identification Number? (yes/no): ").lower() == 'yes':
            updates['Identification_number'] = input("Enter Identification Number: ")

        if updates:
            set_clause = ', '.join([f"{key} = ?" for key in updates.keys()])
            values = list(updates.values())
            values.append(customer_id)
            
            cursor.execute(f'''
            UPDATE Customer
            SET {set_clause}
            WHERE Customer_id = ?
            ''', values)

            conn.commit()
            print("Customer data altered successfully!")
        else:
            print("No updates were made.")

    
    input("Press Enter to continue...")
    Customer_Menue()


def Delete_Customer():

    os.system('clear') 
    print("======================================")
    print("\tDelete Customer List")
    print("======================================")

    customer_id = int(input("Enter Customer ID: "))

    
    cursor.execute('SELECT * FROM Customer WHERE Customer_id = ?', (customer_id))
    if not cursor.fetchone():
        print("Customer ID is not found.")
    else:
        
        cursor.execute('''
        delete from Customer
        WHERE Customer_id = ?
        ''', (customer_id))

        # Commit the transaction and close the connection
        conn.commit()
        print("Customer deleted successfully!")

   
    input("Press Enter to continue...")
    Customer_Menue()



def perform_customer_menue_option(menu_option):

    os.system('clear') 
    if menu_option == 1:
        Show_Customers_List()
    elif menu_option == 2:
        Show_Customer_Info()
    elif menu_option == 3:
        Add_New_Customer()
    elif menu_option == 4:
        Alter_Customer_Info()
    elif menu_option == 5:
        Delete_Customer()
    elif menu_option == 6:
        show_main_menu()


##########################################################################################
#                                 Employee Menue                                         #
##########################################################################################

def Employee_Menue():

        os.system('clear') 
        print("=========================================")
        print("\t   Employee Screen")
        print("=========================================")
        print("\t[1] Show Employees List.")
        print("\t[2] Show Employee info.")
        print("\t[3] Add New Employee.")
        print("\t[4] Alter Employee Info.")
        print("\t[5] Delete Employee.")
        print("\t[6] Go Back To Main Menue.")
        print("=========================================")

        Employee_Menue_Option = get_user_input() 
        perform_employee_menue_option(Employee_Menue_Option) 


def Show_Employees_List():


    os.system('clear')

    query = "SELECT * FROM employee"
    cursor.execute(query)

    # Fetch all rows from the executed query
    employees = cursor.fetchall()

    # Print header with improved spacing and clarity
    print("=" * 200)
    print("\t\t\t\t\t\t\t\t\t\t\tEmployees List")
    print("=" * 200)
    print(f"{'Employee ID':<15}{'First Name':<15}{'Last Name':<15}"
          f"{'Email':<35}{'Password':<18}{'':<10}"  # Added 10 spaces for extra spacing
          f"{'Salary':<18}{'Role':<20}{'Permission':<20}"
          f"{'Branch ID':<15}{'Username':<18}")
    print("=" * 200)

    # Print employee data with consistent spacing and currency formatting
    for employee in employees:
        print(f"{employee[0]:<15}{employee[1]:<15}{employee[2]:<15}"
              f"{employee[3]:<35}{employee[4]:<18}{'':<10}"  # Added 10 spaces for extra spacing
              f"${employee[6]:<18,.2f}{employee[7]:<20}{employee[8]:<20}"
              f"{employee[9]:<15}{employee[10]:<18}")


    input("Press Enter to continue...")
    Employee_Menue()

def Show_Employee_Info():

    os.system('clear') 
    print("======================================")
    print("\t Employee Info List")
    print("======================================")

    employee_id = int(input("Enter Employee ID: "))

    
    cursor.execute('''
    SELECT * FROM employee WHERE employee_id = ?
    ''', (employee_id))

    # Fetch the result
    employee = cursor.fetchone()

    
    if employee:
          print(f"{'Employee ID:':<15} {employee[0]:<4} ")
          print(f"{'First Name:':<12} {employee[1]:<12} ")
          print(f"{'Last Name:':<12} {employee[2]:<12} ")
          print(f"{'Email:':<10} {employee[3]:<28} ")
          print(f"{'Password:':<10} {employee[4]:<12} ")
          print(f"{'Date Hired:':<12} {employee[5]:<15} ")
          print(f"{'Salary:':<8} ${employee[6]:<10} ")
          print(f"{'Role:':<6} {employee[7]:<12} ")
          print(f"{'Permission:':<12} {employee[8]:<10} ")
          print(f"{'Branch ID:':<12} {employee[9]:<4} ")
          print(f"{'Username:':<10} {employee[10]:<12}")
    else:
        print("Employee not found.")

    
    input("Press Enter to continue...")
    Employee_Menue()

def Add_New_Employee():

    os.system('clear') 
    print("======================================")
    print("\t Add New Employee List")
    print("======================================")

    # Get employee details from user input
    employee_id = int(input("Enter Employee ID: "))

    # Check if the employee already exists 
    cursor.execute('SELECT * FROM employee WHERE Employee_id = ?', (employee_id))
    existing_employee = cursor.fetchone()

    if existing_employee:
        print("Employee with this ID already exists.")
    else:

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        while True:
            date_joined = input("Enter Date Joined (YYYY-MM-DD): ")
            if is_valid_date(date_joined):
                print("Valid date format.")
                break  # Exit the loop if the date is valid
            else:
                print("Invalid format. Please enter the date in YYYY-MM-DD format.")
        salary = float(input("Enter Salary: "))
        role = input("Enter Role: ")
        permission = input("Enter Permission: ")
        while True:
            branch_id = input("Enter Branch ID: ")
            if is_valid_BranchID(branch_id):
                break  
            else:
                print("Invalid ID.")
        username = input("Enter Username: ")

        cursor.execute('''
            INSERT INTO employee (Employee_id, first_name, last_name, email, password, Date_hired, salary, Role, permission, Branch_id, username)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (employee_id, first_name, last_name, email, password, date_joined, salary, role, permission, branch_id, username))

        # Commit the changes
        conn.commit()
        print("New employee added successfully.")

    
    input("Press Enter to continue...")
    Employee_Menue()

def is_valid_BranchID(branch_id):

    
    cursor.execute("SELECT * FROM branch WHERE branch_id = ?", (branch_id))
    branch_exists = cursor.fetchone()

    if branch_exists:
        return True
    else:
        return False

def Alter_Employee_Info():

    os.system('clear') 
    print("======================================")
    print("      Alter Employee Info List        ")
    print("======================================")

   
    employee_id = int(input("Enter Employee ID: "))

    cursor.execute('SELECT * FROM employee WHERE Employee_id = ?', (employee_id,))
    existing_employee = cursor.fetchone()

    if not existing_employee:
        print("Employee doesn't exist.")
    else:
        updates = {}

        if input("Do you want to update First Name? (yes/no): ").lower() == 'yes':
            updates['first_name'] = input("Enter First Name: ")

        if input("Do you want to update Last Name? (yes/no): ").lower() == 'yes':
            updates['last_name'] = input("Enter Last Name: ")

        if input("Do you want to update Email? (yes/no): ").lower() == 'yes':
            updates['email'] = input("Enter Email: ")

        if input("Do you want to update Password? (yes/no): ").lower() == 'yes':
            updates['password'] = input("Enter Password: ")

        

        if input("Do you want to update Salary? (yes/no): ").lower() == 'yes':
            updates['salary'] = float(input("Enter Salary: "))

        if input("Do you want to update Role? (yes/no): ").lower() == 'yes':
            updates['Role'] = input("Enter Role: ")

        if input("Do you want to update Permission? (yes/no): ").lower() == 'yes':
            updates['permission'] = input("Enter Permission: ")

        if input("Do you want to update Branch ID? (yes/no): ").lower() == 'yes':
            while True:
                branch_id = input("Enter Branch ID: ")
                if is_valid_BranchID(branch_id):
                    updates['Branch_id'] = branch_id
                    break
                else:
                    print("Invalid ID.")

        if input("Do you want to update Username? (yes/no): ").lower() == 'yes':
            updates['username'] = input("Enter Username: ")

        if updates:
            set_clause = ', '.join([f"{key} = ?" for key in updates.keys()])
            values = list(updates.values())
            values.append(employee_id)

            cursor.execute(f'''
            UPDATE employee
            SET {set_clause}
            WHERE Employee_id = ?
            ''', values)

            conn.commit()
            print("Employee Info Changed Successfully.")
        else:
            print("No updates were made.")

   
    input("Press Enter to continue...")
    Employee_Menue()



def Delete_Employee():

    os.system('clear') 
    print("======================================")
    print("\tDelete Employee List")
    print("======================================")

    employee_id = int(input("Enter Employee ID: "))

    
    cursor.execute('SELECT * FROM employee WHERE employee_id = ?', (employee_id))
    if not cursor.fetchone():
        print("Employee ID is not found.")
    else:
        
        cursor.execute('''
        delete from employee
        WHERE employee_id = ?
        ''', (employee_id))

        # Commit the transaction and close the connection
        conn.commit()
        print("Employee deleted successfully!")

   
    input("Press Enter to continue...")
    Employee_Menue()





def perform_employee_menue_option(menu_option):

    os.system('clear') 
    if menu_option == 1:
        Show_Employees_List()
    elif menu_option == 2:
        Show_Employee_Info()
    elif menu_option == 3:
        Add_New_Employee()
    elif menu_option == 4:
        Alter_Employee_Info()
    elif menu_option == 5:
        Delete_Employee()
    elif menu_option == 6:
        show_main_menu()


##########################################################################################
#                                   Branch Menue                                         #
##########################################################################################



def Branch_Menue():

        # Fetch data from the Branch table
        cursor.execute("SELECT Branch_id, Contact_num, Name, Address, employee_id FROM Branch")
        rows = cursor.fetchall()
                
        columns = ["Branch_id", "Contact_num", "Name", "Address", "employee_id"]

        # Calculate the maximum width for each column
        max_widths = [len(column) for column in columns]
        for row in rows:
            for i, value in enumerate(row):
                max_widths[i] = max(max_widths[i], len(str(value)))

        # Create a horizontal separator
        separator = '+'.join(['-' * (width + 2) for width in max_widths])
        separator = f"+{separator}+"

        # Print the table header
        header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
        header = f"|{header}|"
        print(separator)
        print(header)
        print(separator)

        # Print the table rows
        for row in rows:
            row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
            row_str = f"|{row_str}|"
            print(row_str)
            print(separator)


        input("Press Enter to continue...")
        Employee_Menue()


##########################################################################################
#                                  Account Menue                                         #
##########################################################################################


def Account_Menue():

        os.system('clear') 
        print("=========================================")
        print("\tAccount Screen")
        print("=========================================")
        print("\t[1] Show Accounts.")
        print("\t[2] Show Account Info.")
        print("\t[3] Add new account.")
        print("\t[4] Delete account.")
        print("\t[5] Update Account Status.")
        print("\t[6] Go Back To Main Menue.")
        print("=========================================")

        Account_Menue_Option = get_user_input() 
        perform_account_menue_option(Account_Menue_Option) 

def perform_account_menue_option(menu_option):

    os.system('clear') 
    if menu_option == 1:
        Show_Accounts_List()
    elif menu_option == 2:
        Show_Account_Info()
    elif menu_option == 3:
        Add_New_Account()
    elif menu_option == 4:
        Delete_Account()
    elif menu_option == 5:
        Update_Account_Status()
    elif menu_option == 6:
        show_main_menu()

        

def Show_Accounts_List():

        # Fetch data from the Account table
        cursor.execute("SELECT Account_id, Status, Balance, Date_created, type, customer_id FROM Account")
        rows = cursor.fetchall()

        # Define the column names
        columns = ["Account_id", "Status", "Balance", "Date_created", "type", "customer_id"]

        # Calculate the maximum width for each column
        max_widths = [len(column) for column in columns]
        for row in rows:
            for i, value in enumerate(row):
                max_widths[i] = max(max_widths[i], len(str(value)))

        # Create a horizontal separator
        separator = '+'.join(['-' * (width + 2) for width in max_widths])
        separator = f"+{separator}+"

        # Print the table header
        header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
        header = f"|{header}|"
        print(separator)
        print(header)
        print(separator)

        # Print the table rows
        for row in rows:
            row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
            row_str = f"|{row_str}|"
            print(row_str)
            print(separator)


        input("Press Enter to continue...")
        Account_Menue()

def printAccountInfo(account_id):

    cursor.execute("SELECT Account_id, Status, Balance, Date_created, type, customer_id FROM Account WHERE Account_id = ?", (account_id,))
    account = cursor.fetchone()

    # Check if the account exists
    if account:
        # Print the account information
        print(f"{'Account ID:':<15} {account[0]}")
        print(f"{'Status:':<15} {account[1]}")
        print(f"{'Balance:':<15} {account[2]}")
        print(f"{'Date Created:':<15} {account[3]}")
        print(f"{'Type:':<15} {account[4]}")
        print(f"{'Customer ID:':<15} {account[5]}")
    else:
        print("Account not found.")

def Show_Account_Info():

    print("=========================================")
    print("\tAccount Info Screen")
    print("=========================================")

    account_id = input("Enter the Account ID: ")
    printAccountInfo()

    
    print("=========================================")
    input("Press Enter to continue...")
    Account_Menue()

def account_exists(account_id):
    cursor.execute("SELECT 1 FROM Account WHERE Account_id = ?", (account_id,))
    return cursor.fetchone() is not None

def customer_exists(customer_id):
    cursor.execute("SELECT 1 FROM Customer WHERE customer_id = ?", (customer_id))
    return cursor.fetchone() is not None

def account_exists(account_id):
    cursor.execute("SELECT 1 FROM Account WHERE Account_id = ?", (account_id,))
    return cursor.fetchone() is not None

def Add_New_Account():

    print("=========================================")
    print("\tAdd New Account Screen")
    print("=========================================")

    # Prompt the user for account details
    account_id = input("Enter the Account ID: ")

    if account_exists(account_id):
        print("Account already exists.")
    else:
        status = input("Enter the Status: ")
        balance = 0
        while True:
            date_created = input("Enter Date Created (YYYY-MM-DD): ")
            if is_valid_date(date_created):
                break 
            else:
                print("Invalid format. Please enter the date in YYYY-MM-DD format.")

        account_type = input("Enter the Type: ")

        while True:
            customer_id = input("Enter the Customer ID: ")
            if customer_exists(customer_id):
                break  
            else:
                print("Customer is not found, enter another one ")

        
        cursor.execute("INSERT INTO Account (Account_id, Status, Balance, Date_created, type, customer_id) VALUES (?, ?, ?, ?, ?, ?)",
                       (account_id, status, balance, date_created, account_type, customer_id))
        conn.commit()
        print("Account added successfully.")

    input("Press Enter to continue...")
    Account_Menue()

def Update_Account_Status():

    print("=========================================")
    print("\tUpdate Account Status Screen")
    print("=========================================")
    account_id = input("Enter the Account ID: ")

    if not account_exists(account_id):
        print("Account is not found.")
    else:
        status = input("Enter the Status: ")
        cursor.execute('update account set status= ? where account_id= ?',(status,account_id))
        print("Account status changed successfully.")

    print("=========================================")

    input("Press Enter to continue...")
    Account_Menue()


def Delete_Account():

    account_id = input("Enter the Account ID to delete: ")
    if account_exists(account_id):
        cursor.execute("DELETE FROM Account WHERE Account_id = ?", (account_id,))
        conn.commit()
        print("Account deleted successfully.")
    else:
        print("Account not found.")

    input("Press Enter to continue...")
    Account_Menue()


##########################################################################################
#                                 Transaction Menue                                      #
##########################################################################################

def Transaction_Menue():

        os.system('clear') 
        print("=================================================")
        print("                Transaction Screen               ")
        print("=================================================")
        print("\t[1] Show Transactions.")
        print("\t[2] Search for Transaction by ID.")
        print("\t[3] Deposite Menue.")
        print("\t[4] Withdraw Menue.")
        print("\t[5] Transfer from account to another one.")
        print("\t[6] Show Incoming Transfers.")
        print("\t[7] Show Outgoing Transfers.")
        print("\t[8] Go Back To Main Menue.")
        print("=================================================")

        Transaction_Menue_Option = get_user_input() 
        perform_transaction_menue_option(Transaction_Menue_Option) 

def perform_transaction_menue_option(menu_option):

        os.system('clear') 
        if menu_option == 1:
            Show_Transactions()
        elif menu_option == 2:
            Search_Transaction()
        elif menu_option == 3:
            Deposit_Menue()
        elif menu_option == 4:
            Withdraw_Menue()
        elif menu_option == 5:
            transfer()
        elif menu_option == 6:
            Show_Incoming_Transfers()
        elif menu_option == 7:
            Show_Outgoing_Transfers()
        elif menu_option == 8:
            show_main_menu()

def Show_Transactions():

    cursor.execute("SELECT Id, Amount, Type, Date, Account_id FROM [Transaction]")
    rows = cursor.fetchall()

    # Define the column names
    columns = ["Id", "Amount", "Type", "Date", "Account_id"]

    # Calculate the maximum width for each column
    max_widths = [len(column) for column in columns]
    for row in rows:
        for i, value in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(value)))

    # Create a horizontal separator
    separator = '+'.join(['-' * (width + 2) for width in max_widths])
    separator = f"+{separator}+"

    # Print the table header
    header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
    header = f"|{header}|"
    print(separator)
    print(header)
    print(separator)

    # Print the table rows
    for row in rows:
        row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
        row_str = f"|{row_str}|"
        print(row_str)
        print(separator)

    input("Press Enter to continue...")
    Transaction_Menue()

def Search_Transaction():

    print("=========================================")
    print("\tSearch For Transaction Screen")
    print("=========================================")

    # Prompt the user for the Transaction ID
    transaction_id = input("Enter the Transaction ID: ")

    cursor.execute("SELECT Id, Amount, Type, Date, Account_id FROM [Transaction] WHERE Id = ?", (transaction_id,))
    transaction = cursor.fetchone()
    
    if transaction:
        print(f"{'Transaction ID:':<15} {transaction[0]}")
        print(f"{'Amount:':<15} {transaction[1]}")
        print(f"{'Type:':<15} {transaction[2]}")
        print(f"{'Date:':<15} {transaction[3]}")
        print(f"{'Account ID:':<15} {transaction[4]}")
    else:
        print("Transaction not found.")

    print("=========================================")

    input("Press Enter to continue...")
    Transaction_Menue()

def Deposit_Menue():

     print("=========================================")
     print("\t\tDeposit Screen")
     print("=========================================")

     # Prompt the user for account details
     account_id = int(input("Enter the Account ID: "))

     # Call the stored procedure
     cursor.execute("{CALL My_Account (?)}", account_id)
     
     # Fetch the results
     result = cursor.fetchone()
     
     if result:
         message = result.Message
         balance = result.Balance if 'Balance' in result.cursor_description else None
         print(f"Message: {message}")
         if balance:
             print(f"Balance: {balance}")
     else:
        print("No result returned from the procedure.")

     
     if message=='OK, how can I help you':
         
             print('Account Info')
             print('-'*40)
             printAccountInfo(account_id)
             amount = float(input("Enter the Amount to deposit: "))
             transaction_type = 'deposit'
             transaction_date = datetime.now().strftime('%Y-%m-%d')

             cursor.execute("{CALL Deposit_Withdraw(?, ?, ?, ?)}", (account_id, amount, transaction_type, transaction_date))
             conn.commit()
             print("Deposit successfully.")

             print('New Account Info')
             print('-'*40)
             printAccountInfo(account_id)

     

     input("Press Enter to continue...")
     Transaction_Menue()

def Withdraw_Menue():

     print("=========================================")
     print("\t\tWithdraw Screen")
     print("=========================================")

     # Prompt the user for account details
     account_id = int(input("Enter the Account ID: "))

     # Call the stored procedure
     cursor.execute("{CALL My_Account (?)}", account_id)
     
     # Fetch the results
     result = cursor.fetchone()
     
     if result:
         message = result.Message
         balance = result.Balance if 'Balance' in result.cursor_description else None
         print(f"Message: {message}")
         if balance:
             print(f"Balance: {balance}")
     else:
        print("No result returned from the procedure.")

     
     if message=='OK, how can I help you':
         
         print('Account Info')
         print('-'*40)
         printAccountInfo(account_id)
         amount = float(input("Enter the Amount to withdraw: "))

         cursor.execute("SELECT dbo.check_balance(?, ?)", (account_id, amount))
         result = cursor.fetchone()

         if result[0]:
             transaction_type = 'withdraw'
             transaction_date = datetime.now().strftime('%Y-%m-%d')

             cursor.execute("{CALL Deposit_Withdraw(?, ?, ?, ?)}", (account_id, amount, transaction_type, transaction_date))
             conn.commit()
             print("withdraw done successfully.")

             print('New Account Info')
             print('-'*40)
             printAccountInfo(account_id)
         else:
                print("Insufficient balance.")

    
         

     input("Press Enter to continue...")
     Transaction_Menue()

def transfer():

     print("=================================================")
     print("              Transfer Screen")
     print("=================================================")

     saccount_id = int(input("Enter the Source Account ID     : "))
     daccount_id = int(input("Enter the Destination Account ID: "))

     if account_exists(saccount_id) and account_exists(daccount_id) :
         print('------------------------------------------')
         print('          Source Account Info')
         print('------------------------------------------')
         printAccountInfo(saccount_id)
         print('------------------------------------------')
         print('        Destination Account Info')
         print('------------------------------------------')
         printAccountInfo(daccount_id)
         print('------------------------------------------')
         amount = float(input("Enter the Amount to transfer: "))

         cursor.execute("SELECT dbo.check_balance(?, ?)", (saccount_id, amount))
         result = cursor.fetchone()
         if result[0]:
             
             transferdate = datetime.now().strftime('%Y-%m-%d')

             cursor.execute("{CALL Transfer(?, ?, ?, ?)}", (saccount_id,daccount_id, amount,transferdate))
             conn.commit()
             print("\n\ntransfer done successfully.\n")

             print('------------------------------------------')
             print('        New Source Account Info')
             print('------------------------------------------')
             printAccountInfo(saccount_id)
             print('------------------------------------------')
             print('       New Destination Account Info')
             print('------------------------------------------')
             printAccountInfo(daccount_id)
             print('------------------------------------------')
         else:
                print("Insufficient balance.")




     else:
         print('Both Accounts Must Exist!!')


     print("="*60)
     input("Press Enter to continue...")
     Transaction_Menue()

def Show_Incoming_Transfers():

    cursor.execute("SELECT id, Date, Amount, Destination_account, Account_id FROM incoming_transfers")
    rows = cursor.fetchall()

    # Define the column names
    columns = ["id", "Date", "Amount", "Destination_account", "Account_id"]

    # Calculate the maximum width for each column
    max_widths = [len(column) for column in columns]
    for row in rows:
        for i, value in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(value)))

    # Create a horizontal separator
    separator = '+'.join(['-' * (width + 2) for width in max_widths])
    separator = f"+{separator}+"

    # Print the table header
    header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
    header = f"|{header}|"
    print(separator)
    print(header)
    print(separator)

    # Print the table rows
    for row in rows:
        row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
        row_str = f"|{row_str}|"
        print(row_str)
        print(separator)

    input("Press Enter to continue...")
    Transaction_Menue()


def Show_Outgoing_Transfers():

    cursor.execute("SELECT Id, [Date], Amount, Destination_account, Account_id FROM outgoing_transfers")
    rows = cursor.fetchall()

    # Define the column names
    columns = ["Id", "Date", "Amount", "Destination_account", "Account_id"]

    # Calculate the maximum width for each column
    max_widths = [len(column) for column in columns]
    for row in rows:
        for i, value in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(value)))

    # Create a horizontal separator
    separator = '+'.join(['-' * (width + 2) for width in max_widths])
    separator = f"+{separator}+"

    # Print the table header
    header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
    header = f"|{header}|"
    print(separator)
    print(header)
    print(separator)

    # Print the table rows
    for row in rows:
        row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
        row_str = f"|{row_str}|"
        print(row_str)
        print(separator)

    input("Press Enter to continue...")
    Transaction_Menue()


##########################################################################################
#                                        Loan Menue                                      #
##########################################################################################



def Loan_Menue():

    cursor.execute("SELECT Loan_id, [Start], [End], [Status], Amount, Purpose, Account_id FROM Loan")
    rows = cursor.fetchall()

    # Define the column names
    columns = ["Loan_id", "Start", "End", "Status", "Amount", "Purpose", "Account_id"]

    # Calculate the maximum width for each column
    max_widths = [len(column) for column in columns]
    for row in rows:
        for i, value in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(value)))

    # Create a horizontal separator
    separator = '+'.join(['-' * (width + 2) for width in max_widths])
    separator = f"+{separator}+"

    # Print the table header
    header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
    header = f"|{header}|"
    print(separator)
    print(header)
    print(separator)

    # Print the table rows
    for row in rows:
        row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
        row_str = f"|{row_str}|"
        print(row_str)
        print(separator)

    input("Press Enter to continue...")
    Transaction_Menue()


##########################################################################################
#                                        Card Menue                                      #
##########################################################################################


def Card_Menue():

        os.system('clear') 
        print("=================================================")
        print("                   Card Screen                   ")
        print("=================================================")
        print("\t[1] Show Cards.")
        print("\t[2] Add New Card.")
        print("\t[3] Search for Card by ID.")
        print("\t[4] Update Card Info.")
        print("\t[5] Delete Card.")
        print("\t[6] Go Back To Main Menue.")
        print("=================================================")

        Card_Menue_Option = get_user_input() 
        perform_card_menue_option(Card_Menue_Option) 

def perform_card_menue_option(menu_option):

        os.system('clear') 
        if menu_option == 1:
            Show_Cards()
        elif menu_option == 2:
            Add_New_Card()
        elif menu_option == 3:
            Search_Card()
        elif menu_option == 4:
            Update_Card()
        elif menu_option == 5:
            Delete_Card()
        elif menu_option == 6:
            show_main_menu()
    
def Show_Cards():

    os.system('clear') 

    cursor.execute("SELECT Card_id, [password], [type], Number, Expired, [status], Account_id FROM Card")
    rows = cursor.fetchall()

    # Define the column names
    columns = ["Card_id", "password", "type", "Number", "Expired", "status", "Account_id"]

    # Calculate the maximum width for each column
    max_widths = [len(column) for column in columns]
    for row in rows:
        for i, value in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(value)))

    # Create a horizontal separator
    separator = '+'.join(['-' * (width + 2) for width in max_widths])
    separator = f"+{separator}+"

    # Print the table header
    header = '|'.join([f" {column.ljust(max_widths[i])} " for i, column in enumerate(columns)])
    header = f"|{header}|"
    print(separator)
    print(header)
    print(separator)

    # Print the table rows
    for row in rows:
        row_str = '|'.join([f" {str(value).ljust(max_widths[i])} " for i, value in enumerate(row)])
        row_str = f"|{row_str}|"
        print(row_str)
        print(separator)

    input("Press Enter to continue...")
    Card_Menue()

def Add_New_Card():

    os.system('clear') 

    print("=================================================")
    print("                Add New Card Screen              ")
    print("=================================================")

    card_id = input("Enter Card ID: ")

    cursor.execute("SELECT * FROM Card WHERE Card_id = ?", (card_id,))
    existing_card = cursor.fetchone()

    if existing_card:
        print(f"Card with Card_id {card_id} already exists.")
    else:
        password = input("Enter Password: ")
        card_type = input("Enter Card Type: ")
        number = input("Enter Card Number: ")
        while True:
            expired = input("Enter Expiry Date (YYYY-MM-DD): ")
            if is_valid_date(expired):
                    break  
            else:
                    print("Invalid format. Please enter the date in YYYY-MM-DD format.")
        
        status = input("Enter Status: ")
        while True:
            account_id = input("Enter the Account ID: ")
            if customer_exists(account_id):
                break  
            else:
                print("Account is not found, enter another one ")
        cursor.execute("""
            INSERT INTO Card (Card_id, password, type, Number, Expired, status, Account_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (card_id, password, card_type, number, expired, status, account_id))
        conn.commit()
       
        print(f"New card with Card_id {card_id} added successfully.")

    input("Press Enter to continue...")
    Card_Menue()


def Search_Card():

    os.system('clear') 
    print("=================================================")
    print("              Search For Card Screen             ")
    print("=================================================")

    # Get the Card ID from user input
    card_id = input("Enter Card ID: ")

    # Query the Card table for the specific Card ID
    cursor.execute("SELECT Card_id, password, type, Number, Expired, status, Account_id FROM Card WHERE Card_id = ?", (card_id,))
    card_info = cursor.fetchone()

    if card_info:
        # Define the column names
        columns = ["Card_id", "password", "type", "Number", "Expired", "status", "Account_id"]

        # Print the card information
        print("\nCard Information:")
        for column, value in zip(columns, card_info):
            print(f"{column}: {value}")
    else:
        print(f"No card found with Card_id {card_id}.")

    input("Press Enter to continue...")
    Card_Menue()

def Delete_Card():

    os.system('clear') 

    print("==================================================")
    print("                Delete Card Screen                ")
    print("==================================================")

    # Get the Card ID from user input
    card_id = input("Enter Card ID to delete: ")

    # Check if the card exists
    cursor.execute("SELECT * FROM Card WHERE Card_id = ?", (card_id,))
    existing_card = cursor.fetchone()

    if existing_card:
        # Delete the card
        cursor.execute("DELETE FROM Card WHERE Card_id = ?", (card_id))
        conn.commit()
        print(f"Card with Card_id {card_id} deleted successfully.")
    else:
        print(f"No card found with Card_id {card_id}.")

    input("Press Enter to continue...")
    Card_Menue()


def Update_Card():

    os.system('clear') 

    print("==================================================")
    print("                Update Card Screen                ")
    print("==================================================")

    card_id = input("Enter Card ID: ")

    cursor.execute("SELECT * FROM Card WHERE Card_id = ?", (card_id))
    existing_card = cursor.fetchone()

    if not existing_card:
        print(f"Card with Card_id {card_id} is not found.")
    else:
        updates = {}

        if input("Do you want to update Password? (yes/no): ").lower() == 'yes':
            updates['password'] = input("Enter Password: ")

        if input("Do you want to update Card Type? (yes/no): ").lower() == 'yes':
            updates['type'] = input("Enter Card Type: ")

        if input("Do you want to update Card Number? (yes/no): ").lower() == 'yes':
            updates['Number'] = input("Enter Card Number: ")

        if input("Do you want to update Expiry Date? (yes/no): ").lower() == 'yes':
            updates['Expired'] = input("Enter Expiry Date (YYYY-MM-DD): ")

        if input("Do you want to update Status? (yes/no): ").lower() == 'yes':
            updates['status'] = input("Enter Status: ")

        if input("Do you want to update Account ID? (yes/no): ").lower() == 'yes':
            while True:
                account_id = input("Enter the Account ID: ")
                if customer_exists(account_id):
                    updates['Account_id'] = account_id
                    break
                else:
                    print("Account is not found, enter another one ")

        if updates:
            set_clause = ', '.join([f"{key} = ?" for key in updates.keys()])
            values = list(updates.values())
            values.append(card_id)

            cursor.execute(f'''
            UPDATE Card
            SET {set_clause}
            WHERE Card_id = ?
            ''', values)

            conn.commit()
            print("Card Info Updated Successfully.")
        else:
            print("No updates were made.")

    
    input("Press Enter to continue...")
    Card_Menue()




   

##########################################################################################
#                                        Login Menue                                     #
##########################################################################################


def check_employee_login(username, password):
    cursor.execute("{CALL CheckUserCredentials (?, ?)}", (username, password))
    result = cursor.fetchone()

    # Check the result and return the appropriate boolean value
    if result and result[0] == 1:
        return True
    else:
        return False

def show_main_menu():

        os.system('clear') 
   
        print("===========================================")
        print("                 Main Screen               ")
        print("===========================================")
        print("\t[1] Customer Menue.")
        print("\t[2] Employee Menue.")
        print("\t[3] Branch Menue.")
        print("\t[4] Account Menue.")
        print("\t[5] Transaction Menue.")
        print("\t[6] Loan Menue.")
        print("\t[7] Card Menue.")
        print("\t[8] Logout.")
        print("===========================================")

       
        menu_option = get_user_input() 
        perform_main_menu_option(menu_option) 
        

def get_user_input():

    try:
        return int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_input()  # Recursive call for invalid input


def perform_main_menu_option(menu_option):

    os.system('clear') 
    if menu_option == 1:
        Customer_Menue()
    elif menu_option == 2:
        Employee_Menue()
    elif menu_option == 3:
        Branch_Menue()
    elif menu_option == 4:
        Account_Menue()
    elif menu_option == 5:
        Transaction_Menue()
    elif menu_option == 6:
        Loan_Menue()
    elif menu_option == 7:
        Card_Menue()
    elif menu_option == 8:
        Login()
  


def Login():

    login_attempts = 3

    while login_attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if check_employee_login(username, password):
            print("Login successful.")
            show_main_menu();
            break
        else:
            login_attempts -= 1
            print(f"Invalid username or password. {login_attempts} attempts remaining.")

    if login_attempts == 0:
        print("You are locked out.")



##########################################################################################
##########################################################################################



#Here is the start
Login() 






# Close the cursor and connection
cursor.close()
conn.close()

