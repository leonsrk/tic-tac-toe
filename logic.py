import classes as c

gamefield = c.game(row1=[c.field(pos=(1, 1)), c.field(pos=(1, 2)), c.field(pos=(1, 3))],
                   row2=[c.field(pos=(2, 1)), c.field(pos=(2, 2)), c.field(pos=(2, 3))],
                   row3=[c.field(pos=(3, 1)), c.field(pos=(3, 2)), c.field(pos=(3, 3))])

user = c.player(id="x")
computer = c.player(id="o")


def test():
    for row in [gamefield.row1, gamefield.row2, gamefield.row3]:
        print([field.id for field in row])


test()
