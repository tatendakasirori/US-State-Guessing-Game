from turtle import Turtle
import pandas as pd

class Writter(Turtle):
    def __init__(self,coord,state):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def name_state(self,coord,state):
        self.goto(coord)
        self.write(arg = state.capitalize())
