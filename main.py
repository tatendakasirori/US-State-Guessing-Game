import pandas as pd
import turtle as t
from writter import Writter

screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)


DATA = pd.read_csv("50_states.csv")
writter = Writter()

def find_state(answer):
    for state in DATA.state:
        if answer == state:
            coord = (int(DATA[DATA.state == answer].x), int(DATA[DATA.state == answer].y))
            return coord
    return False


guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title= f"{writter.correct}/50", prompt= "What's another state's name?")
    answer = answer.title()
    if answer.lower() == "exit":
        missing_states = []
        for state in DATA.state:
            if state not in guessed_states:
                missing_states.append(state)
        mis_states_df = pd.DataFrame(missing_states,columns=["state"])
        mis_states_csv = mis_states_df.to_csv("missed.csv")
        break
    coord = find_state(answer)
    if coord != False:
        writter.name_state(coord,answer)
        writter.correct += 1
        if answer not in guessed_states: guessed_states.append(answer)

m_states = pd.read_csv("missed.csv")

for state in m_states.state:
    coord = find_state(state)
    if coord != False:
            writter.name_state(coord,state,w_color = 'red')
t.mainloop()







