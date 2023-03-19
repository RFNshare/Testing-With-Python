import pytest


@pytest.fixture()
def setup():
    print("Setup Processing...")
    yield
    print("Teardown ...")


def test_fix_demo(setup):
    print("Test in fixtureDemo")