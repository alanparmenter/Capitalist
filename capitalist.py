class Stock:
  def __init__(self, price):
    self.price = price
    self.holdings = 0.0
    self.fees = 10
  def __repr__(self):
    return "This stock has {} price, {} holdings and {} fees.".format(self.price, self.holdings, self.fees)
  def buy(self, amount, bank):
    self.holdings += (amount - self.fees) / self.price
    band.withdraw(amount)
  def sell(self, amount, bank):
    self.holdings -= amount / self.price
    bank.deposit(amount - self.fees)
  def get_balance(self):
    return self.holdings * self.price
