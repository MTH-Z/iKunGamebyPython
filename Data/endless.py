import json, sys, time
import pygame
import pygame.mixer as mixer
import Data.functions as functions

from Data.classic import Classic


class Endless(Classic):
    def __init__(self):
        pygame.init()
        mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        self._load_settings()
        self.screen = pygame.display.set_mode(
            (self.settings["screen_width"], self.settings["screen_height"]))
        pygame.display.set_caption("iKunGame2023 v1.0")

        self.iKuns_num = 0
        self.start_time = 0
        self.game_time = 0
        self.last_time = 0
        self.highest_score = 0
        self._load_datas()

        self.iKuns = pygame.sprite.Group()
        self.temporary_iKuns = []
        self._first_iKuns()

    def _load_settings(self):
        with open('Data/settings.json', encoding='utf-8') as settings:
            self.settings = json.load(settings)

    def _load_datas(self):
        with open('Data/scores.json', encoding='utf-8') as score:
            scores = json.load(score)
        self.iKuns_num = scores["best_score"]["endless"]["score"]
        self.last_time = scores["best_score"]["endless"]["time"]
        self.highest_score = scores["best_score"]["endless"]["highest"]

    def run_game(self):
        self.start_time = time.time()
        while True:
            self.game_time = time.time() - self.start_time + self.last_time
            if self.iKuns_num >= 0:
                self._check_events()
                self._update_screen()
                functions.score_board_endless(self.iKuns_num, self.game_time)
            else:
                functions.defeat_endless()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self._save_and_quit()
        if event.key == pygame.K_a:
            a = 0
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    self.iKuns_num -= 20
        if event.key == pygame.K_s:
            a = 1
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    self.iKuns_num -= 20
        if event.key == pygame.K_d:
            a = 2
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    self.iKuns_num += 1
                else:
                    self.iKuns_num -= 20
        if event.key == pygame.K_f:
            a = 3
            for i in self.iKuns:
                if i.rect.x / 200 == a:
                    i.kill()
                    self._new_iKun()
                    functions.classic_click()
                    if self.iKuns_num > self.highest_score:
                        self.highest_score = self.iKuns_num
                    self.iKuns_num += 1
                else:
                    self.iKuns_num -= 20

    def _save_and_quit(self):
        with open('Data/scores.json', encoding = 'utf-8') as scores:
            s = json.load(scores)
        s["best_score"]["endless"]["score"] = self.iKuns_num
        s["best_score"]["endless"]["time"] = self.game_time
        s["best_score"]["endless"]["highest"] = self.highest_score
        with open('Data/scores.json', mode='w', encoding = 'utf-8') as scores:
            json.dump(s, scores)
        sys.exit()
