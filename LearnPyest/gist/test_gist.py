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


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"


@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")


def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")


@pytest.mark.parametrize(
    "company_name",
    ["TikTok", "Instagram", "Twitch"],
    ids=["TICKTOK TEST", "INSTA TEST", "TWITCH TEST"]
)
def test_params(company_name: str) -> None:
    print(f"\nTest With {company_name}")


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)
