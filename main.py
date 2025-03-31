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

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)

    # starting screen
    headline = FONT_h1.render("TicTacToe", True, WHITE)
    headline_rect = headline.get_rect()
    headline_rect.center = (400, 200)

    playTxt = FONT_h2.render("Play", True, WHITE)
    playTxt_rect = playTxt.get_rect()
    playTxt_rect.center = (400, 350)

    screen.blit(playTxt, playTxt_rect)
    screen.blit(headline, headline_rect)

    pygame.display.flip()

pygame.quit()
