import ctypes
import pygame
import sys
import json
import socket


# Check config file before init
def check_json(file_js):
    try:
        with open(file_js) as f:
            print(f.readlines())
            # Do something with the file
    except IOError:
        print("File not accessible")
        f = open(file_js, "a")

        # Screen size
        user32 = ctypes.windll.user32
        ScreenWidth = user32.GetSystemMetrics(0)
        ScreenHeight = user32.GetSystemMetrics(1)

        x = {
            "settings": {
                "volume": 1,
                "music": 1,
                "tps": 60
            },
            "screen": {
                "width": ScreenWidth,
                "height": ScreenHeight,
                "fullscreen": 1
            }
        }
        f.write(json.dumps(x))
        f.close()


# load json file
def load_json(file_js):
    with open(file_js, 'r') as file:
        data = file.read().replace('\n', '')
        data = json.loads(data)
    return data


# Update json file
def update_json(json_object, file_js):
    a_file = open(file_js, "w")
    json.dump(json_object, a_file)
    a_file.close()


class Game(object):
    def __init__(self):
        # ----------------------------------------------------------------------------------------
        # ----------------------------------------[CONFIG]----------------------------------------
        # ----------------------------------------------------------------------------------------

        # Config
        self.choice = 'menu'
        self.Title = "Bill's Adventrure"
        self.config_file = 'config.txt'
        self.save_file = 'save.json'
        tps_clock = pygame.time.Clock()
        tps_delta = 0.0

        # Check settings
        check_json(self.config_file)
        self.json_data = load_json(self.config_file)

        # Settings
        settings_json = self.json_data['settings']
        tps_max = settings_json['tps']
        volume_m = settings_json['music']

        # Screen size
        screen_json = self.json_data['screen']
        fullscreen = screen_json['fullscreen']
        screensize = (screen_json['width'], screen_json['height'])

        # ----------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------

        # Initialization
        pygame.init()
        pygame.display.set_caption(self.Title)

        if fullscreen == 0:
            self.screen = pygame.display.set_mode((1200, 800))
        else:
            self.screen = pygame.display.set_mode(screensize, pygame.FULLSCREEN, 0, 32)

        self.x = self.screen.get_width()
        self.y = self.screen.get_height()

        # Main Menu Music
        pygame.mixer.music.load('Framework/Music/Cinematic.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume_m)

        # Icon Image
        gameIcon = pygame.image.load('Framework/Graphic/Icon.png')
        pygame.display.set_icon(gameIcon)

        # Buttons Image
        self.btn_image = pygame.image.load("Framework/Graphic/sing.png").convert_alpha()
        self.btn_image_active = pygame.image.load("Framework/Graphic/sing_active.png").convert_alpha()
        self.btn_image_sm_active = pygame.image.load("Framework/Graphic/sing_active_sm.png").convert_alpha()

        # Background Image
        self.background_image = pygame.image.load("Framework/Graphic/background.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.x, self.y))
        self.bg_l1_image = pygame.image.load("Framework/Graphic/plansza_1.png").convert()
        self.bg_l1_image = pygame.transform.scale(self.bg_l1_image, (self.x, self.y))

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)

            # Ticking
            tps_delta += tps_clock.tick() / 1000.0
            while tps_delta > 1 / tps_max:
                self.tick()
                tps_delta -= 1 / tps_max

            # Drawing
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
        result = self.choice.split(":")
        self.choice = result[0]

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
        elif self.choice == 'volume':
            self.choice = 'settings'
            volume_m = result[1]
            volume_m = int(volume_m) / 100.0
            pygame.mixer.music.set_volume(volume_m)
            self.json_data['settings']['music'] = volume_m
            update_json(self.json_data, self.config_file)
        elif self.choice == "fullscreen":
            self.choice = 'settings'
            data = result[1]
            data = int(data)
            self.json_data['screen']['fullscreen'] = data
            update_json(self.json_data, self.config_file)

        self.draw_text("Preview version. Build 2e83c51", (27, 27, 27), (self.x + 100) - self.x, (self.y + 10) - self.y,
                       16)

    # Draw buttons function
    def draw_buttons(self, text, text_color, size, x, y, width, height, choice=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        self.btn_image = pygame.transform.scale(self.btn_image, (width, height))
        self.btn_image_active = pygame.transform.scale(self.btn_image_active, (width, height))

        # self.btn_image_sm = pygame.transform.scale(self.btn_image_sm, (width, height))
        self.btn_image_sm_active = pygame.transform.scale(self.btn_image_sm_active, (width, height))

        if int(x / 2 - int(width / 2)) + width > mouse[0] > int(x / 2 - int(width / 2)) and y + height > mouse[1] > y:
            if width < 200:
                self.screen.blit(self.btn_image_sm_active, [int(x / 2 - int(width / 2)), y])
            else:
                self.screen.blit(self.btn_image_active, [int(x / 2 - int(width / 2)), y])
            self.draw_text(text, text_color, int(x / 2), int(y + int(height / 2)), size)
            if click[0] == 1 and choice != None:
                self.choice = choice
        else:
            if width < 200:
                self.screen.blit(self.btn_image, [int(x / 2 - int(width / 2)), y])
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
        data = load_json(self.save_file)
        count = data['count']

        # Background and title
        self.screen.blit(self.background_image, [0, 0])
        # Draw text title
        self.draw_text(self.Title, (127, 27, 27), int(self.x / 2), 100, 96)

        # Available game saves
        self.draw_text("Available game saves: " + str(count) + "/4", (154, 27, 27), self.x / 2, 200, 48)

        y = 250
        for x in range(count):
            x += 1
            save = data['save' + str(x)]
            world = save['world']
            self.draw_buttons("World " + str(world), (154, 27, 27), 36, self.x, y + 40, 500, 80, 'new_game:save' + str(x))
            y += 100

        self.draw_buttons("Back", (127, 27, 27), 36, self.x, self.y - 100, 300, 64, 'back')

    # Multiplayer function
    def multiplayer(self):
        self.choice = 'menu'
        HOST = '127.0.0.1'
        PORT = 9879

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'Test message')
            data = s.recv(1024)

        print('Received', repr(data))


    # CC function
    def change_character(self):
        pass

    def settings(self):
        # Background and title
        self.screen.blit(self.background_image, [0, 0])
        # Draw text title
        self.draw_text(self.Title, (127, 27, 27), int(self.x / 2), 100, 96)

        # Volume
        self.draw_text("Volume", (154, 27, 27), (self.x + 300) - self.x, 300, 48)
        self.draw_buttons("0%", (127, 27, 27), 36, self.x, 268, 100, 64, 'volume:0')
        self.draw_buttons("20%", (127, 27, 27), 36, self.x + 250, 268, 100, 64, 'volume:20')
        self.draw_buttons("50%", (127, 27, 27), 36, self.x + 500, 268, 100, 64, 'volume:50')
        self.draw_buttons("70%", (127, 27, 27), 36, self.x + 750, 268, 100, 64, 'volume:70')
        self.draw_buttons("100%", (127, 27, 27), 36, self.x + 1000, 268, 100, 64, 'volume:100')

        # Full screen
        self.draw_text("Full Screen", (154, 27, 27), (self.x + 300) - self.x, 400, 48)
        self.draw_buttons("Off", (127, 27, 27), 36, self.x + 375, 368, 100, 64, 'fullscreen:0')
        self.draw_buttons("On", (127, 27, 27), 36, self.x + 625, 368, 100, 64, 'fullscreen:1')

        # Screen resolution
        self.draw_text("Screen resolution", (154, 27, 27), (self.x + 300) - self.x, 500, 48)

        self.draw_buttons("Back", (127, 27, 27), 36, self.x, self.y - 100, 300, 64, 'back')

    # Naprawić i zrobić
    def create_sockets(self):
        self.ip = "192.168.1.24"
        self.port = 8888
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)
        self.conn, self.addr = self.server_socket.accept()


if __name__ == "__main__":
    Game()
