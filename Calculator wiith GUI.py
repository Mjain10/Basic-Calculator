from tkinter import *
import math

window = Tk()
window.title('Python Calculator')
window.configure(background = "pale turquoise")


def add():
    n = int(entry.get())
    n2 = int(entry2.get())
    answer['text'] = n + n2

def subtract():
    n = int(entry.get())
    n2 = int(entry2.get())
    answer['text'] = n - n2

def multiply():
    n = int(entry.get())
    n2 = int(entry2.get())
    answer['text'] = n * n2

def divide():
    n = int(entry.get())
    n2 = int(entry2.get())
    answer['text'] = n/n2

def exponential():
    n = int(entry.get())
    n2 = int(entry2.get())
    answer['text'] = n ** n2

def remainder():
    n = int(entry.get())
    n2 = int(entry2.get())
    answer['text'] = n % n2
    

answer = Label(window, bg = "pale turquoise", text = 'Answer', font = ("Comic Sans MS", 15))
answer.pack(side = BOTTOM, fill=BOTH, expand=YES)

##First Number entry box and label
entry = Entry(window, width = 10, bg = "alice blue", font = ("Comic Sans MS", 20))
entry.pack(side = TOP, fill=BOTH, expand=YES)

label_n = Label(window, bg = "pale turquoise", font = ("Comic Sans MS", 10), text = 'First Number')
label_n.pack(side = TOP, fill=BOTH, expand=YES)

##Second Number entry box and label
entry2 = Entry(window, width = 10, bg = "alice blue", font = ("Comic Sans MS", 20))
entry2.pack(side = BOTTOM, fill=BOTH, expand=YES)

label_n2 = Label(window, bg = "pale turquoise", font = ("Comic Sans MS", 10), text = 'Second Number')
label_n2.pack(side = BOTTOM, fill=BOTH, expand=YES)

##Functions
b_add = Button(window, fg = 'black', text = '+', font = ("Comic Sans MS", 20), command = add)  
b_add.pack(side = RIGHT, fill=BOTH, expand=YES)

b_sub = Button(window, fg = 'black', text = '-', font = ("Comic Sans MS", 20), command = subtract)  
b_sub.pack(side = RIGHT, fill=BOTH, expand=YES)

b_mul = Button(window, fg = 'black', text = 'x', font = ("Comic Sans MS", 20), command = multiply)  
b_mul.pack(side = RIGHT, fill=BOTH, expand=YES)

b_div = Button(window, fg = 'black', text = '/', font = ("Comic Sans MS", 20), command = divide)  
b_div.pack(side = RIGHT, fill=BOTH, expand=YES)

b_r = Button(window, fg = 'black', text = 'R', font = ("Comic Sans MS", 20), command = remainder)  
b_r.pack(side = RIGHT, fill=BOTH, expand=YES)

b_ex = Button(window, fg = 'black', text = '^', font = ("Comic Sans MS", 20), command = exponential)  
b_ex.pack(side = RIGHT, fill=BOTH, expand=YES)

window.mainloop()
