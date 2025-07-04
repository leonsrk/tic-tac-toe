import pygame
import time
from classes import *
from loggerconfig import logger

pygame.init()
pygame.mixer.init()

# game settings
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

# colors and font
BLACK = (36, 36, 36)
WHITE = (255, 255, 255)

FONT_h1 = pygame.font.SysFont("Arial", 70)
FONT_h2 = pygame.font.SysFont("Arial", 40)

# sounds
winningSound = pygame.mixer.Sound("sounds/win.mp3")
losingSound = pygame.mixer.Sound("sounds/lose.mp3")
startSound = pygame.mixer.Sound("sounds/gamestart.mp3")
clickingSound = pygame.mixer.Sound("sounds/click.mp3")

# buttons
btn1_1 = Cell(pygame.Rect(105, 105, 190, 190), 1)
btn1_2 = Cell(pygame.Rect(305, 105, 190, 190), 2)
btn1_3 = Cell(pygame.Rect(505, 105, 190, 190), 3)

btn2_1 = Cell(pygame.Rect(105, 305, 190, 190), 4)
btn2_2 = Cell(pygame.Rect(305, 305, 190, 190), 5)
btn2_3 = Cell(pygame.Rect(505, 305, 190, 190), 6)

btn3_1 = Cell(pygame.Rect(105, 505, 190, 190), 7)
btn3_2 = Cell(pygame.Rect(305, 505, 190, 190), 8)
btn3_3 = Cell(pygame.Rect(505, 505, 190, 190), 9)

allBtns = [btn1_1, btn1_2, btn1_3, btn2_1, btn2_2, btn2_3, btn3_1, btn3_2, btn3_3]

# game objects
game = Game()
user = Player()
enemy = Enemy()
enemy.player = user


# functions
def startScreen():
    screen.fill(BLACK)
    headline = FONT_h1.render("TicTacToe", True, WHITE)
    headline_rect = headline.get_rect()
    headline_rect.center = (400, 200)

    playTxt = FONT_h2.render("Press ENTER to play", True, WHITE)
    playTxt_rect = playTxt.get_rect()
    playTxt_rect.center = (400, 350)

    screen.blit(playTxt, playTxt_rect)
    screen.blit(headline, headline_rect)

    pygame.display.flip()


def drawPlayer(button: Cell):
    center = button.pos.center
    radius = min(button.pos.width, button.pos.height) // 2 - 15
    pygame.draw.circle(screen, WHITE, center, radius, 10)
    pygame.display.flip()
    clickingSound.play()
    button.taken = "p"
    user.cells.append(button)
    logger.debug(f'userCells: {user.cells}')
    user.move = False
    if game.checkWin(user.cells) is True:
        endScreenWin()
    else:
        # enemy action after player move
        enemy.cells.append(enemy.enemyMove(allBtns))
        drawEnemy(enemy.cells[(len(enemy.cells) - 1)])


def drawEnemy(button: Cell):
    time.sleep(2)
    sPos1 = (button.pos.left + 15, button.pos.top + 15)
    ePos1 = (button.pos.left + button.pos.width - 15, button.pos.top + button.pos.height - 15)

    sPos2 = (button.pos.left + button.pos.width - 15, button.pos.top + 15)
    ePos2 = (button.pos.left + 15, button.pos.top + button.pos.height - 15)

    pygame.draw.line(screen, WHITE, sPos1, ePos1, 15)
    pygame.draw.line(screen, WHITE, sPos2, ePos2, 15)
    pygame.display.flip()
    clickingSound.play()
    button.taken = "e"

    if game.checkWin(enemy.cells) is True:
        endScreenLose()
    else:
        user.move = True


def gameScreen():
    screen.fill(BLACK)
    # lines
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(100, 300), end_pos=(700, 300), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(100, 500), end_pos=(700, 500), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(300, 100), end_pos=(300, 700), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(500, 100), end_pos=(500, 700), width=5)
    # buttons
    pygame.draw.rect(screen, BLACK, btn1_1.pos)
    pygame.draw.rect(screen, BLACK, btn1_2.pos)
    pygame.draw.rect(screen, BLACK, btn1_3.pos)
    pygame.draw.rect(screen, BLACK, btn2_1.pos)
    pygame.draw.rect(screen, BLACK, btn2_2.pos)
    pygame.draw.rect(screen, BLACK, btn2_3.pos)
    pygame.draw.rect(screen, BLACK, btn3_1.pos)
    pygame.draw.rect(screen, BLACK, btn3_2.pos)
    pygame.draw.rect(screen, BLACK, btn3_3.pos)

    pygame.display.flip()


def endScreenWin():
    screen.fill(BLACK)
    headline = FONT_h1.render("You won!", True, WHITE)
    headline_rect = headline.get_rect()
    headline_rect.center = (400, 400)
    screen.blit(headline, headline_rect)
    pygame.display.flip()
    winningSound.play()


def endScreenLose():
    screen.fill(BLACK)
    headline = FONT_h1.render("You lost!", True, WHITE)
    headline_rect = headline.get_rect()
    headline_rect.center = (400, 400)
    screen.blit(headline, headline_rect)
    pygame.display.flip()
    losingSound.play()


# main loop
running = True
startScreen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                gameScreen()
                startSound.play()
                user.move = True
        # mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            # move - player
            if user.move:
                if btn1_1.pos.collidepoint(event.pos) and btn1_1.taken == "f":
                    drawPlayer(btn1_1)
                if btn1_2.pos.collidepoint(event.pos) and btn1_2.taken == "f":
                    drawPlayer(btn1_2)
                if btn1_3.pos.collidepoint(event.pos) and btn1_3.taken == "f":
                    drawPlayer(btn1_3)
                if btn2_1.pos.collidepoint(event.pos) and btn2_1.taken == "f":
                    drawPlayer(btn2_1)
                if btn2_2.pos.collidepoint(event.pos) and btn2_2.taken == "f":
                    drawPlayer(btn2_2)
                if btn2_3.pos.collidepoint(event.pos) and btn2_3.taken == "f":
                    drawPlayer(btn2_3)
                if btn3_1.pos.collidepoint(event.pos) and btn3_1.taken == "f":
                    drawPlayer(btn3_1)
                if btn3_2.pos.collidepoint(event.pos) and btn3_2.taken == "f":
                    drawPlayer(btn3_2)
                if btn3_3.pos.collidepoint(event.pos) and btn3_3.taken == "f":
                    drawPlayer(btn3_3)


pygame.quit()
