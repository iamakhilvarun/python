# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.


import tkinter

mainwindow=tkinter.Tk()

mainwindow.title('CALCULATOR')
mainwindow.geometry('600x400+600+200')

for i in range(0,4):
    mainwindow.columnconfigure(i,weight=1)
for i in range(0,6):
    mainwindow.rowconfigure(i,weight=1)

# Buttons

result=tkinter.Entry(mainwindow)
result.grid(row=0,column=0,columnspan=4,sticky='nsew')
result.config(border=2,relief='sunken')

tkinter.Button(mainwindow,text='C').grid(row=1,column=0,sticky='nsew')
tkinter.Button(mainwindow,text='CE').grid(row=1,column=1,sticky='nsew')
tkinter.Button(mainwindow,text='7').grid(row=2,column=0,sticky='nsew')
tkinter.Button(mainwindow,text='8').grid(row=2,column=1,sticky='nsew')
tkinter.Button(mainwindow,text='9').grid(row=2,column=2,sticky='nsew')
tkinter.Button(mainwindow,text='+').grid(row=2,column=3,sticky='nsew')
tkinter.Button(mainwindow,text='4').grid(row=3,column=0,sticky='nsew')
tkinter.Button(mainwindow,text='5').grid(row=3,column=1,sticky='nsew')
tkinter.Button(mainwindow,text='6').grid(row=3,column=2,sticky='nsew')
tkinter.Button(mainwindow,text='-').grid(row=3,column=3,sticky='nsew')
tkinter.Button(mainwindow,text='1').grid(row=4,column=0,sticky='nsew')
tkinter.Button(mainwindow,text='2').grid(row=4,column=1,sticky='nsew')
tkinter.Button(mainwindow,text='3').grid(row=4,column=2,sticky='nsew')
tkinter.Button(mainwindow,text='*').grid(row=4,column=3,sticky='nsew')
tkinter.Button(mainwindow,text='0').grid(row=5,column=0,sticky='nsew')
tkinter.Button(mainwindow,text='=').grid(row=5,column=1,columnspan=2,sticky='nsew')
tkinter.Button(mainwindow,text='/').grid(row=5,column=3,sticky='nsew')

number=''
expression=''
def button_click(number):
    result.insert(tkinter.END,str(number))

mainwindow.mainloop()