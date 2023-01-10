from tkinter import *
from View import View
from Controller import Controller
from Model import Model

class App():
    def __init__(self):               
        root = Tk()
        root.title("CRUD c/ Python")
        Controller(Model("tbIdSensor"), View(root))
        root.mainloop()

app = App()