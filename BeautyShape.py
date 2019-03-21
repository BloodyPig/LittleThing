import turtle

def draw_square(t):
    for i in range(1,5):
        t.forward(200)
        t.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()
