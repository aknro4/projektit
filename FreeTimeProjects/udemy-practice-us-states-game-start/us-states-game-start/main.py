import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_name = data["state"]

missed_states = {
    "state": state_name.tolist()
}


score = 0


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess state {score}/50", prompt="What is the state name")

    for state in state_name.tolist():
        if state.lower() in answer_state.lower():
            coor = data[data["state"] == state]
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(int(coor["x"]), int(coor["y"]))
            new_turtle.write(state)
            score += 1
            missed_states.get("state").remove(state)

    if answer_state == "exit":
        game_is_on = False

df = pandas.DataFrame(missed_states)
df.to_csv("missed_states")

