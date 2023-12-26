import random
from bank import Bank
from stock import Stock

print("*************************************\nWelcome to Capitalist!\nWin the game by doubling your money…\nLose the game by going bankrupt…\n*************************************\n")
feta = Stock("FETA")
farclays = Bank("Farclays Bank")
print("To get you started, we have opened a Farclays Bank account with a balance of 10000, to buy FETA stock with. You will have ten turns to buy or sell integer units of stock. You cannot borrow money from the bank.\n")

for year in range(10):
  response = input("Your {} balance is {:.2f}\n\
Would you like to buy {} stock at price {:.0f}? (units) ".format(farclays.name, farclays.get_balance(), feta.name, feta.price))
  feta.buy(int(response) * 310, farclays)
  farclays.pay_interest()
  feta.price *= 0.75+random.randint(0,5)/10

total = farclays.get_balance() + feta.get_balance()
if total >= 20000:
  print(total + " total wins the game!\n")
elif total >= 10000:
  print(total + " total gains some profit to put towards your pension. Try again with 10000?\n")
else:
  print(total + " total exceeds your debts so you have no choice but to declare bankruptcy\n")

print("**********\nGame Over!\n**********\n")