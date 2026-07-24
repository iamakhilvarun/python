try:
    import tkinter
except ImportError:
     import Tkinter as tkinter # not nessassry to write ==> for python 2

mainwindow= tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry('640x480+600+200')

label=tkinter.Label(mainwindow,text="Hello world")

label.grid(row=0,column=0)

leftframe=tkinter.Frame(mainwindow)
leftframe.grid(row=1,column=1)

canvas=tkinter.Canvas(leftframe,relief='raised',borderwidth=1)
canvas.grid(row=1,column=0)

rightframe=tkinter.Frame(mainwindow)
rightframe.grid(row=1,column=2,sticky='n')

button1=tkinter.Button(rightframe,text='button 1')
button2=tkinter.Button(rightframe,text='button 2')
button3=tkinter.Button(rightframe,text='button 3')

button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)

#column configure
mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.grid_columnconfigure(2,weight=1)

leftframe.config(relief='sunken',borderwidth=1)
rightframe.config(relief='sunken',borderwidth=1)
leftframe.grid(sticky='ns')
rightframe.grid(sticky='new')

rightframe.columnconfigure(0,weight=1)
button2.grid(sticky='ew') # due to weight it doesnt work
mainwindow.mainloop()
print("Tkinter version:", tk.TkVersion)

root = tk.Tk()
root.title("Test")
root.mainloop()
