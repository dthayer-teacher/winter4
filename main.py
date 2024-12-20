import random

import turtle

move_up_down = 0
move_mantle = move_up_down + 35
move_left_right = 0

t = turtle.Turtle()
colors = ['firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', ]
t.speed(0)
bump = 0
adjust_x = -100
adjust_y = 100
x = -100
y = move_up_down
size_x = 40
brick_x = 8
brick_y = 2.25
scale = size_x / brick_x
size_y = scale * brick_y
t.fillcolor('tan')
t.penup()
t.goto(move_left_right + -16 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.pendown()
t.begin_fill()
t.goto(move_left_right + 296 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.goto(move_left_right + 296 + adjust_x, move_mantle - size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_mantle - size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.end_fill()
x_beg = -20
y_beg = 0
for x in range(15):
    x_beg = x * 20 - 8
    t.penup()
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + adjust_y)
    t.pendown()
    col = random.choice(colors)
    t.fillcolor(col)
    t.begin_fill()
    t.goto(move_left_right + x_beg + adjust_x + 20, move_up_down - y_beg + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x + 20, move_up_down - y_beg + size_y + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + size_y + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + adjust_y)
    t.end_fill()

for j in range(12):
    move_y = j * size_y
    if j % 2 == 0:
        bump = 0
    else:
        x = 0
        bump = size_x / 2
        t.penup()
        t.goto(move_left_right + x + adjust_x, y - move_y + adjust_y)
        t.pendown()
        col = random.choice(colors)
        t.fillcolor(col)
        t.begin_fill()
        t.goto(move_left_right + x + bump + adjust_x, y - move_y + adjust_y)
        t.goto(move_left_right + x + bump + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + x + adjust_x, y - move_y + adjust_y)
        t.penup()
        t.end_fill()
    for i in range(7):
        x = i * size_x
        if x + bump + size_x > 280:
            size_x = size_x / 2
        else:
            size_x = 40

        start_x = x + bump
        end_x = x + bump + size_x

        t.penup()
        t.goto(move_left_right + start_x + adjust_x, y - move_y + adjust_y)
        t.pendown()

        col = random.choice(colors)
        t.fillcolor(col)
        t.begin_fill()
        if j >= 3 and j <= 9:
            if end_x > 100 and start_x < 180:
                end_x = 80

                start_x = 200
                t.penup()
                size_x = 40

        t.goto(move_left_right + end_x + adjust_x, y - move_y + adjust_y)
        t.goto(move_left_right + end_x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + start_x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + start_x + adjust_x, y - move_y + adjust_y)
        t.penup()
        t.end_fill()

t.goto(move_left_right + 80 + adjust_x, move_up_down - 35 + adjust_y)
t.fillcolor('black')
t.begin_fill()
t.goto(move_left_right + 205 + adjust_x, move_up_down - 35 + adjust_y)
t.goto(move_left_right + 205 + adjust_x, move_up_down - 115 + adjust_y)
t.goto(move_left_right + 80 + adjust_x, move_up_down - 115 + adjust_y)
t.goto(move_left_right + 80 + adjust_x, move_up_down - 35 + adjust_y)
t.end_fill()

t.fillcolor('tan')
t.penup()
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 + adjust_y)
t.pendown()
t.begin_fill()
t.goto(move_left_right + 296 + adjust_x, move_up_down - 135 + adjust_y)
t.goto(move_left_right + 296 + adjust_x, move_up_down - 135 - 2 * size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 - 2 * size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 + adjust_y)
t.end_fill()

turtle.addshape("fire.gif")
t.shape('fire.gif')
t.penup()
t.goto(45,25)


turtle.done()