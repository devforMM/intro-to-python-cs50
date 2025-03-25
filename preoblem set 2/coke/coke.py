bottle_price=50
coins=[25,10,5]
costumer_money=0
amount_due=bottle_price
while True:
 print(f"Amount Due: {amount_due}")
 coin=int(input("insert a coin "))
 if coin in coins:

  costumer_money+=coin
  amount_due-=coin
  if amount_due<=0:
   break

change_owed=costumer_money-bottle_price
print(f"Change Owed: {change_owed}")
