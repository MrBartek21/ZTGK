import pygame, sys

screen = pygame.display.set_mode((1280,720))

while True:
    # Handle events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    # Drawing
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10,50,200,500))
    pygame.display.flip()