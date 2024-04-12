from is_prime import is_prime

def test_1_is_not_prime():
    assert not is_prime(1)

def test_2_is_prime():
    assert is_prime(2)

def test_3_is_prime():
    assert is_prime(3)

def test_4_is_not_prime():
    assert not is_prime(4)

def test_5_is_prime():
    assert is_prime(5)

def test_991_is_prime():
    assert is_prime(991)

def test_993_is_not_prime():
    assert not is_prime(993)

def test_7873_is_prime():
    assert is_prime(7873)

def test_7909_is_not_prime():
    assert not is_prime(7909)

def test_7802143_is_not_prime():
    assert not is_prime(7802143)

def test_7802143_is_not_prime():
    assert not is_prime(7802143)
