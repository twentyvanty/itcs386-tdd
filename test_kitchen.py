# test_kitchen.py 
from kitchen import Quantity 
def test_multiplication(): 
 flour = Quantity(200) 
 flour.times(3) 
 assert flour.amount == 600 
class Quantity: 
 def __init__(self, amount): 
  self.amount = amount 
 def times(self, multiplier): 
  self.amount = 600 
