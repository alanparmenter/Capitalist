import random
from bank import Bank
from stock import Stock

print("\n*************************************\nWelcome to Capitalist!\nWin the game by doubling your money…\nLose the game by going bankrupt…\n*************************************\n")
feta = Stock("FETA")
farclays = Bank("Farclays Bank")
print("To get you started, Farclays Bank have loaned you 10000, to buy FETA stock with.\nYou will have ten turns to buy or sell integer units of stock.\nYou cannot borrow more money from the bank.\nYou will get 5% interest on deposits\nThe bank will get 5% interest on their loan\nThere are fees of 10 on every transaction.\nEverything is liquidated at the end of the game.")

for year in range(10):
  print("\n")
  buy_response = input("Your {} balance is {:.2f}\n\
Would you like to buy {} stock at price {:.0f}? (units) ".format(farclays.name, farclays.get_balance(), feta.name, feta.price))
  feta.buy(int(buy_response), farclays)
  sell_response = input("Your {} balance is {:.2f}\n\
Would you like to sell {} stock at price {:.0f}? (units) ".format(farclays.name, farclays.get_balance(), feta.name, feta.price))
  feta.sell(int(sell_response), farclays)

  farclays.pay_interest()
  feta.price *= 0.75+random.randint(0,5)/10

print("\n**********\nGame Over!\n**********\n")
loan = 10000*(1+farclays.interest_rate)**10
total = farclays.get_balance() + feta.get_balance()
if feta.get_balance() > 0:
  total -= feta.fees
if total >= 20000:
  print("{:.2f} total wins the game!\n".format(total))
elif total >= loan:
  print("{:.2f} total gains some profit to put towards your pension.\nThe bank take back {:.2f} but you get to keep {:.2f}\nYou may not have won the game but you have increased the security of your future.\n".format(total, loan, total-loan))
else:
  print("{:.2f} total assets on liquidation.\nYour {:.2f} debt to the bank unfortunately exceeds this.\nYou have no choice but to declare bankruptcy.\n".format(total, loan))
