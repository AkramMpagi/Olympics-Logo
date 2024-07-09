from main import multiply

def test_multiply():
    assert multiply(1, 1) == 1
    
def test_multiply_2():
    assert multiply(2, 2) == 4

def test_multiply_3():
    assert multiply(3, 3) == 9

def test_multiply_4():
    assert multiply(4, 4) == 16

def test_multiply_5():
    assert multiply(23, 45) == 1035
    




