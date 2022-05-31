from dataclasses import dataclass, field
from tkinter import *

from game import Game

@dataclass
class Model:
    title: str = "Tennis Game"
    game: Game = field(default=Game(0, 0))


@dataclass
class Commands:
    model: Model

    def reset_game(self):
        self.model.game.p1 = 0
        self.model.game.p2 = 0
        label['text'] = self.model.game.score

    def score_p1(self):
        self.model.game.score_p1()
        label['text'] = self.model.game.score

    def score_p2(self):
        self.model.game.score_p2()
        label['text'] = self.model.game.score




model = Model()
commands = Commands(model=model)


window = Tk()
window.title(model.title)

btn1 = Button(window, text="P1 Score", command=commands.score_p1)
btn2 = Button(window, text="P2 Score", command=commands.score_p2)
label = Label(window, text="Score")
btn3 = Button(window, text="Reset Game", command=commands.reset_game)

for widget in [btn1, btn2, label, btn3]:
    widget.pack(side=LEFT)



window.mainloop()