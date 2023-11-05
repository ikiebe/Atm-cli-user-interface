import random

#comment
print("Welcome to FCMB  member account creation")
Dashboard1=print("welcome to FCMB dashboard what do you want to do Create account,Account Balance, Transfer ")
Dashboard2=input()
acc_balance= []
acc_balance2= acc_balance.append[1000]
                                 
acc_number2=random.randint(10**7,10**8-1)
acc_number3=str(acc_number2)
acc_number="210"+acc_number3

if Dashboard2=="Create Account":
    option = input("do you want to create an account (type yes or no)\n")
    type_of_acc=input("do you want a savings or current account\n")
    user_name= input('enter your name in the order First name, Middle name, Last name\n')
    user_dob=input('enter your date of birth in the order DD/MM/YYYY\n')
    while  option!= "yes":
        if type(user_name) != str :
            print("please enter a valid option")
        if type(type_of_acc) != "savings" or "current":
            print("enter a valid input")
        elif type(user_dob)!= int:
            print("please enter a valid input")
    print(f"welcome{user_name} to FCMB thanks for creating a {type_of_acc} account, you have been credited with {acc_balance2}#")
    print(f"your account number is {acc_number}")
elif Dashboard2=="Account Balance":
    print(f"you have {acc_balance2} available in your acount")
elif Dashboard2=="Transfer":
    type_of_bank=input("enter the name of bank you wanna send to\n")
    user_acc=input("enter the account number you want to send to\n")
    amount=int(input("enter the amount you want to send\n"))
    left=int(acc_balance2[0])-amount
    print(f"you have successfully transfered {amount} to user{user_acc} of {type_of_bank} ")
    print(f"you have {left} remaining in your account")
