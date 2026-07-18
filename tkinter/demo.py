try:
    import tkinter
except ImportError:
     import Tkinter as tkinter # not nessassry to write ==> for python 2

mainwindow= tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry('640x480+600+200')

label=tkinter.Label(mainwindow,text="Hello world")
label.pack(side="top")

leftframe=tkinter.Frame(mainwindow)
leftframe.pack(side='left',anchor='n',fill=tkinter.Y,expand=False)

canvas=tkinter.Canvas(leftframe,relief='raised',borderwidth=1)
canvas.pack(side='left',anchor='n')

rightframe=tkinter.Frame(mainwindow)
rightframe.pack(side='right',anchor='n',expand=True)

button1=tkinter.Button(rightframe,text='button 1')
button2=tkinter.Button(rightframe,text='button 2')
button3=tkinter.Button(rightframe,text='button 3')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainwindow.mainloop()