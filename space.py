from turtle import Turtle
from bullet import Bullet


class Space(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.goto(0, -220)
        self.bullet = None
        self.bullet_speed = 20
        self.bullet_state = "ready"

    def move_right(self):
        if self.xcor() < 170:
            new_x = self.xcor() + 10
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -175:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())

    def shoot(self):
        if self.bullet_state == "ready":
            self.bullet = Bullet(self.xcor(), self.ycor() + 10)
            self.bullet_state = "fire"






