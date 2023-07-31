from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

outfit = []
#buttons to choose which part of the outfit to select
shirt1 = "Shirts/shirt1.png"
shirt2 = "Shirts/shirt2.png"
jacket1 = "Jackets/jacket1.png"
jacket2 = "Jackets/jacket2.png"

def chosenShirt1():
    print("Chosen 1")
    outfit.append(shirt1)
def chosenShirt2():
    print("Chosen 2")
    outfit.append(shirt2)
def chosenJacket1():
    print("Chosen 1")
    outfit.append(jacket1)
def chosenJacket2():
    print("Chosen 2")
    outfit.append(jacket2)
    


print("Welcome to your Outfit Maker")
print("You will choose your outfit from top to bottom")
print("First, let's start with the shirt")


# Creating a photoimage object to use image
#SHIRTS
window = Tk()
window.title("Outfit Maker / Shirt selection")

shirt1PH = ImageTk.PhotoImage(Image.open(shirt1))
shirt1BUTT = Button(window, text = 'Shirt 1', image = shirt1PH, compound = TOP, command=chosenShirt1).grid(row=0, column=0)

shirt2PH = ImageTk.PhotoImage(Image.open(shirt2)) 
shirt2BUTT = Button(window, text = 'Shirt 2', image = shirt2PH, compound = TOP, command=chosenShirt2).grid(row=0, column=1)

nextBUTT = Button(window, text = "Next", command = window.destroy).grid(row=2, column=2)
window.mainloop()

#JACKETS
window = Tk()
window.title("Outfit Maker / Jacket selection")

jacket1PH = ImageTk.PhotoImage(Image.open(jacket1))
jacket1BUTT = Button(window, text = 'Jacket 1', image = jacket1PH, compound = TOP, command=chosenJacket1).grid(row=0, column=0)

jacket2PH = ImageTk.PhotoImage(Image.open(jacket2))
jacket1BUTT = Button(window, text = 'Jacket 2', image = jacket2PH, compound = TOP, command=chosenJacket2).grid(row=0, column=1)

nextBUTT = Button(window, text = "Next", command = window.destroy).grid(row=2, column=2)
window.mainloop()


print(outfit)
