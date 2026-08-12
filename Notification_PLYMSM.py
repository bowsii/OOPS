# Create notifiction as a class and subclasses as EMail , SMS, Whatsapp
#Every notification must implement send
#The main program should be able to send different notific types without changing its core logic
#extension requirement: add push Notific without modifying the existing notification implementations
class Notification:
    def send(self,msg):
        pass
class Email(Notification):
    def send(self,msg):
        print("Email Notification: ",msg)
class SMS(Notification):
    def send(self,msg):
        print("SMS Notification: ",msg)

class Whatsapp(Notification):
    def send(self,msg):
        print("Whatsapp Notification: ",msg)

def send_notific(notification,msg):
    notification.send(msg)

E=Email()
S=SMS()
W=Whatsapp()

send_notific(E,input("\nEnter the Email message:"))
send_notific(S,input("\nEnter the SMS message:"))
send_notific(W,input("\nEnter the Whatsapp message:"))