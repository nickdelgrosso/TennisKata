


def calc_score(p1: int, p2: int) -> str: 
    score_name = {0: "love", 1: "15", 2: "30", 3: "40"}
    p1_score = score_name[p1]
    p2_score = score_name[p2]
    return f"{p1_score} - {p2_score}"