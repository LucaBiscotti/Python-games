from random import uniform
from re import A
from playsound import playsound
import turtle


sound_path = "/home/luca/Documents/Vari/Python/source/4391__noisecollector__pongblipf-5.wav"

w = turtle.Screen()
padle_a = turtle.Turtle()
padle_b = turtle.Turtle()
ball = turtle.Turtle()
pen = turtle.Turtle()
pen.a=0
pen.b=0

def set_padle(x,y,pad):
    pad.shape("square")
    pad.shapesize(4,1)
    pad.speed(0)
    pad.color("white")
    pad.penup()
    pad.goto(x,y)

def set_ball():
    ball.shape("square")
    ball.shapesize()
    ball.speed(1)
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 0.1
    ball.dy = 0.1

def set_window():
    w.title("Pong")
    w.setup(width=800,height=600)
    w.bgcolor("black")
    w.tracer(0)
    w.listen()
    w.onkeypress(a_up,"w")
    w.onkeypress(a_down,"s")
    w.onkeypress(b_up,"Up")
    w.onkeypress(b_down,"Down")

def set_res():
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    write_res()

def write_res():
    pen.clear()
    pen.write("Player A:{}      Player B:{}".format(pen.a,pen.b),align="center",font=("Courier",24,"normal"))

def a_up():
    y = padle_a.ycor()
    if(y < 260):
        y += 20
        padle_a.sety(y)

def a_down():
    y = padle_a.ycor()
    if(y > -260):
        y -= 20
        padle_a.sety(y)

def b_up():
    y = padle_b.ycor()
    if(y < 260):
        y += 20
        padle_b.sety(y)

def b_down():
    y = padle_b.ycor()
    if(y > -260):
        y -= 20
        padle_b.sety(y)

def bounce():
    if (ball.dx > 0):
        if(ball.ycor() > padle_b.ycor()+40 or ball.ycor() < padle_b.ycor()-40):
            w.win = "A HA VINTO!"
            pen.a += 1
            write_res()
            return False
    else:
        if(ball.ycor() > padle_a.ycor()+40 or ball.ycor() < padle_a.ycor()-40):
            w.win = "B HA VINTO!"
            pen.b += 1
            write_res()
            return False
    return True

def ball_move():
    if(ball.xcor() >= 370 or ball.xcor() <= -370):
        if bounce():
            ball.dx *= -1
            playsound(sound_path)
        else:
            return False
    if(ball.ycor() >= 290 or ball.ycor() <= -290):
        ball.dy *= -1
        playsound(sound_path)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    return True

def start_game():
    if(w.textinput(w.win,"Continuare?") != None):
        return True
    return False

def main():
    set_window()
    set_padle(-380,0,padle_a)
    set_padle(380,0,padle_b)
    set_ball()
    set_res()
    while ball_move():
        w.update()
    if(start_game()):
        main()

main()



    
