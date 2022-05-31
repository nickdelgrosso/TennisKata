from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse
import pytest
from types import SimpleNamespace

from game import calc_score

@pytest.fixture
def names():
    return SimpleNamespace()
    

scenarios("tennis.feature")


@given(
    parse("you have {p1:d} point and your opponent has {p2:d} points")
)
def stepdef(p1, p2, names):
    assert isinstance(p1, int) and isinstance(p2, int)
    names.p1 = p1
    names.p2 = p2
    


@then(
    parse("the score is {score}")
)
def stepdef(score: str, names):
    observed = calc_score(p1=names.p1, p2=names.p2)
    assert observed == score