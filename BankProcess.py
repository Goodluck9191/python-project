print('Hello welcome to GPM Bank')

def services():
    print('Please enter the service do you want')
    print('1.Check balance ')
    print('2.Deposit Money ')
    print('3.Withdraw Money')
    selection = input()
    return selection

customersPin = [12, 4, 1234,654,25]

selection = services()






if not selection: 
    print('You do not select any services PLease try again')
    services()



if selection:
    if(selection =='1'):
        pin = input('Please enter your PIN ')
        for i in range(len(customersPin)):
            if (pin == customersPin[i]):
                print('Your balance is 5000')
            else:
                print('You enter the incorrect Password')



