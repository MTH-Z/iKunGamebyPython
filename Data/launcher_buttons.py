import tkinter


def buttons_classic(self):
    lbl = tkinter.Label(self.window, text="Choose Difficulty (Classic)",
                        font=(self.font, self.word_size))
    lbl.grid(column=0, row=0)

    btn = tkinter.Button(
        self.window, text=" Easy ", bg="blue", fg="white",
        font=(self.font, self.word_size), command=self._easy)
    btn.grid(column=1, row=0)

    btn = tkinter.Button(
        self.window, text="Normal", bg="yellow", fg="black",
        font=(self.font, self.word_size), command=self._normal)
    btn.grid(column=2, row=0)

    btn = tkinter.Button(
        self.window, text=" Hard ", bg="red", fg="white",
        font=(self.font, self.word_size), command=self._hard)
    btn.grid(column=3, row=0)

    btn = tkinter.Button(
        self.window, text="Insane", bg="purple", fg="white",
        font=(self.font, self.word_size), command=self._insane)
    btn.grid(column=4, row=0)


def buttons_endless(self):
    lbl = tkinter.Label(self.window, text="Endless",
                        font=(self.font, self.word_size))
    lbl.grid(column=0, row=1)

    btn = tkinter.Button(
        self.window, text=" PLAY ", bg="blue", fg="white",
        font=(self.font, self.word_size), command=self._play_endless)
    btn.grid(column=1, row=1)
