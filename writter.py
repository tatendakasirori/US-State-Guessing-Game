from turtle import Turtle
import pandas as pd

class Writter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.correct = 0
        
    def name_state(self,coord,state):
        self.goto(coord)
        self.write(arg = state.capitalize())
