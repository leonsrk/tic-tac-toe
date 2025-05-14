import classes


def possibleMoves(allMoves: list[classes.Cell]) -> list:
    posMoves = []
    for i in allMoves:
        if i.taken == "f":
            posMoves.append(i)
    return posMoves
