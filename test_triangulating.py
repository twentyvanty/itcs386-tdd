def test_multiplication_by_two(): 
 flour = Quantity(200) 
 flour.times(2) 
 assert flour.amount == 400 
