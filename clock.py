import turtle
import time
import math

#SCREEN SETUP 
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("#0a0a12")
screen.setup(650, 650)
screen.tracer(0)

CENTER_COLOR = "#FFD700"
FACE_COLOR = "#E0E0E0"

#CLOCK FACE 
face = turtle.Turtle()
face.hideturtle()
face.speed(0)

def draw_face():
    # Outer Ring
    face.penup()
    face.goto(0, -210)
    face.pendown()
    face.pensize(5)
    face.color("#4444ff")
    face.circle(210)

    # Minute & Hour Marks
    for i in range(60):
        angle = math.radians(90 - i * 6)

        outer = 200
        inner = 180 if i % 5 == 0 else 190

        x1 = outer * math.cos(angle)
        y1 = outer * math.sin(angle)
        x2 = inner * math.cos(angle)
        y2 = inner * math.sin(angle)

        face.penup()
        face.goto(x1, y1)
        face.pendown()

        face.pensize(3 if i % 5 == 0 else 1)
        face.color(FACE_COLOR if i % 5 == 0 else "#666677")
        face.goto(x2, y2)

    # Numbers
    face.penup()
    face.color(FACE_COLOR)

    for i in range(1, 13):
        angle = math.radians(90 - i * 30)

        x = 155 * math.cos(angle)
        y = 155 * math.sin(angle)

        face.goto(x, y - 12)
        face.write(
            str(i),
            align="center",
            font=("Georgia", 18, "bold")
        )

    #Brand Name
    face.goto(0, 90)
    face.color("#8a8ab5")
    face.write(
        "NAMIT",
        align="center",
        font=("Georgia", 12, "normal")
    )

draw_face()

#HANDS
def make_hand(color, width):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)
    t.pensize(width)
    return t

hour_hand = make_hand("white", 7)
minute_hand = make_hand("#00E5FF", 5)
second_hand = make_hand("#FF3B3B", 2)

#DIGITAL CLOCK 
digital = turtle.Turtle()
digital.hideturtle()
digital.penup()
digital.color("#BBBBBB")
digital.goto(0, -260)

#DATE & DAY
date_pen = turtle.Turtle()
date_pen.hideturtle()
date_pen.speed(0)
date_pen.penup()

def draw_date():
    date_pen.clear()

    # Small box near 3 o'clock (nudged slightly inward toward center)
    x = 65
    y = 12

    width = 78
    height = 22

    # Box
    date_pen.goto(x, y)
    date_pen.setheading(0)
    date_pen.pensize(2)
    date_pen.color("black", "white")
    date_pen.pendown()
    date_pen.begin_fill()

    for _ in range(2):
        date_pen.forward(width)
        date_pen.right(90)
        date_pen.forward(height)
        date_pen.right(90)

    date_pen.end_fill()

    # Date (with year) inside box
    date_pen.penup()
    date_pen.goto(x + width/2, y - 16)
    date_pen.color("black")
    date_pen.write(
        time.strftime("%d/%m/%Y"),
        align="center",
        font=("Arial", 9, "bold")
    )

    # Day name below the box
    date_pen.goto(x + width/2, y - 40)
    date_pen.color("#DDDDDD")
    date_pen.write(
        time.strftime("%A"),
        align="center",
        font=("Arial", 10, "bold")
    )

#DRAW HAND 
def draw_hand(hand, angle, length, tail=0):
    hand.penup()

    if tail:
        back = angle + 180
        hand.goto(
            tail * math.cos(math.radians(back)),
            tail * math.sin(math.radians(back))
        )
    else:
        hand.goto(0, 0)

    hand.setheading(angle)
    hand.pendown()
    hand.forward(length)

#CENTER DOT
center = turtle.Turtle()
center.hideturtle()
center.speed(0)

def draw_center():
    center.clear()
    center.penup()
    center.goto(0, -9)
    center.color(CENTER_COLOR)
    center.pendown()
    center.begin_fill()
    center.circle(9)
    center.end_fill()

#ANIMATION 
def tick():

    hour_hand.clear()
    minute_hand.clear()
    second_hand.clear()
    digital.clear()

    draw_date()

    now = time.localtime()

    h = now.tm_hour % 12
    m = now.tm_min
    s = now.tm_sec

    hour_angle = 90 - (h * 30 + m * 0.5)
    minute_angle = 90 - (m * 6 + s * 0.1)
    second_angle = 90 - s * 6

    draw_hand(hour_hand, hour_angle, 100)
    draw_hand(minute_hand, minute_angle, 150)
    draw_hand(second_hand, second_angle, 175, tail=25)

    digital.write(
        time.strftime("%H:%M:%S"),
        align="center",
        font=("Consolas", 16, "normal")
    )

    draw_center()

    screen.update()
    screen.ontimer(tick, 1000)

tick()

try:
    screen.mainloop()
except turtle.Terminator:
    pass

