from tkinter import *
import random


def thiz_iz_da_kommand():
    arr = list(ent.get())
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[len(arr)-i])
    label.config(str(newarr))


root = Tk()
root.geometry("300x500")
root.resizable(False, True)
root.title("1, #ff0000")
booton = Button(root, text = "1", fg = "#00ffff", bg = "#ff0000", command = thiz_iz_da_kommand, width = 39)
booton.pack()
ent = Entry(root)
ent.pack()
lab = Label(root, text="l9ug")
root.mainloop()
