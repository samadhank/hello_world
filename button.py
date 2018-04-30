from Tkinter import *

def sel():
    selection ="You selected option " + str(val.get())
    label.config(text=selection)

root=Tk()
val = IntVar()
R1 = Radiobutton(root,text="Option 1",variable=val,value=1,command=sel)
R1.pack(anchor = W)
R2 = Radiobutton(root,text="Option 2",variable=val,value=2,command=sel)
R2.pack(anchor = W)
R3= Radiobutton(root,text="Option 3",variable=val,value=3,command=sel)
R3.pack(anchor = W)
label = Label(root)
label.pack()
root.mainloop()
