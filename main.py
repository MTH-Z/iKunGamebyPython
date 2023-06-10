import sys, json, random
import pygame

from Data.iKun import IKun


class Main:
    def __init__(self):
        pygame.init()
        self._load_settings()
        self.screen = pygame.display.set_mode(
            (self.settings["screen_width"], self.settings["screen_height"]))
        pygame.display.set_caption("iKunGame2023")
        self.iKuns = pygame.sprite.Group()
        
        self.a = 1 # iKun生成时的循环计数器
        
        self._create_fleet()

    def _load_settings(self):
        with open('Data/settings.json', encoding = 'utf-8') as settings:
            self.settings = json.load(settings)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def _update_screen(self):
            bg_color = (self.settings["bg_color_R"],
                        self.settings["bg_color_G"],
                        self.settings["bg_color_B"])
            self.screen.fill(bg_color)

            self.iKuns.draw(self.screen)

            pygame.display.flip()

    def _create_fleet(self):
        self._new_iKun()

    def _new_iKun(self):
        if self.a == 1:
            for i in range(3):
                iKun = IKun(self)
                iKun.x = random.randint(0, 3) * 200
                iKun.y = i * 200
                iKun.rect.x = iKun.x
                iKun.rect.y = iKun.y
                self.iKuns.add(iKun)
                
                self.a += 1

        else:
            pass


if __name__ == '__main__':
    main = Main()
    main.run_game()
