from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.hideturtle()
        self.goto(-180, 200)
        self.write(f"Points:{self.point}", move=False, font=("Ariel", 14, "normal"))

    def change_point(self):
        self.clear()
        self.point += 4
        self.write(f"Points:{self.point}", move=False, font=("Ariel", 14, "normal"))

    def you_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"You win", move=False, font=("Ariel", 14, "normal"))
