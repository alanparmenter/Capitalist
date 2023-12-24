class Bank:
  def __init__(self, initial_deposit):
    self.name = "Anonymous Bank"
    self.cash = initial_deposit
    self.interest_rate = 0
  def __repr__(self):
    return "This bank named {} has {} cash and an interest rate of {}".format(self.name, self.cash, self.interest_rate)
  def deposit(self, deposit_amount):
    self.cash += deposit_amount
  def withdraw(self, withdrawal_amount):
    self.cash -= withdrawal_amount
  def get_balance(self):
    return self.cash
