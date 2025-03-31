class player():

    def __init__(self, id: str) -> None:
        self.id = id
        self.score = 0
        self.move = False
        self.win = False


class field():

    def __init__(self, pos: tuple[int, int]) -> None:
        self.id = "f"
        self.pos = pos


class game():

    def __init__(self, row1: list[field], row2: list[field], row3: list[field]) -> None:
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
