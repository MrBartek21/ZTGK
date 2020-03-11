import ctypes
import pygame
import sys
import sqlite3 as lite

con = lite.connect('settings.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()[0]
    print("SQLite version: {}".format(data))

print(pygame.font.get_fonts())
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

        # Initialization
        pygame.init()
        pygame.display.set_caption('ZTGK 2020')

        if self.DeveloperMode:
            self.screen = pygame.display.set_mode((1200, 800))
        else:
            self.screen = pygame.display.set_mode(screensize, pygame.FULLSCREEN, 0, 32)

        self.x = self.screen.get_width()
        self.y = self.screen.get_height()

        # Fonts
        self.font = pygame.font.Font('Framework/Fonts/comic-sans-ms.ttf', 32)

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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            # print(self.tps_delta)

            # Drawing
            # self.screen.fill((0,0,0))
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
        pygame.draw.rect(self.screen, (127, 127, 127), self.box)
        self.draw_text("ZTGK 2020", (0, 255, 0), 15, 10)

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, True, color)
        textRect = textobj.get_rect()
        textRect.topleft = (x, y)
        self.screen.blit(textobj, textRect)


if __name__ == "__main__":
    Game()
