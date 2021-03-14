import sqlite3
from Account import Account

conn = sqlite3.connect('accounts.s3db')
c=conn.cursor()
#c.execute("""CREATE TABLE cards (
 #           number TEXT,
  #          pin TEXT,
   #        balance INTEGER
    #        ) """)
def insert_card(card):
    with conn:
        c.execute("INSERT INTO cards Values(:card_number, :pin, :balance)",{'card_number': card.number, 'pin': card.pin, 'balance': card.balance})
def get_balance_by_num(number):
    c.execute("Select balance FROM cards WHERE number=?", (number,))
    return c.fetchone()[0]
def deposit(card, money):
    new_bal=card.balance+money
    with conn:
        c.execute("""UPDATE cards SET balance=:balance
        WHERE number=:number AND pin=:pin""",
                  {'balance':new_bal, 'number':card.number, 'pin':card.pin})
    card.charge(money)

def remove_card(card):
    with conn:
        c.execute("""Delete from cards WHERE number=:number AND pin=:pin""",
                  {'number':card.number, 'pin':card.pin})

acc1=Account('789', '789')
acc2=Account('098', '000')
acc3=Account('123', '123')
#insert_card(acc3)
#insert_card(acc2)
#cards=get_balance_by_num('789')
#print(cards)
deposit(acc2, 200)
balance=get_balance_by_num('789')
print(balance)
conn.close()