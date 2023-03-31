import pytest


def test_first() -> None:
    assert 2 == 2


@pytest.mark.skip
def test_will_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="Skipped beacuse i want to")
def test_will_skipped_if() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_dont_care_fails() -> None:
    assert 2 == 2


@pytest.mark.slow
def test_with_custom_mark1() -> None:
    pass


@pytest.mark.slow
def test_with_custom_mark2() -> None:
    pass