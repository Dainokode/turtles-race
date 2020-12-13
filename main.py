from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# Make bet
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race?")

# Create turtles
colors = ["red", "blue", "pink", "orange"]
coordinates_y = [0, 30, 60, 90]


for turtle_index in range(0, 4):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(-240, coordinates_y[turtle_index])


screen.exitonclick()
