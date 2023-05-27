import sys, json
import pygame


class Main:
    def __init__(self):
        pygame.init()
        self.load_settings()
        self.screen = pygame.display.set_mode(
            (self.settings["screen_width"], self.settings["screen_height"]))
        pygame.display.set_caption("iKunGame2023")
        self.run_game()
    
    def load_settings(self):
        with open('Data/settings.json', encoding = 'utf-8') as settings:
            self.settings = json.load(settings)

    def run_game(self):
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            bg_color = (self.settings["bg_color_R"],
                        self.settings["bg_color_G"],
                        self.settings["bg_color_B"])
            self.screen.fill(bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    main = Main()
