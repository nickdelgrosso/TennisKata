Feature: Tennis Scoring System


    Scenario Outline: Score Names are Correct when points are different
        Given you have <yourPoints> point and your opponent has <oppPoints> points
        Then the score is <score>
        
        Examples:
        
        | yourPoints | oppPoints | score |
        | 1          | 1         | 15 - 15 |
        | 1          | 2         | 15 - 30 |
        | 3          | 2         | 40 - 30 |
        | 0          | 3         | love - 40 |
        | 0          | 0         | love - love |

    # Scenario:
    #     Given you have 40
    #     When you win a point
    #     Then you win the game

    # Scenario:
    #     Given you have 40 and your opponent has 40
    #     Then the score is "deuce".


    # Scenario:
    #     Given the game is in deuce
    #     When you win a point
    #     Then you have advantage

    # Scenario:
    #     Given you have advantage
    #     When you win a point
    #     Then you win the game

    # Scenario:
    #     Given you have advantage
    #     When your opponent wins a point
    #     Then the score is "deuce"

