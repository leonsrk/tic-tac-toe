import classes
import random
from loggerconfig import logger


def win(ownCells: list[classes.Cell]) -> bool:
    """returns True if a winning move was made
    Args:
        ownCells (list): list with all the current cells of the player or the enemy
    Return:
        bool
    """
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
        identical = 0
        for cell in combination:
            for ownCell in ownCells:
                if ownCell.num == cell:
                    identical += 1
            if identical == 3:
                logger.debug(f'Return value of win(): {True}')
                return True
    logger.debug(f'Return value of win(): {False}')
    return False


# -------------------- enemy logic -----------------------

def startEnemy(allMoves: list[classes.Cell], enemyCells: list[classes.Cell] = []):
    return possibleMoves(allMoves, enemyCells)


def possibleMoves(allMoves: list[classes.Cell], enemyCells: list[classes.Cell] = []):
    """returns a list with all the possible moves for the next turn
    Args:
        allMoves (list): list with all moves, contains objects of Cell
    """
    posMoves = []
    for i in allMoves:
        if i.taken == "f":
            posMoves.append(i)
    logger.debug(f'posMoves: {posMoves}')
    return possibleWin(posMoves, allMoves, enemyCells)


def possibleWin(posMoves: list[classes.Cell], allMoves: list[classes.Cell], ownCells: list[classes.Cell]) -> classes.Cell:
    copy = ownCells
    for move in posMoves:
        copy.append(move)
        if win(copy) is True:
            logger.debug(f'Winning enemy move: {move.num}')
            return move
        copy.pop((len(copy) - 1))
    return randomMove(posMoves)


def randomMove(posMoves: list[classes.Cell]):
    return random.choice(posMoves)
