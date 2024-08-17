import json, random, sys, time
import pygame
import pygame.mixer as mixer
import Data.functions as functions

from Data.iKun import IKun


class Classic:
    def __init__(self, difficulty):
        pygame.init()
        mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        self._load_settings()
        self.screen = pygame.display.set_mode(
            (self.settings["screen_width"], self.settings["screen_height"]))
        pygame.display.set_caption("iKunGame2023 v1.1")
        
        self.difficulty = difficulty
        self.iKuns_num = 0
        self.total_iKuns_num = \
            self.settings["classic_iKun_num"][self.difficulty]
        self.max_time = self.settings["classic_time"]
        self.start_time = 0
        self.game_time = 0
        
        self.iKuns = pygame.sprite.Group()
        self.temporary_iKuns = []
        self._first_iKuns()

    def _load_settings(self):
        with open('Data/settings.json', encoding = 'utf-8') as settings:
            self.settings = json.load(settings)

    def run_game(self):
        self.start_time = time.time()
        while True:
            self.game_time = time.time() - self.start_time
            if self.game_time < self.max_time:
                self._check_events()
                self._update_screen()
                if self.iKuns_num >= self.total_iKuns_num:
                    functions.victory(self.game_time, self.difficulty)
            else:
                functions.defeat_classic(self.iKuns_num)
            functions.score_board_classic(self.iKuns_num, self.total_iKuns_num)

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
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_a:
            a = 0
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    functions.defeat_classic(self.iKuns_num)
        if event.key == pygame.K_s:
            a = 1
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    functions.defeat_classic(self.iKuns_num)
        if event.key == pygame.K_d:
            a = 2
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    functions.defeat_classic(self.iKuns_num)
        if event.key == pygame.K_f:
            a = 3
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    functions.defeat_classic(self.iKuns_num)

    def _first_iKuns(self):
        iKun = IKun(self)
        iKun.x = random.randint(0, 3) * 200
        iKun.y = 0
        iKun.rect.x = iKun.x
        iKun.rect.y = iKun.y
        self.iKuns.add(iKun)

    def _new_iKun(self):
        iKun = IKun(self)
        iKun.x = random.randint(0, 3) * 200
        iKun.rect.x = iKun.x
        iKun.rect.y = 0
        self.iKuns.add(iKun)
