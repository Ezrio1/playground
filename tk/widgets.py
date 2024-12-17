from tkinter import *
from tkinter import ttk

def change(*args):
    try:
        afterward.set('text is changed')
        label.config(background="black", foreground="white")
    except ValueError:
        pass


root = Tk()

label = ttk.Label(root, text='Full name:') # create the label
label.grid(row=0, column=0) # than place if we dont do this label will not show up

frame = ttk.Frame(root, height=200, width=200) # setting up label
frame['padding'] = 50 # configure
frame['borderwidth'] = 10
frame['relief'] = 'sunken'

frame.grid(row=0,column=1) # than place it

# afterward we can change label text
afterward = StringVar()
label['textvariable'] = afterward
afterward.set('New value to display')
#extra
ttk.Button(text='change the text', width=50, command=change).grid(row=1,column=0)

"""
This is way to display a image
image = PhotoImage(file = 'myimage.gif') 
label['image'] = image  
"""

root.mainloop()
