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
        self.temporary_iKuns = pygame.sprite.Group()
        
        self._first_iKuns()

    def _load_settings(self):
        with open('Data/settings.json', encoding = 'utf-8') as settings:
            self.settings = json.load(settings)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
            bg_color = (self.settings["bg_color_R"],
                        self.settings["bg_color_G"],
                        self.settings["bg_color_B"])
            self.screen.fill(bg_color)

            self.iKuns.draw(self.screen)

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_a:
            a = 0
            for i in self.iKuns:
                if i.rect.x / 200 == a and i.rect.y == 400:
                    i.kill()
                    self._move_iKuns()
                    self._new_iKun()
                else:
                    pass
        if event.key == pygame.K_s:
            a = 1
            for i in self.iKuns:
                if i.rect.x / 200 == a and i.rect.y == 400:
                    i.kill()
                    self._move_iKuns()
                    self._new_iKun()
                else:
                    pass
        if event.key == pygame.K_d:
            a = 2
            for i in self.iKuns:
                if i.rect.x / 200 == a and i.rect.y == 400:
                    i.kill()
                    self._move_iKuns()
                    self._new_iKun()
                else:
                    pass
        if event.key == pygame.K_f:
            a = 3
            for i in self.iKuns:
                if i.rect.x / 200 == a and i.rect.y == 400:
                    i.kill()
                    self._move_iKuns()
                    self._new_iKun()
                else:
                    pass

    def _move_iKuns(self):
        for i in iter(self.iKuns):
            i.rect.x = i.rect.x
            i.rect.y += 200
            self.temporary_iKuns.add(i)
        self.iKuns = self.temporary_iKuns

    def _first_iKuns(self):
        for i in range(3):
            iKun = IKun(self)
            iKun.x = random.randint(0, 3) * 200
            iKun.y = i * 200
            iKun.rect.x = iKun.x
            iKun.rect.y = iKun.y
            self.iKuns.add(iKun)

    def _new_iKun(self):
        iKun = IKun(self)
        iKun.x = random.randint(0, 3) * 200
        iKun.rect.x = iKun.x
        iKun.rect.y = 0
        self.iKuns.add(iKun)


if __name__ == '__main__':
    main = Main()
    main.run_game()
