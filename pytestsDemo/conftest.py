import pytest


@pytest.fixture(scope="class")
def setup():
    print("Setup Processing...")
    yield
    print("Teardown ...")