from turtle import Turtle, Screen
import random

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# Make bet
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race?")

# Create turtles
colors = ["red", "blue", "pink", "orange"]
coordinates_y = [0, 30, 60, 90]
turtles_list = []

is_race_on = False


for turtle_index in range(0, 4):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(-230, coordinates_y[turtle_index])
    turtles_list.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_ in turtles_list:
        if turtle_.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                print(f"You've won, {winning_color} arrived first!")
            else:
                print(f"You've lost, {winning_color} arrived first!")

        random_distance = random.randint(0, 10)
        turtle_.forward(random_distance)


screen.exitonclick()
