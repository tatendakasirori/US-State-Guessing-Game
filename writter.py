from turtle import Turtle
import pandas as pd

class Writter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.correct = 0
        
    def name_state(self,coord,state,w_color = "black"):
        if w_color:
            self.color(w_color)
        self.goto(coord)
        self.write(arg = state.title(), font= ("Arial", 8, "bold"))
