import pytest


def test_one_plus_one():
    assert 1+1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
    

def test_dev_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

#multiplication test ideas

# two positiv integers
# identity: multiplyting any number by 1
# zero: mult any number by 0
# pos by neg
# neg by neg
# multiply floats

def test_multiply_2_pos():
    assert 2 * 3 == 6

def test_mult_identity():
    assert 1 * 99 == 99

def test_mult_zero():
    assert 0 * 100 == 0


# A parametrized test function

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product








