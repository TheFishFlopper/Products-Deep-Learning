from tkinter import *
from tkinter import scrolledtext, font
import random


# Button command
def buttonCommand():
    textInput = reviewInput.get('1.0', 'end-1c')
    print(textInput)
    starNum = random.randint(1, 5)
    stars.config(text='★' * starNum)

# Create window
root = Tk()

root.title('Ratings AI')
root.geometry('950x600')
root.minsize(700, 500)

# Fonts
titleFont = font.Font(family="Lucida Console", size=18, weight='bold')
instructionsFont = font.Font(family="Lucida Console", size=14)
textFont = font.Font(family="Calibri", size=12)
buttonFont = font.Font(family="Lucida Console", size=12)

# UI Elements
frame = Frame(root, bd=0, bg='white')
frame.place(relx=0, rely=0, relheight=1, relwidth=1)

title = Label(frame, text='Review Rating Suggester', font=titleFont, bg='white')
title.place(relx=0.5, rely=0.125, width=500, y=-18, x=-250)

instructions = Label(frame, text='Write a review and we\'ll suggest a rating:', font=instructionsFont, bg='white')
instructions.place(relx=0.5, rely=0.25, width=500, y=-30, x=-250)

reviewInput = scrolledtext.ScrolledText(frame, undo=True, padx=10, pady=10, bd=3, relief=GROOVE)
reviewInput.configure(font=textFont)
reviewInput.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

goButton = Button(frame, text='Go', font=buttonFont, command=buttonCommand)
goButton.place(relx=0.5, rely=0.75, width=200, y=10, x=-100, height=25)

stars = Label(frame, text='', font=('bold', 30), fg='#FFA41D', bg='white')
stars.place(relx=0.5, rely=0.875, width=200, y=-15, x=-100)

# Run application
root.mainloop()
