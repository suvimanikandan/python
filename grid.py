from tkinter import*

root=Tk()
#creating a label widget
myLabel1=Label(root,text="Hello world!")
myLabel2=Label(root,text="My name is swetha")
myLabel3=Label(root,text="")


#showimg in onto the screen

myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=0)
#myLabel2.grid(row=1,column=1)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=1)

root.mainloop()