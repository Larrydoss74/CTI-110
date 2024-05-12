"""
Larry Doss
4/15/24
P4LAB1b
Initials
"""
import turtle as t

# Set up the turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a turtle
ld_turtle = t.Turtle()
ld_turtle.speed("fastest")  # Set the drawing speed

# Draw the letter "L"
ld_turtle.penup()
ld_turtle.goto(-50, 0)
ld_turtle.pendown()
ld_turtle.right(90)
ld_turtle.forward(170)
ld_turtle.left(90) 
ld_turtle.forward(100)

# Move to draw the letter "D"
ld_turtle.penup()
ld_turtle.goto(50, 0)
ld_turtle.pendown()
ld_turtle.circle(90, 180)
ld_turtle.left(90)
ld_turtle.forward(180)


# Hide the turtle cursor
ld_turtle.hideturtle()

# Keep the window open until manually closed
t.done()
