#create an abstract class or interface Payment
#implementing the creditcard payment,upi payment and cash payment
#each should implement pay(amount) i.e pass arguments
#Should interact without depending on internal payment process

class Payment:
    def __init__(self):
        pass
    def pay(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        print("Amount that is being paid: ",amount)
        print("The Credit Card Payment has been successfully implemented\n")
class UPIpayment(Payment):
    def pay(self,amount):
        print("Amount that is being paid: ",amount)
        print("The UPI payment that has been paid.\n")
class CashPayment(Payment):
    def pay(self,amount):
        print("Amount that is being paid:",amount)
        print("The Cash Payment has been successfully paid.\n")
CC=CreditCardPayment()
UPI=UPIpayment()
C=CashPayment()
CC.pay(10000)
UPI.pay(2000)
C.pay(500)