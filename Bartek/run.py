import pygame, sys, ctypes

class Game(object):
    def __init__(self):
        # Screen size
        user32 = ctypes.windll.user32
        self.ScreenWidth = user32.GetSystemMetrics(0)
        self.ScreenHeight = user32.GetSystemMetrics(1)
        screensize = (self.ScreenWidth, self.ScreenHeight)

        # Config
        self.tps_max = 60.0
        self.box = pygame.Rect(0, 0, 300, self.ScreenHeight)

        # Initialization
        pygame.init()
        pygame.display.set_caption('ZTGK 2020')
        self.screen = pygame.display.set_mode(screensize, pygame.FULLSCREEN)
        self.background_image = pygame.image.load("Framework/Graphic/background.png").convert()
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
                #print("Hey")
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            #print(self.tps_delta)

            # Drawing
            #self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()
            self.screen.blit(self.background_image, [0, 0])



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
       # self.box.x += 1
        #self.box.y += 1
        #self.box.w += 1
        pygame.draw.rect(self.screen, (127, 127, 127, 50), self.box)

if __name__ == "__main__":
    Game()
