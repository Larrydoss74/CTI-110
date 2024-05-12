'''
Larry Doss
4/6/24
P4LAB1a
Shapes
'''

import turtle

# Set up the turtle
window = turtle.Screen()
window.bgcolor("white")
my_turtle = turtle.Turtle()
my_turtle.speed("slow")  # Adjust the speed as desired
my_turtle.color("green")  # You can choose any color you like
my_turtle.pensize(2)

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Side length of the square
    my_turtle.right(90)  # Turn 90 degrees to the right

# Move to a new position for the triangle
my_turtle.penup()
my_turtle.goto(150, 0)  # Adjust the position
my_turtle.pendown()

# Draw an equilateral triangle
for _ in range(3):
    my_turtle.forward(100)  # Side length of the triangle
    my_turtle.left(120)  # Turn 120 degrees to the left

# Hide the turtle cursor
my_turtle.hideturtle()

# Keep the window open until manually closed
turtle.done()
