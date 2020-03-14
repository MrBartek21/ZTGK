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
        self.choice = 0
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

        # Main Menu Music
        pygame.mixer.music.load('Framework/Music/Cinematic.mp3')
        # pygame.mixer.music.play(-1)

        # Icon Image
        gameIcon = pygame.image.load('Framework/Graphic/Icon.png')
        pygame.display.set_icon(gameIcon)

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
            # print(self.tps_clock.tick())

            # Drawing
            # self.screen.fill((0,0,0))
            print(self.choice)
            self.draw()
            pygame.display.flip()

    # Tick function
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

    # Main draw function
    def draw(self):
        if self.choice < 5:
            self.screen.blit(self.background_image, [0, 0])
            # Draw text title
            self.draw_text(self.Title, (127, 27, 27), int(self.x / 2), 100, 96, 0)

            # Choice Menu
            if self.choice == 0:
                self.draw_buttons("New game", (0, 250, 0), (27, 27, 27), self.x, 250, 300, 75, self.new_game, 0)
                self.draw_buttons("Settings", (0, 250, 0), (27, 27, 27), self.x, 350, 300, 75, self.settings, 0)
                self.draw_buttons("Exit", (0, 250, 0), (27, 27, 27), self.x, 450, 300, 75, self.quit_game, 0)
            elif self.choice == 2:
                self.draw_buttons("Music", (0, 250, 0), (27, 27, 27), 650, 300, 300, 75, self.back, 1)
                self.draw_buttons("Back", (0, 250, 0), (27, 27, 27), self.x, 650, 300, 75, self.back, 0)

    # Draw buttons function
    def draw_buttons(self, text, idle_color, action_color, x, y, width, height, action=None, choice=0):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if int(x / 2 - 150) + width > mouse[0] > int(x / 2 - 150) and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, idle_color, (int(x / 2 - 150), y, width, height))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.screen, action_color, (int(x / 2 - 150), y, width, height))

        # Other buttons
        if choice == 1:
            self.draw_text(text, (127, 27, 27), int(x / 2), int(y + int(height / 2)), 36, 0)
        else:
            self.draw_text(text, (127, 27, 27), 0, y, 36, 1)

    # Drawn text functions
    def draw_text(self, text, color, x, y, size, choice):
        # Fonts
        font = pygame.font.Font('Framework/Fonts/leadcoat.ttf', size)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()

        if choice == 1:
            textrect.center = (int(int(self.x / 2 - 150) + (300 / 2)), int(y + (75 / 2)))
        else:
            textrect.center = (x, y)
        self.screen.blit(textobj, textrect)

    def new_game(self):
        self.choice = 1

    def settings(self):
        self.choice = 2

    # Exit game function
    def quit_game(self):
        sys.exit(0)

    # Back function
    def back(self):
        self.choice = 0


if __name__ == "__main__":
    Game()
