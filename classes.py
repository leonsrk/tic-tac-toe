class Player():

    def __init__(self, id: str, move: bool = False) -> None:
        self.id = id
        self.move = move
        self.win = False


class Cell():

    def __init__(self, pos, taken: str, num: int) -> None:    # taken = f: free; p: player; e: enemy
        self.pos = pos
        self.taken = taken
        self.num = num

    def __repr__(self) -> str:
        return str(self.num)

    def __str__(self) -> str:
        return str(self.num)
