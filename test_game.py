from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse
import pytest
from types import SimpleNamespace

from game import Game

@pytest.fixture
def names():
    return SimpleNamespace()
    

scenarios(".")


@given(
    parse("you have {p1:d} points and your opponent has {p2:d} points")
)
def stepdef(p1, p2, names):
    names.game = Game(p1=p1, p2=p2)


@given("the game is in deuce")   
def stepdef(names):
    names.game = Game(p1=3, p2=3)

@then(
    parse("the score is {score}.")
)
def stepdef(score: str, names):
    assert names.game.score == score


@when("you win a point")
def stepdef(names):
    names.game.score_p1()


@then("you win the game")
def stepdef(names):
    assert names.game.score == "P1 Wins"
