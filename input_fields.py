from tkinter import*
root=Tk()

#e=Entry(root,width=50,bg="blue",fg="white")
#e=Entry(root,width=50,borderwidth=5)
e=Entry(root,width=50,)

e.pack()
e.insert(0,"Enter your Name: ")

def myClick():
	hello="Hello" + e.get()
	myLabel=Label(root,text=hello)
	myLabel.pack()

myButton=Button(root,text="Enter your stack quote:",command=myClick)
myButton.pack()


root.mainloop()