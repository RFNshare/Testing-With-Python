import pytest


@pytest.mark.xfail
def test_third_program():
    msg = "Hello"
    print("Skip but not skipped")
    assert msg == "Hi", "Test Failed Because strings do not match"


@pytest.mark.smoke
@pytest.mark.skip
def test_fourth_program_debit_card():
    a = 2
    b = 6
    assert a + 2 == 6, "Summation is not working"
