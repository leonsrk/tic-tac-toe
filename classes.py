from loggerconfig import logger
import random


class Cell():

    def __init__(self, pos, num: int) -> None:
        self.pos = pos
        self.taken = "f"  # taken = f: free; p: player; e: enemy
        self.num = num

    def __repr__(self) -> str:
        return str(self.num)

    def __str__(self) -> str:
        return str(self.num)


class Game():

    def checkWin(self, ownCells: list[Cell]) -> bool:
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
        return False


class Player():

    def __init__(self, move: bool = False) -> None:
        self.move = move
        self.cells: list[Cell] = []
        self.id = "p"
        self.win = False


class Enemy(Game):

    def __init__(self) -> None:
        self.cells: list[Cell] = []
        self.id = "e"
        self.win = False

    def enemyMove(self, allCells: list[Cell]):
        return self.possibleMoves(allCells)

    def possibleMoves(self, allCells: list[Cell]):
        """returns a list with all the possible moves for the next turn
        Args:
            allCells (list): list with all cells, contains objects of Cell
        """
        posMoves = []
        for cell in allCells:
            if cell.taken == "f":
                posMoves.append(cell)
        logger.debug(f'posMoves: {posMoves}')
        return self.possibleWin(posMoves, allCells)

    def possibleWin(self, posMoves: list[Cell], allCells: list[Cell]) -> Cell:
        copy = self.cells
        for move in posMoves:
            copy.append(move)
            if self.checkWin(copy) is True:
                logger.debug(f'Winning enemy move: {move.num}')
                return move
            copy.pop((len(copy) - 1))
        return self.randomMove(posMoves)

    def randomMove(self, posMoves: list[Cell]):
        return random.choice(posMoves)
