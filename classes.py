class player():

    def __init__(self, id: str, score: int, win: bool) -> None:
        self.id = id
        self.score = score
        self.win = False


class field():

    def __init__(self, id: str, pos: (int)) -> None:
        self.id = "f"
        self.pos = pos
