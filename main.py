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
        if answer.lower() == state.lower():
            coord = (int(DATA[DATA.state == answer].x), int(DATA[DATA.state == answer].y))
            return coord
    return False


game_on = True
while game_on:
    answer = screen.textinput(title= f"{writter.correct}/50", prompt= "What's another state's name?")
    coord = find_state(answer)
    if coord != False:
        writter.name_state(coord,answer)
        writter.correct += 1
       
t.mainloop()







