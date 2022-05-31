from dataclasses import dataclass, field


@dataclass
class Game:
    p1: int
    p2: int

    @property
    def score(self) -> str:
        return calc_score(p1=self.p1, p2=self.p2)

    def score_p1(self) -> None:
        if self.p1 == 3 and self.p2 == 4:
            self.p2 -= 1
        else:
            self.p1 += 1

    def score_p2(self) -> None:
        if self.p1 == 4 and self.p2 == 3:
            self.p1 -= 1
        else:
            self.p2 += 1

    


def calc_score(p1: int, p2: int) -> str:
    special_scores = {
        (3, 3): "deuce",
        (4, 3): "P1 Advantage",
        (3, 4): "P2 Advantage",
    }
    score = special_scores.get((p1, p2))
    if score is not None:
        return score

    if p1 >= 4:
        return "P1 Wins"
    if p2 >= 4:
        return "P2 Wins"

    score_name = {0: "love", 1: "15", 2: "30", 3: "40"}
    p1_score = score_name[p1]
    p2_score = score_name[p2]
    return f"{p1_score} - {p2_score}"


