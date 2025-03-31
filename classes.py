class player():

    def __init__(self, id: str, score: int, win: bool) -> None:
        self.id = id
        self.score = score
        self.win = False


class field():

    def __init__(self, id: str, pos: tuple[int, int]) -> None:
        self.id = "f"
        self.pos = pos


class game():

    def __init__(self, row1: list[str], row2: list[str], row3: list[str]) -> None:
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
