from tkinter import*

root=Tk()


def myClick():
	myLabel=Label(root,text="Look! I Clicked a Button!!")
	myLabel.pack()

	

#myButton=Button(root,text="click me!",state=DISABLED)

#myButton=Button(root,text="click me!",padx=50)

#myButton=Button(root,text="click me!",pady=50)


#myButton=Button(root,text="click me!",padx=50,pady=50)

#myButton=Button(root,text="Click me!",command=myClick)
myButton=Button(root,text="Click me!",command=myClick,fg="blue",bg="#ffffff")
myButton.pack()


root.mainloop()
