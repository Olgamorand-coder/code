
class Account:
    #list_of_cards=[]
    def __init__(self, number, pin):
        self.number=number
        self.pin=pin
        self.balance=0
    def charge(self, value):
        self.balance+=value
