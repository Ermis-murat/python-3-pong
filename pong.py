import turtle

# Venster instellen
wn = turtle.Screen()
wn.title("Pong voor Murat ermis")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=6, stretch_len=1)
paddle.penup()
paddle.goto(-380, 0)

def paddle_up(): 
    y = paddle.ycor() 
    if y < 250: 
        y += 20 
        paddle.sety(y)

def paddle_down(): 
    y = paddle.ycor() 
    if y > -240: 
        y -= 20 
        paddle.sety(y)

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

# Pen om de score weer te geven
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

def update_score():
    pen.clear()
    pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

while True:
    wn.update()
    # Beweeg de bal
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # detecteer randen van het scherm
    if (ball.xcor() > 380 or ball.xcor() < -400 ):
       ball.dx *= -1
    if (ball.ycor() > 290 or ball.ycor() < -290 ):
       ball.dy *= -1
    # Detecteer botsing met paddle
    if (ball.dx < 0 and ball.xcor() < -380): # ball beweegt naar links en zit bij de linker zijkant.
        if (paddle.ycor() - 60 < ball.ycor() < paddle.ycor() + 60): # bal 'raakt' de bal
            ball.dx *= -1 # beweeg de bal de andere kant uit (horizontaal)
            ball.dy *= -1 # beweeg de bal de andere kant uit (verticaal)
        else:
            ball.dx = 0 
            ball.dy = 0
    
    score = score + 1
    update_score()  # Werk de score weergave bij

# Score variabele
score = 0

# Pen om de score weer te geven
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

def update_score():
    pen.clear()
    pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
input("Press any key to continue...") # tijdelijke toevoeging t.b.v. testen