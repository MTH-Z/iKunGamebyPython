import json, sys, tkinter

from Data.classic import Classic as Classic
import Data.functions as functions


class Main():
    def __init__(self):
        self._load_settings()
        window = tkinter.Tk()
        window.title(self.title)
        window.geometry(self.size)
        
        self.window = window

        self._buttons()

        window.mainloop()

    def _load_settings(self):
        with open('Data/settings.json', encoding = 'utf-8') as settings:
            self.settings = json.load(settings)
        self.title = self.settings["title"]
        self.size = self.settings["choosing_board_size"]
        self.font = self.settings["font"]
        self.w_size = self.settings["w_size"]
    
    def _buttons(self):
        lbl = tkinter.Label(self.window, text="Choose Difficultty",
                            font=(self.font, self.w_size))
        lbl.grid(column=0, row=0)

        btn = tkinter.Button(
            self.window, text=" Easy ", bg="blue", fg="white",
            font=(self.font, self.w_size), command=self._easy)
        btn.grid(column=1, row=0)

        btn = tkinter.Button(
            self.window, text="Normal", bg="yellow", fg="black",
            font=(self.font, self.w_size), command=self._normal)
        btn.grid(column=2, row=0)

        btn = tkinter.Button(
            self.window, text=" Hard ", bg="red", fg="white",
            font=(self.font, self.w_size), command=self._hard)
        btn.grid(column=3, row=0)

        btn = tkinter.Button(
            self.window, text="Insane", bg="purple", fg="white",
            font=(self.font, self.w_size), command=self._insane)
        btn.grid(column=4, row=0)

        lbl = tkinter.Label(self.window, text="Reset The Highest Score",
                            font=(self.font, self.w_size))
        lbl.grid(column=0, row=1)

        btn = tkinter.Button(
            self.window, text=" Reset", bg="black", fg="white",
            font=(self.font, self.w_size), 
            command=functions.clear_score_list)
        btn.grid(column=1, row=1)

        btn = tkinter.Button(
            self.window, text="About ",
            font=(self.font, self.w_size), command=functions.about)
        btn.grid(column=2, row=1)

        btn = tkinter.Button(
            self.window, text=" Quit ",
            font=(self.font, self.w_size), command=sys.exit)
        btn.grid(column=3, row=1)

    def _easy(self):
        self.difficulty = "easy"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.w_size),
            command=self._play)
        btn.grid(column=5, row=0)
        
    def _normal(self):
        self.difficulty = "normal"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.w_size),
            command=self._play)
        btn.grid(column=5, row=0)
        
    def _hard(self):
        self.difficulty = "hard"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.w_size),
            command=self._play)
        btn.grid(column=5, row=0)
        
    def _insane(self):
        self.difficulty = "insane"
        btn = tkinter.Button(
            self.window, text="PLAY", font=(self.font, self.w_size),
            command=self._play)
        btn.grid(column=5, row=0)
        
    def _play(self):
        self.classic_game = Classic(self.difficulty)
        functions.play_bgm()
        self.classic_game.run_game()


if __name__ == '__main__':
    main = Main()
