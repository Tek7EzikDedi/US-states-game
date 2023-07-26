import turtle
import pandas as pd
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pd.read_csv("50_states.csv")

state_list = data.state.to_list()

x_list = data.x.to_list()
y_list = data.y.to_list()

guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    if answer_state is None:
        break
    answer_state = answer_state.title()

    if answer_state in state_list:
        guessed_states.append(answer_state)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        tim.write(state_data.state.item())

x_pos = []
y_pos = []

for i in state_list:
    if i not in guessed_states:
        s_data = data[data.state == i]
        x = s_data.x.item()
        x_pos.append(x)
        y = s_data.y.item()
        y_pos.append(y)

data_dict = {
    "state": state_list,
    "x": x_pos,
    "y": y_pos,
}

csv = pd.DataFrame(data_dict)
csv.to_csv("remaining_states.csv")
