import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's color
t.color("blue")

# Move the turtle to the center of the screen
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw a square
for i in range(4):
    t.forward(100)
    t.left(90)

# Wait for a key press
t.done()