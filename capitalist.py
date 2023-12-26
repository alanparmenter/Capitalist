from bank import Bank
from stock import Stock

feta = Stock("FETA")
farclays = Bank("Farclays Bank")
print("{} initial balance: {}".format(farclays.name, farclays.get_balance()))
feta.buy(310, farclays)
print("Feta holdings as balance after purchase: " + str(feta.get_balance()))
print("{} balance after purchase: {}".format(farclays.name, farclays.get_balance()))
feta.sell(300, farclays)
print("Feta holdings as balance after sale: " + str(feta.get_balance()))
print("{} balance after purchase: {}".format(farclays.name, farclays.get_balance()))
for year in range(10):
  input("Your {} balance is {} and the {} price is {}.\n\
Would you like to buy stock? (y/n) ".format(farclays.name, farclays.get_balance(), feta.name, feta.price))
  farclays.pay_interest()
  print("Year {} {} balance after interest paid: {:.2f}".format(year,farclays.name, farclays.get_balance()))