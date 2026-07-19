try:
    import tkinter
except ImportError:
    import Tkinter as tkinter  # not nessassry to write ==> for python 2
import os

mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry("640x480+600+200")


label = tkinter.Label(mainwindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# Configure Grid
mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1)
mainwindow.columnconfigure(3, weight=1)
mainwindow.columnconfigure(4, weight=1)

mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

# =======================
# Listbox Starts Here
# =======================
filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1, column=0, sticky="nsew", rowspan=2)
filelist.config(border=2, relief="sunken")
for zone in os.listdir("C:/windows/system32"):
    filelist.insert(
        tkinter.END, zone
    )  # put it at the end of the list then loop continues


# =======================
# Scrollbar Starts Here
# =======================
listscroll = tkinter.Scrollbar(
    mainwindow, orient=tkinter.VERTICAL, command=filelist.yview
)
# filelist.yview ==> "When the user moves me, tell the Listbox to scroll vertically."
listscroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
# Listbox updates the Scrollbar position
filelist["yscrollcommand"] = listscroll.set

# frame of radio buttons
optionframe = tkinter.LabelFrame(mainwindow, text="File Details")
optionframe.grid(row=1, column=2, sticky="ne")

rbvalue = tkinter.IntVar()
rbvalue.set(1)  # this sets the default value of rbvalue to 1
# Radio buttons
radio1 = tkinter.Radiobutton(optionframe, text="Filename", value=1, variable=rbvalue)
radio2 = tkinter.Radiobutton(optionframe, text="Path", value=2, variable=rbvalue)
radio3 = tkinter.Radiobutton(optionframe, text="Timestamp", value=3, variable=rbvalue)
radio1.grid(row=0, column=1, sticky="w")
radio2.grid(row=1, column=1, sticky="w")
radio3.grid(row=2, column=1, sticky="w")

# Result box (widget to dispay the result)
resultLabel = tkinter.Label(mainwindow, text="Result")
resultLabel.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky="sw")


# Frame for time spinners
timeframe = tkinter.LabelFrame(mainwindow, text="Time")
timeframe.grid(row=3, column=0, sticky="new")
# Timespinners
hourspinner = tkinter.Spinbox(timeframe, width=2, values=tuple(range(0, 24)))
minutespinner = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
secondspinner = tkinter.Spinbox(timeframe, width=2, from_=0 ,to = 59)
hourspinner.grid(row=0,column=0)
tkinter.Label(timeframe,text=':').grid(row=0,column=1)
minutespinner.grid(row=0,column=2)
tkinter.Label(timeframe,text=':').grid(row=0,column=3)
secondspinner.grid(row=0,column=4)
timeframe['padx']=36


# Frame for the date spinners
dateFrame=tkinter.Frame(mainwindow)
dateFrame.grid(row=4,column=0,sticky='new')
# Date labels
dayLabels=tkinter.Label(dateFrame,text='Day')
monthLabels=tkinter.Label(dateFrame,text='Month')
yearLabels=tkinter.Label(dateFrame,text='Year')
dayLabels.grid(row=0,column=0,sticky='w')
monthLabels.grid(row=0,column=1,sticky='w')
yearLabels.grid(row=0,column=2,sticky='w')
# Date spinners
dayspin=tkinter.Label(dateFrame,width=5,from_=1,to=31)
monthspin=tkinter.Label(dateFrame,width=5,values=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
yearspin=tkinter.Label(dateFrame,width=5,from_=2000,to=2099)
dayspin.grid(row=1,column=0)
monthspin.grid(row=1,column=1)
yearspin.grid(row=1,column=2)
mainwindow.mainloop()
print(rbvalue.get())
