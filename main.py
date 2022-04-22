from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
race_on = True
user_choice = screen.textinput(title="make your bet", prompt="which turtle will win the race?")
position_Y = [70, 40, 10, -20, -50, -80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []

# creating 6 turtles
for index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=position_Y[index])
    turtle_list.append(new_turtle)

while race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 210:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_choice:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()