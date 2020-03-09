import pygame, sys, ctypes

# Screen size
user32 = ctypes.windll.user32

pygame.init()
screen = pygame.display.set_mode((user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)))
box = pygame.Rect(10,10,200,500)

while True:
    # Handle events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
    # Input
    box.x += 1
    box.y += 1
    box.w += 1

    # Drawing
   #screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), box)
    pygame.display.flip()