"""
Today,we are creating a Ludu Dice.
Language:Python,
required Modules:tkinter,pillow,random.
Let's start....
"""

#first of all import requred modules.

from tkinter import *
from PIL import Image,ImageTk
from random import randint

#global variables.

root=Tk()
diceNumber = randint(1,6)
diceSide=ImageTk.PhotoImage(Image.open(f"{diceNumber}.png"))
diceLabel=Label(root,image=diceSide)

#The rollDice function  display the dice.

def rollDice():
    global diceNumber,diceSide,diceLabel
    diceNumber=randint(1,6)
    diceSide=ImageTk.PhotoImage(Image.open(f"{diceNumber}.png"))
    diceLabel.pack_forget()
    diceLabel=Label(root,image=diceSide)
    diceLabel.pack()

#main function where the base of the application.

def main(name,bgColor="black"):
    #customize the window.
    
    root.title(name)
    
    """
    Creating The Button.
    if user click the Button the dice is Roll. 
    """
    
    rollButton=Button(root,text="Roll Dice",command=rollDice)
    rollButton.pack()
    
    #pack the Dice Label                           
    
    diceLabel.pack()
    
    #running the loop of window and change color.
    
    root.config(bg=bgColor)
    root.mainloop()

#run the dice program from this file.

if __name__=='__main__':
    
    #call the main function with the name : "---Ludu Dice---"
    
    main('"---Ludu-Dice---"',"white")            

"""
About Coder:
    Name:Redoan Saleh.
    Age:13.
    School:B.O.F High School.
    Class:7.
About Code:
    Date when start:Sunday,14 March 2021.
©redocode    
"""                                                        