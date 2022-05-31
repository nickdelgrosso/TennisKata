Feature: Tennis Scoring System


    Scenario Outline: Score Names are Correct when points are different
        Given you have <yourPoints> points and your opponent has <oppPoints> points
        Then the score is <score>.
        
        Examples:
        | yourPoints | oppPoints | score |
        | 1          | 1         | 15 - 15 |
        | 1          | 2         | 15 - 30 |
        | 3          | 2         | 40 - 30 |
        | 0          | 3         | love - 40 |
        | 0          | 0         | love - love |


    Scenario:  Winning by Two or More
        Given you have 3 points and your opponent has 0 points
        When you win a point
        Then you win the game

    Scenario:  Deuce on 40
        Given you have 3 points and your opponent has 3 points
        Then the score is deuce.


    Scenario: Advantage
        Given the game is in deuce
        When you win a point
        Then the score is P1 Advantage.

    Scenario:  Winning after Advantage
        Given you have advantage
        When you win a point
        Then you win the game

    # Scenario:
    #     Given you have advantage
    #     When your opponent wins a point
    #     Then the score is "deuce"

