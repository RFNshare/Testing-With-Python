import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fix_demo_one(self):
        print("Test in fixtureDemo")

    def test_fix_demo_two(self):
        print("Test in fixtureDemo")

    def test_fix_demo_three(self):
        print("Test in fixtureDemo")