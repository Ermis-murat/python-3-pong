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

while True:
    wn.update()
    # Beweeg de bal
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

input("Press any key to continue...") # tijdelijke toevoeging t.b.v. testen