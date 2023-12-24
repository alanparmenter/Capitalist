from bank import Bank
from stock import Stock

feta = Stock(300)
farclays = Bank(10000)
print("Farclays initial balance: " + str(farclays.get_balance()))
feta.buy(310, farclays)
print("Feta holdings as balance after purchase: " + str(feta.get_balance()))
print("Farclays balance after purchase: " + str(farclays.get_balance()))
feta.sell(300, farclays)
print("Feta holdings as balance after sale: " + str(feta.get_balance()))
print("Farclays balance after purchase: " + str(farclays.get_balance()))
