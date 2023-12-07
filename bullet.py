from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.goto(x, y + 10)
        self.speed("fastest")
        self.move_speed = 20
        self.dy = 20

    def move(self):
        self.sety(self.ycor() + self.dy)