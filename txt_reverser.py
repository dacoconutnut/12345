from tkinter import *


def thiz_iz_da_kommand():
    arr = list(ent.get())
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[len(arr)-i-1])
    newtxt = ''.join(newarr)
    print(newtxt)
    ent.delete(0, len(arr))
    ent.insert(0, newtxt)


root = Tk()
root.resizable(True, True)
root.title("reverse")
booton = Button(root, text = "reverse", fg = "#ffffff", bg = "#000000", command = thiz_iz_da_kommand)
booton.pack()
ent = Entry(root, width=100)
ent.pack()
root.mainloop()
