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

# Toetsenbordbinding
wn.listen()
wn.onkeypress(paddle_up, "w")
wn.onkeypress(paddle_down, "s")

while True:
    wn.update()

input("Press any key to continue...") # tijdelijke toevoeging t.b.v. testen