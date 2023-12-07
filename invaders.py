from turtle import Turtle


class Invaders(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.speed("fastest")
        self.shapesize(1, 1)
        self.penup()
        self.goto(position)
        self.x_speed = 15
        self.direction = 1

    def move(self):
        new_x = self.xcor() + self.x_speed * self.direction
        self.setx(new_x)
