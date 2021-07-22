class Atm(object):
    def __init__(user,pin,balance):
        user.pin  = pin
        user.balance = balance


    def cashWithdrawal(user):
        return(user.balance - withdraw)
        
kumail = Atm(1234,1000)
password = int(input("Enter your pin kumail: "))
if password == kumail.pin :
    withdraw = int(input("how much do you want to withdraw"))
    print("Your new balance is:",end="")
    print(kumail.cashWithdrawal())
else :
    print("incorrect password")
    



