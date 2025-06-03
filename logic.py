import classes


def win(ownCells: list[classes.Cell]) -> bool:
    combinations = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9],
                    [3, 5, 7],
                    [1, 5, 9]
                    ]
    for combination in combinations:
        for cell in combination:
            pass  # TODO


# -------------------- enemy logic -----------------------

enemyCells: list[classes.Cell] = []


def possibleMoves(allMoves: list[classes.Cell]):
    """returns a list with all the possible moves for the next turn
    Args:
        allMoves (list): list with all moves, contains objects of Cell
    """
    posMoves = []
    for i in allMoves:
        if i.taken == "f":
            posMoves.append(i)
    print("posMoves:", posMoves)  # -------------------------------DEBUG
    possibleWin(posMoves, enemyCells)


def possibleWin(posMoves: list[classes.Cell], ownCells: list[classes.Cell]):
    pass  # TODO
