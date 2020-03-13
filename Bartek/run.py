import ctypes
import pygame, pygameMenu
import sys
import sqlite3 as lite

con = lite.connect('database.db')
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS save( id integer PRIMARY KEY, nick text NOT NULL, coin integer, world integer, lvl integer, eq integer);")
    # cur.execute("SHOW TABLES;")

    # data = cur.fetchone()[0]
    # print("SQLite version: {}".format(data))
    # fsdfsd

"""
    Nick coin World Lvl Eq 
"""


class Game(object):
    def __init__(self):
        # Screen size
        user32 = ctypes.windll.user32
        self.ScreenWidth = user32.GetSystemMetrics(0)
        self.ScreenHeight = user32.GetSystemMetrics(1)
        screensize = (self.ScreenWidth, self.ScreenHeight)
        self.ScreenWidth2 = int(self.ScreenWidth / 5)

        # Config
        self.tps_max = 60.0
        self.box = pygame.Rect(0, 0, self.ScreenWidth2, self.ScreenHeight)
        self.DeveloperMode = True
        self.Title = "Bill's Adventrure"

        # Initialization
        pygame.init()
        pygame.display.set_caption(self.Title)

        if self.DeveloperMode:
            self.screen = pygame.display.set_mode((1200, 800))
        else:
            self.screen = pygame.display.set_mode(screensize, pygame.FULLSCREEN, 0, 32)

        self.x = self.screen.get_width()
        self.y = self.screen.get_height()

        # Background Image
        self.background_image = pygame.image.load("Framework/Graphic/background.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.x, self.y))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            # print(self.tps_delta)

            # Drawing
            # self.screen.fill((0,0,0))
            self.mouse = pygame.mouse.get_pos()
            # print(mouse)
            self.draw()
            pygame.display.flip()

    def tick(self):
        """
            # Input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                buttonBoxActive.x += 10
                buttonBoxActive.y += 10
            elif keys[pygame.K_UP]:
                buttonBoxActive.x -= 10
                buttonBoxActive.y -= 10
            """

    def draw(self):
        self.screen.blit(self.background_image, [0, 0])
        # pygame.draw.rect(self.screen, (127, 127, 127), self.box)
        # Rysowanie napisu
        self.draw_text(self.Title, (127, 27, 27), int(self.x/2), 100, 80, 0)

        # Start Button
        if int(self.x/2-150) + 300 > self.mouse[0] > int(self.x/2-150) and 250 + 75 > self.mouse[1] > 250:
            pygame.draw.rect(self.screen, (0, 255, 0), (int(self.x/2-150), 250, 300, 75))
        else:
            pygame.draw.rect(self.screen, (0, 200, 0), (int(self.x/2-150), 250, 300, 75))

        self.draw_text("New game", (127, 27, 27), 0, 0, 24, 1)




    def draw_text(self, text, color, x, y, size, dev):
        # Fonts
        # self.font = pygame.font.Font('Framework/Fonts/comic-sans-ms.ttf', 32)
        self.font = pygame.font.Font('Framework/Fonts/leadcoat.ttf', size)

        textobj = self.font.render(text, True, color)
        textRect = textobj.get_rect()

        if dev == 1:
            textRect.center = ((int(self.x/2-150) + (300 / 2)), (250 + (75 / 2)))
        else:
            textRect.center = (x, y)
        self.screen.blit(textobj, textRect)


if __name__ == "__main__":
    Game()
