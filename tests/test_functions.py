import pytest 
import time 
import functions.my_functions as my_functions

def test_add():
    result = my_functions.add(4,5)
    assert result == 9

def test_divide():
    result = my_functions.divide(15,5)
    assert result == 3

 

@pytest.mark.slow 
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(15,5)
    assert result == 3

@pytest.mark.skip(reason="This feature is currently broken ")
def test_add():
    assert my_functions.add(1,2)==3

@pytest.mark.xfail(reason="we know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(3,0)



