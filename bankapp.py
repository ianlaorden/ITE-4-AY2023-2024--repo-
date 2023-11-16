class BankAccount:
    def __init__(self, account_number, pin, name, address, email, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.address = address
        self.email = email
        self.balance = balance

    def balance_inquiry(self):
        self.account_transaction(f'Balance Inquiry {self.balance}')
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.account_transaction(f'Deposit Amount: {amount}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.account_transaction(f'Witdrawal Amount: {amount}')
        else:
            print('Insufficient Balance!')

    def account_summary(self):
        filename = self.account_number + '_summary.txt'
        print(f'Account Number: {self.account_number}\nName: {self.name}\nAddress: {self.address}\nEmail: {self.email}\nBalance: {self.balance}\n\nAccount Transaction: \n')
        with open(filename, 'r') as file:
            content = file.read()
            print(content)

    def create_account(self, account_type):
        filename = account_type + 'Account.txt'
        content = self.account_number + ',' + self.pin + ',' + self.name + \
            ',' + self.address + ',' + self.email + \
            ',' + str(self.balance) + '\n'
        with open(filename, 'a') as file:
            file.write(content)

    def account_transaction(self, content):
        filename = self.account_number + '_summary.txt'
        with open(filename, 'a') as file:
            file.write(content + '\n')

    def update_balance(self, account_type):
        filename = account_type + 'Account.txt'
        self.newrecord = ''
        with open(filename, 'r') as file:
            content = file.readlines()
            for a in content:
                x = a.split(',')
                if len(x) > 1:
                    if x[0] == self.account_number:
                        x[5] = self.balance
                        self.newrecord += x[0] + ',' + x[1] + ',' + \
                            x[2] + ',' + x[3] + ',' + \
                            x[4] + ',' + str(x[5]) + '\n'
                    else:
                        self.newrecord += x[0] + ',' + x[1] + ',' + \
                            x[2] + ',' + x[3] + ',' + \
                            x[4] + ',' + str(x[5]) + '\n'

        with open(filename, 'w') as file:
            file.write(self.newrecord)


class PersonalAccount(BankAccount):
    def __init__(self, account_number, pin, name, address, email, balance=0):
        super().__init__(account_number, pin, name, address, email, balance)


class CompanyAccount(BankAccount):
    def __init__(self, account_number, pin, name, address, email, balance=0):
        super().__init__(account_number, pin, name, address, email, balance)


account_list = []


def update_list():
    try:
        with open('PersonalAccount.txt', 'r') as file:
            content = file.readlines()
            for a in content:
                x = a.split(',')
                if len(x) > 1:
                    account = PersonalAccount(
                        x[0], x[1], x[2], x[3], x[4], float(x[5]))
                    account_list.append(account)
    except FileNotFoundError:
        with open('PersonalAccount.txt', 'w') as file:
            file.write()
    except Exception as e:
        pass


def create_account(account_type):
    account_number = input('Enter Account Number: ')
    pin = input('Enter pin: ')
    name = input('Enter Name: ') if account_type == 'Personal' else input(
        'Enter Business Name: ')
    address = input('Enter Address: ')
    email = input('Enter Email: ')
    balance = float(input('Enter Balance: '))
    if account_type == 'Personal':
        account = PersonalAccount(
            account_number, pin, name, address, email, balance)
        account_list.append(account)
        account.create_account('Personal')
    elif account_type == 'Company':
        account = CompanyAccount(
            account_number, pin, name, address, email, balance)
        account_list.append(account)
        account.create_account('Company')


def check_account(account_list, accountNumber, pin):
    for account in account_list:
        if account.account_number == accountNumber and account.pin == pin:
            return account
    print('Account Not Found')
    return None


def perform_transactions(account_type):
    accountNumber = input('Enter Account Number: ')
    pin = input('Enter Pin: ')
    account = check_account(account_list, accountNumber, pin)
    if account:
        while True:
            print('\nPersonal Account Transaction:')
            print('a. Deposit')
            print('b. Withdraw')
            print('c. Balance Inquiry')
            print('d. Account Summary')
            print('e. Exit')
            option_t = input('Select an Option: ')
            if option_t.lower() == 'a':
                amount = float(input('Enter Deposit Amount: '))
                account.deposit(amount)
                account.update_balance(account_type)
            elif option_t.lower() == 'b':
                amount = float(input('Enter Withdrawal Amount: '))
                account.withdraw(amount)
                account.update_balance(account_type)
            elif option_t.lower() == 'c':
                print(f'Your available is Php {account.balance_inquiry()}')
            elif option_t.lower() == 'd':
                account.account_summary()
            elif option_t.lower() == 'e':
                break
            else:
                print('Select a Valid Option!')


def main():
    while True:
        print('''
    1. Create Personal Account
    2. Create Company Account
    3. Perform Transactions
    4. Exit''')
        option = input('\nSelect an Option: ')

        if option == '1':
            create_account('Personal')
            continue
        elif option == '2':
            create_account('Company')
            continue
        elif option == '3':
            while True:
                print('\n1. Personal Account\n2. Company Account\n3. Exit')
                account_type = input('Select an Option: ')
                if account_type == '1':
                    perform_transactions('Personal')
                    continue
                elif account_type == '2':
                    perform_transactions('Company')
                    continue
                elif account_type == '3':
                    break
                else:
                    print('\nEnter a valid number!\n')
                    continue
        elif option == '4':
            print('Thank you!')
            break
        else:
            print('Enter a valid number!')


update_list()
main()
