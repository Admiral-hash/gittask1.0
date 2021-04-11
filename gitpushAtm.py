print('WELCOME TO ABC BANK')
accounts={
    'user':['CYRIL','BEN','TOM','RAPH','DAN'],
    'pin':['1234','2345','5678','0978','3245'],
    'balance':['2300','300','123','500','400'],
    'complain':['']
    }
users=accounts['user']
pins=accounts['pin']
balances=accounts['balance']
complains=accounts['complain']
print('DO YOU HAVE AN ACCOUNT WITH US; YES(1) OR NO(2)')
option=int(input('SELECT AN OPTION:\n'))
if option==1:
    def login():
        print('<<<<<LOGIN>>>>>')
        name=input('ENTER YOUR NAME:\n')
        if name in users:
            pin=input('ENTER YOUR PIN:\n')
            userid=users.index(name)
            if pin==pins[userid]:
                print('WELCOME %s' %name)
                print('SELECT THE TRANSACTION YOU WANT TO PERFORM')
                print('1. Cash Withdrawal')
                print('2. Deposit')
                print('3. Change pin')
                print('4. Complaint')
                print('5. Logout')
                selected_option=int(input('PLEASE SELECT AN OPTION:\n'))
                if selected_option==1:
                    def Withdrawal():
                        amount=int(input('HOW MUCH DO YOU WANT TO WITHDRAW:\n'))
                        userbalance=users.index(name)
                        if amount<=int(balances[userbalance]):
                            print('TAKE YOUR CASH!')
                        else:
                            print('YOU DO NOT HAVE ENOUGH CASH TO COMPLETE THE TRANSACTION')
                    Withdrawal()
                elif selected_option==2:
                    def Deposit():
                        amount=int(input('HOW MUCH DO YOU WANT TO DEPOSIT:\n'))
                        userbalance=users.index(name)
                        balance=int(balances[userbalance])
                        balance=balance+amount
                        print("YOU DEPOSITED " + str(amount))
                        print(' YOUR NEW BALANCE IS ' + str(balance))
                    Deposit()
                elif selected_option==3:
                    def pin_change():
                        enter_pin=str(input('ENTER YOUR PIN TO CONTINUE:\n'))
                        if enter_pin==pin:
                            new_pin=str(input('ENTER YOUR NEW PIN:\n'))
                            confirm_pin=str(input('CONFIRM YOUR PIN:\n'))
                            if new_pin==confirm_pin:
                                user_pin=pins.index(pin)
                                pins.remove(pin)
                                pins.insert(user_pin,new_pin)
                            else:
                                print('PINS DO NOT MATCH,TRY AGAIN')
                        else:
                            print('PIN IS INCORRECT')
                    pin_change()
                elif selected_option==4:
                    def complaint():
                        complain=input('PLEASE WRITE OUT YOUR COMPLAINT:\n')
                        complains.append(complain)
                        print('THANKS FOR CONTACTING US,YOUR FEEDBACK WILL BE ADDRESSED AS SOON AS POSSIBLE')
                    complaint()
                elif selected_option==5:
                    print('CLICK THE LOGOUT BUTTON')
                else:
                    print('YOU CHOSE A WRONG OPTION')
                

            else:
                print('PIN NOT CORRECT')
        else:
            print('USER NOT FOUND')
    login()
if option==2:
    def register():
        print('<<<<<<<REGISTER>>>>>>')
        new_username=input('ENTER YOUR USERNAME:\n')
        new_pin=int(input('ENTER YOUR PIN:\n'))
        balance=0
        users.append(new_username)
        pins.append(new_pin)
        balances.append(balance)
        print('YOUR ACCOUNT HAS BEEN OPENED,LOGIN TO PERFORM TRANSACTIONS')
    register()