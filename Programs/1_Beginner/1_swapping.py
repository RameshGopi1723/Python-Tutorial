import pytest

#swapping function 
def swapper(a, b):
    temp = a #temp variable approach
    a = b
    b = temp
    # a, b = b, a  #direct swap approact
    return a, b


a = 5
b = 10

print("Before swapping: a =", a, "b =", b, end = "\n\n")
a, b = swapper(a,b)
print("After swapping: a =", a, "b =", b)


#test cases using pytest
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, (2, 1)),
    ('x', 'y', ('y', 'x')),
    ([1], [2], ([2], [1])),
    (None, True, (True, None)),
])

def test_swapper_multiple(a, b, expected):
    assert swapper(a, b) == expected
