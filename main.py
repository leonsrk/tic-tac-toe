import pygame

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


def gameScreen():
    screen.fill(BLACK)
    # lines
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(100, 300), end_pos=(700, 300), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(100, 500), end_pos=(700, 500), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(300, 100), end_pos=(300, 700), width=5)
    pygame.draw.line(surface=screen, color=WHITE, start_pos=(500, 100), end_pos=(500, 700), width=5)

    pygame.display.flip()


# main loop
running = True
startScreen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                gameScreen()


pygame.quit()
