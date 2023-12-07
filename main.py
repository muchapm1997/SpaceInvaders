import time
from turtle import Screen
from space import Space
from invaders import Invaders
from scoreboard import Scoreboard

screen = Screen()
screen.title("Space Invaders")
screen.setup(400, 500)
scoreboard = Scoreboard()

blocks_position = []

x = -120
for i in range(7):
    y = 160
    for j in range(3):
        blocks_position.append((x, y))
        y -= 30
    x += 40

blocks_list = [Invaders(position) for position in blocks_position]


space = Space()
screen.listen()
screen.onkey(space.move_left, "Left")
screen.onkey(space.move_right, "Right")
screen.onkey(space.shoot, "space")
screen.onkeypress(space.move_left, "Left")
screen.onkeypress(space.move_right, "Right")

while True:
    if scoreboard.point == 84:
        scoreboard.you_win()
    for block in blocks_list:
        block.move()
    if any(block.xcor() > 160 or block.xcor() < -170 for block in blocks_list):
        for block in blocks_list:
            block.direction *= -1
    screen.update()
    time.sleep(0.01)
    if space.bullet_state == "fire":
        space.bullet.move()
        for enemy in blocks_list:
            if space.bullet.distance(enemy) < 15:
                enemy.hideturtle()
                blocks_list.remove(enemy)
                scoreboard.change_point()
                space.bullet.hideturtle()
                space.bullet_state = "ready"
        if space.bullet.ycor() > 250:
            space.bullet.hideturtle()
            space.bullet_state = "ready"
        if space.bullet_state == "ready":
            screen.onkey(space.shoot, "space")
