class player():

    def __init__(self, id: str) -> None:
        self.id = id
        self.move = False
        self.win = False


class cell():

    def __init__(self, pos, taken: str, num: int) -> None:    # taken = f: free; p: player; e: enemy
        self.pos = pos
        self.taken = taken
        self.num = num
