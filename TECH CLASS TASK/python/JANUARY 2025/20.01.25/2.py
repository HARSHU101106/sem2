import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Heart Invitation")

# Create the turtle object
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a heart shape
def draw_heart():
    pen.color("red")
    pen.fillcolor("lightpink")  # Subtle pink color for the heart
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Function to draw a flower
def draw_flower(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("gold")
    pen.begin_fill()
    for _ in range(6):  # Draw 6 petals for a flower
        pen.circle(10, 60)
        pen.left(60)
    pen.end_fill()

# Function to draw leaves
def draw_leaves(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(15, 180)
    pen.left(90)
    pen.circle(15, 180)
    pen.end_fill()

# Function to write text
def write_text(text, x, y, font=("Arial", 25, "bold"), color="darkred"):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.write(text, align="center", font=font)

# Function to draw small hearts
def draw_small_heart(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("red")
    pen.fillcolor("pink")
    pen.begin_fill()
    pen.left(50)
    pen.forward(20)
    pen.circle(10, 200)
    pen.right(140)
    pen.circle(10, 200)
    pen.forward(20)
    pen.end_fill()

# Draw the heart shape
pen.penup()
pen.goto(0, -100)
pen.pendown()
draw_heart()

# Write the title "You're Invited!" in a professional style
write_text("You're Invited!", 0, 150, font=("Arial", 30, "bold"), color="darkblue")

# Write the names "Kamalika" and "Selvam"
write_text("Gokul", 0, -30, font=("Times New Roman", 28, "bold"), color="darkred")
write_text("and", 0, -60, font=("Times New Roman", 22, "bold"), color="darkred")
write_text("Harshu", 0, -90, font=("Times New Roman", 28, "bold"), color="darkred")

# Draw flowers and leaves around the invitation
draw_flower(100, 30)  # Flower on the right
draw_flower(-100, 30)  # Flower on the left
draw_flower(120, -50)  # Flower below right
draw_flower(-120, -50)  # Flower below left

# Draw leaves around the flowers
draw_leaves(80, 10)  # Leaves on the right
draw_leaves(-80, 10)  # Leaves on the left
draw_leaves(100, -40)  # Leaves below right
draw_leaves(-100, -40)  # Leaves below left

# Draw small hearts next to Harshu and Gokul
write_text("Harshu", 100, -130, font=("Times New Roman", 28, "bold"), color="darkred")
draw_small_heart(130, -160)  # Heart next to Harshu

write_text("Gokul", -100, -130, font=("Times New Roman", 28, "bold"), color="darkred")
draw_small_heart(-130, -160)  # Heart next to Gokul

# Draw a subtle floral border
pen.penup()
pen.goto(-180, 80)
pen.pendown()
pen.pensize(2)
pen.color("lightgray")
for _ in range(2):
    pen.forward(360)
    pen.left(90)
    pen.forward(220)
    pen.left(90)

# Draw a soft ribbon at the bottom
pen.penup()
pen.goto(-100, -150)
pen.pendown()
pen.color("lightblue")
pen.width(3)
pen.begin_fill()
pen.setheading(0)
pen.forward(200)
pen.right(90)
pen.circle(20, 180)
pen.right(90)
pen.forward(200)
pen.end_fill()

# Finish
pen.hideturtle()
screen.mainloop()