from tkinter import *

glb = "#767676"
counter = 0


def thiz_iz_da_kommand():
    global counter
    arr = list(ent.get())
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[len(arr)-i-1])
    newtxt = ''.join(newarr)
    #print(newtxt)
    ent.delete(0, len(arr))
    ent.insert(0, newtxt)
    counter += 1
    if(counter > 1):
        counter = 0
    if(counter == 1):
        root.title("esrever")
    else:
        root.title("reverse")


def clr():
    ent.delete(0, len(list(ent.get())))
    root.title("")


root = Tk()
root.configure(bg = "#4586db")
root.resizable(False, False)
root.title("reverse")
booton = Button(root, text = "rev", fg = "#ffffff", bg = glb, command = thiz_iz_da_kommand, padx = 10, borderwidth = 0)
booton.pack(side = LEFT)
booton1 = Button(root, text = "clr", fg = "#ffffff", bg = glb, command = clr, padx = 10, borderwidth = 0)
booton1.pack(side = RIGHT)
ent = Entry(root, width=100, bg = "#4586db", fg = "#ffffff", borderwidth = 0)
ent.pack()
root.mainloop()
