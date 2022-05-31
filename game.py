from dataclasses import dataclass, field


@dataclass
class Game:
    p1: int
    p2: int

    @property
    def score(self) -> str:
        return calc_score(p1=self.p1, p2=self.p2)

    def score_p1(self) -> None:
        self.p1 += 1

    def score_p2(self) -> None:
        self.p2 += 1

    


def calc_score(p1: int, p2: int) -> str:
    if p1 == 3 and p2 == 3:
        return "deuce"
    if p1 > 3:
        return "P1 Wins"
    if p2 > 3:
        return "P2 Wins"

    score_name = {0: "love", 1: "15", 2: "30", 3: "40"}
    p1_score = score_name[p1]
    p2_score = score_name[p2]
    return f"{p1_score} - {p2_score}"


