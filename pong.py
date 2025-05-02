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

wn.update()

input("Press any key to continue...") # tijdelijke toevoeging t.b.v. testen