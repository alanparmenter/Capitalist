from bank import Bank
from stock import Stock

feta = Stock("FETA")
farclays = Bank("Farclays Bank")
print("{} initial balance: {}".format(farclays.name, farclays.get_balance()))
feta.buy(310, farclays)

print("{} balance after purchase: {}".format(farclays.name, farclays.get_balance()))
feta.sell(300, farclays)
print("Feta holdings as balance after sale: " + str(feta.get_balance()))
print("{} balance after purchase: {}".format(farclays.name, farclays.get_balance()))
for year in range(10):
  response = input("Your {} balance is {:.2f}\n\
Would you like to buy {} stock at price {}? (y/n) ".format(farclays.name, farclays.get_balance(), feta.name, feta.price))
  if response == "y":
    feta.buy(310, farclays)
  farclays.pay_interest()
 