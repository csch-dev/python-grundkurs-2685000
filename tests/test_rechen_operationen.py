from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier

def test_erhoehe_um_zwei():
    assert erhoehe_um_zwei(3) == 5
    assert erhoehe_um_zwei(-1) == 1
    assert erhoehe_um_zwei(0) == 2  

def test_multipliziere_mit_drei():
    assert multipliziere_mit_drei(3) == 9
    assert multipliziere_mit_drei(-1) == -3
    assert multipliziere_mit_drei(0) == 0

def test_subtrahiere_zehn():
    assert subtrahiere_zehn(15) == 5
    assert subtrahiere_zehn(10) == 0
    assert subtrahiere_zehn(5) == -5

def test_teile_durch_vier():
    assert teile_durch_vier(8) == 2
    assert teile_durch_vier(12) == 3
    assert teile_durch_vier(0) == 0

    try:
        teile_durch_vier(5)
        assert False, "Expected ValueError for non-divisible by 4"
    except ValueError:
        pass
