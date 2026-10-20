# test_leap.py 
from leap import is_leap 
def test_2024_is_a_leap_year(): 
 assert is_leap(2024) 
def test_1900_is_a_leap_year(): 
 assert is_leap(1900) 
import pytest 
@pytest.mark.parametrize("year, expected", [ 
 (2000, True), # divisible by 400 
 (1900, False), # divisible by 100 but not by 400 
 (2024, True), # divisible by 4 but not by 100 
 (2023, False), # not divisible by 4 
]) 
def test_is_leap(year, expected): 
 assert is_leap(year) == expected 
 (2400, True),  # Block 1: divisible by 400
 (2100, False), # Block 2: divisible by 100 but not by 400
