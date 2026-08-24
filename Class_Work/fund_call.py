from turtle import *
from datetime import datetime


def jump(distance, angle=0):
    penup()
    right(angle)
    forward(distance)
    left(angle)
    pendown()


def hand(length, tip):
    fd(length)
    rt(90)
    fd(tip / 2.0)
    lt(120)
    fd(tip)
    lt(120)
    fd(tip)
    lt(120)
    fd(tip / 2.0)


def make_hand_shape(name, length, tip):
    reset()
    jump(-length * 0.15)
    begin_poly()
    hand(length, tip)
    end_poly()

    hand_form = get_poly()
    register_shape(name, hand_form)


def clockface(radius):
    reset()
    pensize(7)

   
    pendown()
    circle(radius)
    penup()

    
    for i in range(12):
        jump(radius)
        write(
            i + 1,
            align="center",
            font=("Arial", 16, "normal")
        )
        jump(-radius)
        right(30)


def show_time():
    now = datetime.now()

    hour = now.hour % 12
    minute = now.minute
    second = now.second

    
    setheading(90)
    right(hour * 30 + minute * 0.5)
    shape("hour_hand")
    stamp()

    
    setheading(90)
    right(minute * 6)
    shape("minute_hand")
    stamp()

    
    setheading(90)
    right(second * 6)
    shape("second_hand")
    stamp()

    
    ontimer(show_time, 1000)



make_hand_shape("hour_hand", 70, 15)
make_hand_shape("minute_hand", 100, 12)
make_hand_shape("second_hand", 120, 8)

clockface(150)


hideturtle()
tracer(False)

show_time()

done()