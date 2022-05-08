'''
@author Nikko Pang
@date 08.03.2022
@version 3.0

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
        self.text.set("")
        self.label = Label(master, textvariable = self.text, justify= "left")

        self.button1 = Button(master, text = "1", width=5, height=3, command= self.b1Action)
        self.button2 = Button(master, text = "2", width=5, height=3, command = self.b2Action)
        self.button3 = Button(master, text = "3", width=5, height=3, command = self.b3Action)
        self.button4 = Button(master, text = "4", width=5, height=3, command = self.b4Action)
        self.button5 = Button(master, text = "5", width=5, height=3, command = self.b5Action)
        self.button6 = Button(master, text = "6", width=5, height=3, command = self.b6Action)
        self.button7 = Button(master, text = "7", width=5, height=3, command = self.b7Action)
        self.button8 = Button(master, text = "8", width=5, height=3, command = self.b8Action)
        self.button9 = Button(master, text = "9", width=5, height=3, command = self.b9Action)
        self.button0 = Button(master, text = "0", width=5, height=3, command = self.b0Action)
        self.buttonDot = Button(master, text = ".", width=5, height=3, command = self.dotAction)

        self.buttonDivision = Button(master, text = "/", width=5, height=3, command = self.divideButtonAction)
        self.buttonMultiplication = Button(master, text = "*", width=5, height=3, command = self.multiplyButtonAction)
        self.buttonAddition = Button(master, text = "+", width=5, height=3, command = self.addButtonAction)
        self.buttonSubtraction = Button(master, text = "-", width=5, height=3, command = self.minusButtonAction)
        self.buttonEqual = Button(master, text = "=", width=5, height=11, command = self.equalAction)

        self.buttonDelete = Button(master, text = "c", width=5, height=3, command = self.clearAction)
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

    # All actions buttons are to call the appropriate calculator button function
    def dotAction(self):
        self.numberAction('.')

    def b1Action(self):
        num = 1
        self.numberAction(num)

    def b2Action(self):
        num = 2
        self.numberAction(num)

    def b3Action(self):
        num = 3
        self.numberAction(num)
    
    def b4Action(self):
        num = 4
        self.numberAction(num)
    
    def b5Action(self):
        num = 5
        self.numberAction(num)

    def b6Action(self):
        num = 6
        self.numberAction(num)

    def b7Action(self):
        num = 7
        self.numberAction(num)

    def b8Action(self):
        num = 8
        self.numberAction(num)

    def b9Action(self):
        num = 9
        self.numberAction(num)

    def b0Action(self):
        num = 0
        self.numberAction(num)

    def addButtonAction(self):
        self.action = "+"
        self.updateLabel(2)

    def minusButtonAction(self):
        self.action = "-"
        self.updateLabel(2)
        
    def divideButtonAction(self):
        self.action = "/"
        self.updateLabel(2)
    
    def multiplyButtonAction(self):
        self.action = "*"
        self.updateLabel(2)

    # Adds on "1" to the back of the number for either var1 or var2. It calls the updateLabel function.
    # var1 refers to the first number calculated
    # var2 refers to the second number calculated
    def numberAction(self, num):
        
        if self.action == "":
            # If there isn't any input yet.
            if self.var1 == 0 or self.var1 == inf:
                if num == '.': # Handles decimal input
                    self.var1 = '0.' 
                else: 
                    self.var1 = num
            else:
                    self.var1 = str(self.var1) + str(num) # Adds numbers on top of each other
                    self.var1 = self.var1
            
            self.updateLabel(1)
        
        else:
            # Edits the second variable if they already input their first number and action
            if self.var2 == 0 or self.var2 == inf:
                if num == '.':  # Handles decimal numbers
                    self.var2 = '0.'
                else: 
                    self.var2 = num
            else:
                self.var2 = str(self.var2) + str(num)
                self.var2 = self.var2
            
            self.updateLabel(3)

        print("Var1:", self.var1, "action:", self.action, "var2:", self.var2)

    # This updates the number on the user interface to show the current numbers.
    def updateLabel(self, phase):
        if phase == 1: # Changing var1
            self.text.set(str(self.var1))
        elif phase == 2: # Changing action
            if self.var2 != inf:
                print("Can only calculate 2 numbers at a time.")
            else:
                userOutput = str(self.var1) + " " + self.action
                self.text.set(userOutput)
        elif phase == 3: # Changing 2nd variable
            userOutput = str(self.var1) + " " + self.action + " " + str(self.var2)
            self.text.set(userOutput)
        elif phase == 4:
            self.text.set(self.result)
        else:
            self.text.set("")

    # Deleting the previous button 
    def clearAction(self):
        if self.result != inf: # If all calculations are done, reset to default.
            self.var1 = inf
            self.action = ""
            self.var2 = inf
            self.result = inf
            self.updateLabel(5)
        
        elif len(str(self.var2)) == 1 or self.var2 == inf:
                self.var2 = inf     # Clear the 2nd variable
                self.updateLabel(2)

        elif self.var2 != inf: # If already wrote the second number, indicating deleting second number.
            self.var2 = self.var2[:-1] # Delete a number from the 2nd variable
            self.updateLabel(3)

        elif self.action != "": # If changing the action
            self.action = ""
            self.updateLabel(1)

        else:
            if len(str(self.var1)) == 1 or self.var1 == inf:
                self.var1 = inf     # Clear the 1st variable completely. Reset to default
                self.updateLabel(5)
            else:
                tempV2 = self.var1[:-1] # Delete a number from the 1st variable
                self.updateLabel(1)

    def equalAction(self):
        total = 0
        if (self.var1 != inf and self.var2 != inf):
            if self.action == "+":
                total = float(self.var1) + float(self.var2)
            elif self.action == "-":
                total = float(self.var1) - float(self.var2)
            elif self.action == "*":
                total = float(self.var1) * float(self.var2)
            else:
                total = float(self.var1) / float(self.var2)
        self.result = total
        self.updateLabel(4)

# The main code that runs the whole thing. 
root = Tk()
calculatorGUI = CalculatorGUI(root)
root.mainloop()
