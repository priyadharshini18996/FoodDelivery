balance=2000.32
print("  welcome to No.1 ATM  ")
print("""
1)Balance
2)Withdraw
3)Deposit
4)Quit
""")
Option=int(input("Enter Option: "))
if Option==1:
    print "Balance:",balance

if Option==2:
    print "Balance : ",balance
    Withdraw=float(input("Enter Withdraw amount : "))
    if Withdraw>0:
        currentbalance=(balance-Withdraw)
        print "current Balance  : ",currentbalance
    elif Withdraw>balance:
        print "insufficient balance"
    else:
        print "None withdraw made"

if Option==3:
    print "Balance : ",balance
    Deposit=float(input("Enter deposit amount : "))
    if Deposit>0:
        currentbalance=(balance+Deposit)
        print "currentbalance :",currentbalance
    else:
        print "None deposit made"


if Option==4:
    exit()








