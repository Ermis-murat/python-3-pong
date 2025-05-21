import turtle
import time
# exrta leven door nog een padle te maken en verbinden aan de eerste en dan nog een klijnere hotbox maken die levens geeft
# Venster instellen
wn = turtle.Screen()
wn.title("Pong voor Murat ermis")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
white_paddle = turtle.Turtle()
white_paddle.shape("square")
white_paddle.color("white")
white_paddle.shapesize(stretch_wid=6, stretch_len=1)
white_paddle.penup()
white_paddle.goto(-380, 0)

black_paddle = turtle.Turtle()
black_paddle.shape("square")
black_paddle.color("black")
black_paddle.shapesize(stretch_wid=2, stretch_len=1)
black_paddle.penup()
black_paddle.goto(-380, 0)

def paddle_up():
    y = white_paddle.ycor()
    if y < 250:
        white_paddle.sety(y + 20)
        black_paddle.sety(y + 20)

def paddle_down():
    y = white_paddle.ycor()
    if y > -240:
        white_paddle.sety(y - 20)
        black_paddle.sety(y - 20)

# Bal
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Toetsenbordbinding
wn.listen()
wn.onkeypress(paddle_up, "w")
wn.onkeypress(paddle_down, "s")

# Score variabele
score = 0
life = 3

# Pen om de score weer te geven
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

def update_score():
    pen.clear()
    pen.write("Score: {} Levens: {}".format(score, life), align="center", font=("Courier", 24, "normal"))

def game_over():
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 36, "normal"))

    
while True:
    wn.update()
    # Beweeg de bal
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # detecteer randen van het scherm
    if (ball.xcor() > 380 or ball.xcor() < -390 ):
       ball.dx *= -1
    if (ball.ycor() > 290 or ball.ycor() < -290 ):
       ball.dy *= -1
    
    # Detecteer botsing met paddle
    if (ball.dx < 0 and ball.xcor() < -379): # ball beweegt naar links en zit bij de linker zijkant.
        if (white_paddle.ycor() - 60 < ball.ycor() < white_paddle.ycor() + 60): # bal 'raakt' de bal
            ball.dx = -0.1 # beweeg de bal de andere kant uit (horizontaal)
            ball.dy = -0.1 # beweeg de bal de andere kant uit (verticaal)\
            score += 1
            if (white_paddle.ycor() - 20 < ball.ycor() < white_paddle.ycor() + 20):
                life = life + 1
        
        else:
            life = life -1
            ball.goto(0, 0)
            time.sleep(3)

    update_score()  # Werk de score weergave bij

    if (life == 0):
        game_over()
        time.sleep(5)
        break

input("Press any key to continue...") # tijdelijke toevoeging t.b.v. testen