class Stock:
  def __init__(self, price):
    self.price = price
    self.holdings = 0.0
    self.fees = 10
  def __repr__(self):
    return "This stock has {} price, {} holdings and {} fees.".format(self.price, self.holdings, self.fees)
