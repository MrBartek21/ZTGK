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
        self.choice = 'menu'
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

        # Buttons Image
        self.btn_image = pygame.image.load("Framework/Graphic/tabliczka_2.png").convert_alpha()
        self.btn_image2 = pygame.image.load("Framework/Graphic/tabliczka_3.png").convert_alpha()

        # Background Image
        self.background_image = pygame.image.load("Framework/Graphic/background.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.x, self.y))
        self.bg_l1_image = pygame.image.load("Framework/Graphic/plansza_1.png").convert()
        self.bg_l1_image = pygame.transform.scale(self.bg_l1_image, (self.x, self.y))
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
            # print(self.choice)
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
        # Choice Menu
        if self.choice == 'menu':
            self.main_menu()
        elif self.choice == 'new_game':
            self.new_game()
        elif self.choice == 'load_game':
            self.load_game()
        elif self.choice == 'multiplayer':
            self.multiplayer()
        elif self.choice == 'change_character':
            self.change_character()
        elif self.choice == 'settings':
            self.settings()
        elif self.choice == 'quit_game':
            sys.exit(0)
        elif self.choice == 'back':
            self.choice = 'menu'

        self.draw_text("Preview version. Build 2e83c51", (27, 27, 27), (self.x + 100) - self.x, (self.y+10)-self.y,
                       16)

    # Draw buttons function
    def draw_buttons(self, text, text_color, size, x, y, width, height, choice=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        self.btn_image = pygame.transform.scale(self.btn_image, (width, height))
        self.btn_image2 = pygame.transform.scale(self.btn_image2, (width, height))

        if int(x / 2 - int(width / 2)) + width > mouse[0] > int(x / 2 - int(width / 2)) and y + height > mouse[1] > y:
            self.screen.blit(self.btn_image2, [int(x / 2 - int(width / 2)), y])
            self.draw_text(text, text_color, int(x / 2), int(y + int(height / 2)), size)
            if click[0] == 1 and choice != None:
                self.choice = choice
        else:
            self.screen.blit(self.btn_image, [int(x / 2 - int(width / 2)), y])
            self.draw_text(text, text_color, int(x / 2), int(y + int(height / 2)), size)

    # Drawn text functions
    def draw_text(self, text, color, x, y, size):
        # Fonts
        font = pygame.font.Font('Framework/Fonts/leadcoat.ttf', size)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        self.screen.blit(textobj, textrect)

    def main_menu(self):
        # Background and title
        self.screen.blit(self.background_image, [0, 0])
        # Draw text title
        self.draw_text(self.Title, (127, 27, 27), int(self.x / 2), 100, 96)

        self.draw_buttons("New game", (127, 27, 27), 36, self.x, 250, 300, 64, 'new_game')  # 1
        self.draw_buttons("Load game", (127, 27, 27), 36, self.x, 325, 300, 64, 'load_game')  # 2
        self.draw_buttons("Multiplayer", (127, 27, 27), 36, self.x, 400, 300, 64, 'multiplayer')  # 3
        self.draw_buttons("Change character", (127, 27, 27), 36, self.x, 475, 300, 64, 'change_character')  # 4
        self.draw_buttons("Settings", (127, 27, 27), 36, self.x, 550, 300, 64, 'settings')  # 5
        self.draw_buttons("Exit", (127, 27, 27), 36, self.x, 625, 300, 64, 'quit_game')  # 6

    def new_game(self):
        self.screen.blit(self.bg_l1_image, [0, 0])
        self.draw_buttons("Exit", (127, 27, 27), 36, self.x, 625, 300, 64, 'quit_game')  # 6

    # Load Game function
    def load_game(self):
        pass

    # Multiplayer function
    def multiplayer(self):
        pass

    # CC function
    def change_character(self):
        pass

    def settings(self):
        # Background and title
        self.screen.blit(self.background_image, [0, 0])
        # Draw text title
        self.draw_text(self.Title, (127, 27, 27), int(self.x / 2), 100, 96)

        self.draw_text("Music", (127, 27, 27), (self.x+300)-self.x, 300, 36)
        self.draw_buttons("Back", (127, 27, 27), 36, self.x, self.y - 100, 300, 64, 'back')

    # Music function
    def music(self):
        pass


if __name__ == "__main__":
    Game()
