'''
@author Nikko Pang
@date 08.03.2022
@version 2.0

This is a simple calculator GUI with basic functionalities.
'''

from cmath import inf
from ctypes import alignment
from tkinter import Button, Label, StringVar, Tk
from turtle import width

class CalculatorGUI:

    # Creating the default variables required and the layout for the calculator.
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")

        # Creating the buttons and labels
        self.var1 = inf
        self.action = ""
        self.var2 = inf
        self.result = inf
        self.text = StringVar()
        self.text.set("Test")
        self.label = Label(master, textvariable = self.text, justify= "left")

        self.button1 = Button(master, text = "1", width=5, height=3, command= self.b1Action)
        self.button2 = Button(master, text = "2", width=5, height=3)
        self.button3 = Button(master, text = "3", width=5, height=3)
        self.button4 = Button(master, text = "4", width=5, height=3)
        self.button5 = Button(master, text = "5", width=5, height=3)
        self.button6 = Button(master, text = "6", width=5, height=3)
        self.button7 = Button(master, text = "7", width=5, height=3)
        self.button8 = Button(master, text = "8", width=5, height=3)
        self.button9 = Button(master, text = "9", width=5, height=3)
        self.button0 = Button(master, text = "0", width=5, height=3)
        self.buttonDot = Button(master, text = ".", width=5, height=3)

        self.buttonDivision = Button(master, text = "/", width=5, height=3)
        self.buttonMultiplication = Button(master, text = "*", width=5, height=3)
        self.buttonAddition = Button(master, text = "+", width=5, height=3)
        self.buttonSubtraction = Button(master, text = "-", width=5, height=3)
        self.buttonEqual = Button(master, text = "=", width=5, height=11)

        self.buttonDelete = Button(master, text = "c", width=5, height=3)
        self.buttonOff = Button(master, text = "OFF", command = master.quit, width=5, height=3)

        # Arranging in a grid
        self.label.grid(row=0, column=0, columnspan=5)
        
        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)

        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)

        self.buttonDelete.grid(row=4, column=0)
        self.button0.grid(row=4, column=1)
        self.buttonDot.grid(row=4, column=2)

        self.buttonDivision.grid(row=1, column=3)
        self.buttonMultiplication.grid(row=2, column=3)
        self.buttonAddition.grid(row=3, column=3)
        self.buttonSubtraction.grid(row=4, column=3)

        self.buttonOff.grid(row=1, column=4)
        self.buttonEqual.grid(row=2, column=4, rowspan=3)

    # Adds on "1" to the back of the number for either var1 or var2. It calls the updateLabel function.
    # var1 refers to the first number calculated
    # var2 refers to the second number calculated
    def b1Action(self):
        
        if self.action == "":
            # If there isn't any input yet.
            if self.var1 == 0 or self.var1 == inf:
                self.var1 = 1
            else:
                self.var1 = str(self.var1) + "1"
                self.var1 = int(self.var1)
        else:
            # If they already input their first number and action
            if self.var2 == 0 or self.var2 == inf:
                self.var2 = 1
            else:
                self.var2 = str(self.var2) + "1"
                self.var2 = int(self.var2)

        self.updateLabel()
        print("Var1:", self.var1, "action:", self.action, "var2:", self.var2)

    # 
    def updateLabel(self):
        if self.action == "":
            if self.var1 == inf:                # Just cleared the calculator.
                self.text.set("Nothing. (Test)")
            else:                               # If editting the first number.
                self.text.set(str(self.var1))
        



# The main code that runs the whole thing. 
root = Tk()
calculatorGUI = CalculatorGUI(root)
root.mainloop()