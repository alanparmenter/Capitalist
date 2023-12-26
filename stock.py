class Stock:
  def __init__(self, name):
    self.name = name
    self.price = 300
    self.holdings = 0.0
    self.fees = 10
  def __repr__(self):
    return "This stock has {} price, {} holdings and {} fees".format(self.price, self.holdings, self.fees)
  def buy(self, amount, bank):
    if (amount*self.price-self.fees) > bank.get_balance():
      print("Transaction failed due to insufficient funds\n")
    elif amount == 0:
      pass
    else:
      self.holdings += amount
      bank.withdraw(amount*self.price+self.fees)
      print("{} holdings as balance after purchase: {:.2f}".format(self.name, self.get_balance()))
  def sell(self, amount, bank):
    if amount <= self.holdings:
      self.holdings -= amount
      bank.deposit(amount*self.price-self.fees)
    elif amount == 0:
      pass
    else:
      print("Transaction failed due to insufficient stock\n")
  def get_balance(self):
    return self.holdings * self.price