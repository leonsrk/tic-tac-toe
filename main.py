import pygame
import classes

pygame.init()

# game settings
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

# colors and font
BLACK = (36, 36, 36)
WHITE = (255, 255, 255)

FONT_h1 = pygame.font.SysFont("Arial", 70)
FONT_h2 = pygame.font.SysFont("Arial", 40)

# buttons
btn1_1 = pygame.Rect(105, 105, 190, 190)
btn1_2 = pygame.Rect(305, 105, 190, 190)
btn1_3 = pygame.Rect(505, 105, 190, 190)

btn2_1 = pygame.Rect(105, 305, 190, 190)
btn2_2 = pygame.Rect(305, 305, 190, 190)
btn2_3 = pygame.Rect(505, 305, 190, 190)

btn3_1 = pygame.Rect(105, 505, 190, 190)
btn3_2 = pygame.Rect(305, 505, 190, 190)
btn3_3 = pygame.Rect(505, 505, 190, 190)

# player
user = classes.player("o")
enemy = classes.player("x")


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


def drawPlayer(button):
    center = button.center
    radius = min(button.width, button.height) // 2 - 15
    pygame.draw.circle(screen, WHITE, center, radius, 10)
    pygame.display.flip()


def drawEnemy(button):
    sPos1 = (button.left + 15, button.top + 15)
    ePos1 = (button.left + button.width - 15, button.top + button.height - 15)

    sPos2 = (button.left + button.width - 15, button.top + 15)
    ePos2 = (button.left + 15, button.top + button.height - 15)

    pygame.draw.line(screen, WHITE, sPos1, ePos1, 15)
    pygame.draw.line(screen, WHITE, sPos2, ePos2, 15)
    pygame.display.flip()


def gameScreen():
    screen.fill(BLACK)
    # lines
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(100, 300), end_pos=(700, 300), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(100, 500), end_pos=(700, 500), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(300, 100), end_pos=(300, 700), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(500, 100), end_pos=(500, 700), width=5)
    # buttons
    pygame.draw.rect(screen, BLACK, btn1_1)
    pygame.draw.rect(screen, BLACK, btn1_2)
    pygame.draw.rect(screen, BLACK, btn1_3)
    pygame.draw.rect(screen, BLACK, btn2_1)
    pygame.draw.rect(screen, BLACK, btn2_2)
    pygame.draw.rect(screen, BLACK, btn2_3)
    pygame.draw.rect(screen, BLACK, btn3_1)
    pygame.draw.rect(screen, BLACK, btn3_2)
    pygame.draw.rect(screen, BLACK, btn3_3)

    pygame.display.flip()


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
                user.move = True
        # mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            # move - player
            if user.move:
                if btn1_1.collidepoint(event.pos):
                    drawPlayer(btn1_1)
                    user.move = False
                if btn1_2.collidepoint(event.pos):
                    drawPlayer(btn1_2)
                    user.move = False
                if btn1_3.collidepoint(event.pos):
                    drawPlayer(btn1_3)
                    user.move = False
                if btn2_1.collidepoint(event.pos):
                    drawPlayer(btn2_1)
                    user.move = False
                if btn2_2.collidepoint(event.pos):
                    drawPlayer(btn2_2)
                    user.move = False
                if btn2_3.collidepoint(event.pos):
                    drawPlayer(btn2_3)
                    user.move = False
                if btn3_1.collidepoint(event.pos):
                    drawPlayer(btn3_1)
                    user.move = False
                if btn3_2.collidepoint(event.pos):
                    drawPlayer(btn3_2)
                    user.move = False
                if btn3_3.collidepoint(event.pos):
                    drawPlayer(btn3_3)
                    user.move = False


pygame.quit()
