import json, sys, tkinter

from Data.classic import Classic as Classic
from Data.endless import Endless as Endless
import Data.functions as functions
import Data.launcher_buttons as launcher_buttons


class Main:
    def __init__(self):
        self._load_settings()
        window = tkinter.Tk()
        window.title(self.title)
        window.geometry(self.size)
        
        self.window = window

        self._buttons()

        window.mainloop()

    def _load_settings(self):
        with open('Data/settings.json', encoding='utf-8') as settings:
            self.settings = json.load(settings)
        self.title = self.settings["title"]
        self.size = self.settings["choosing_board_size"]
        self.font = self.settings["font"]
        self.word_size = self.settings["word_size"]
    
    def _buttons(self):
        lbl = tkinter.Label(self.window, text="Choose Difficulty",
                            font=(self.font, self.word_size))
        lbl.grid(column=0, row=0)

        launcher_buttons.buttons_classic(self)
        launcher_buttons.buttons_endless(self)

        lbl = tkinter.Label(self.window, text="Reset The Highest Score",
                            font=(self.font, self.word_size))
        lbl.grid(column=0, row=2)

        btn = tkinter.Button(
            self.window, text=" Reset", bg="black", fg="white",
            font=(self.font, self.word_size), 
            command=functions.clear_score_list)
        btn.grid(column=1, row=2)

        btn = tkinter.Button(
            self.window, text="About ",
            font=(self.font, self.word_size), command=functions.about)
        btn.grid(column=2, row=2)

        btn = tkinter.Button(
            self.window, text=" Quit ",
            font=(self.font, self.word_size), command=sys.exit)
        btn.grid(column=3, row=2)

    def _easy(self):
        self.difficulty = "easy"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.word_size),
            command=self._play_classic)
        btn.grid(column=5, row=0)
        
    def _normal(self):
        self.difficulty = "normal"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.word_size),
            command=self._play_classic)
        btn.grid(column=5, row=0)
        
    def _hard(self):
        self.difficulty = "hard"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.word_size),
            command=self._play_classic)
        btn.grid(column=5, row=0)
        
    def _insane(self):
        self.difficulty = "insane"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.word_size),
            command=self._play_classic)
        btn.grid(column=5, row=0)
        
    def _play_classic(self):
        self.classic_game = Classic(self.difficulty)
        functions.play_bgm()
        self.classic_game.run_game()

    def _play_endless(self):
        self.endless_game = Endless()
        functions.play_bgm()
        self.endless_game.run_game()


if __name__ == '__main__':
    main = Main()
