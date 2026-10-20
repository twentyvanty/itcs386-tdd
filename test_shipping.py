
import pytest
from shipping import shipping_fee


@pytest.mark.parametrize("weight, expected_fee", [
    (0.1, 40),   # Rule 2: below 1 kg
    (0.99, 40),  # Rule 2: just below 1 kg
    (1, 60),     # Rule 3: exactly 1 kg
    (2, 60),     # Rule 3: between 1 and 5 kg
    (5, 60),     # Rule 3: exactly 5 kg
    (5.2, 70),   # Rule 4: started kilogram above 5 kg
    (6, 70),     # Rule 4: exactly 1 kg above 5 kg
    (6.1, 80),   # Rule 4: started second kilogram above 5 kg
])
def test_shipping_fee(weight, expected_fee):
    assert shipping_fee(weight) == expected_fee


@pytest.mark.parametrize("weight", [
    0,    # Rule 1: zero weight is invalid
    -1,   # Rule 1: negative weight is invalid
])
def test_invalid_weight_raises_value_error(weight):
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(weight)
