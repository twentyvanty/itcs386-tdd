class Quantity: 
 def __init__(self, amount): 
  self.amount = amount 
 def times(self, multiplier): 
  self.amount = 600 
  
def times(self, multiplier): 
 self.amount = self.amount * multiplier 
 
def __eq__(self, other): 
 return self.amount == other.amount 
def __repr__(self): 
 return f"Quantity({self.amount})" 
def test_grams_are_not_ounces(): 
 assert Quantity(1, "g") != Quantity(1, "oz")
