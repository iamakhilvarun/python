import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("CALCULATOR")
mainwindow.geometry("600x400+600+200")

for i in range(4):
    mainwindow.columnconfigure(i, weight=1)

for i in range(6):
    mainwindow.rowconfigure(i, weight=1)


# ---------------- Functions ----------------

def button_click(value):
    result.insert(tkinter.END, value)


def clear():
    result.delete(0, tkinter.END)


def clear_last():
    text = result.get()
    result.delete(0, tkinter.END)
    result.insert(0, text[:-1])


def calculate():
    expression = result.get()

    try:
        answer = eval(expression)
        result.delete(0, tkinter.END)
        result.insert(0, str(answer))
    except:
        result.delete(0, tkinter.END)
        result.insert(0, "Error")


def zero():
    button_click("0")


def one():
    button_click("1")


def two():
    button_click("2")


def three():
    button_click("3")


def four():
    button_click("4")


def five():
    button_click("5")


def six():
    button_click("6")


def seven():
    button_click("7")


def eight():
    button_click("8")


def nine():
    button_click("9")


def plus():
    button_click("+")


def minus():
    button_click("-")


def multiply():
    button_click("*")


def divide():
    button_click("/")


# ---------------- Entry ----------------

result = tkinter.Entry(mainwindow)
result.grid(row=0, column=0, columnspan=4, sticky="nsew")
result.config(border=2, relief="sunken")

# ---------------- Buttons ----------------

tkinter.Button(mainwindow, text="C", command=clear).grid(row=1, column=0, sticky="nsew")
tkinter.Button(mainwindow, text="CE", command=clear_last).grid(row=1, column=1, sticky="nsew")

tkinter.Button(mainwindow, text="7", command=seven).grid(row=2, column=0, sticky="nsew")
tkinter.Button(mainwindow, text="8", command=eight).grid(row=2, column=1, sticky="nsew")
tkinter.Button(mainwindow, text="9", command=nine).grid(row=2, column=2, sticky="nsew")
tkinter.Button(mainwindow, text="+", command=plus).grid(row=2, column=3, sticky="nsew")

tkinter.Button(mainwindow, text="4", command=four).grid(row=3, column=0, sticky="nsew")
tkinter.Button(mainwindow, text="5", command=five).grid(row=3, column=1, sticky="nsew")
tkinter.Button(mainwindow, text="6", command=six).grid(row=3, column=2, sticky="nsew")
tkinter.Button(mainwindow, text="-", command=minus).grid(row=3, column=3, sticky="nsew")

tkinter.Button(mainwindow, text="1", command=one).grid(row=4, column=0, sticky="nsew")
tkinter.Button(mainwindow, text="2", command=two).grid(row=4, column=1, sticky="nsew")
tkinter.Button(mainwindow, text="3", command=three).grid(row=4, column=2, sticky="nsew")
tkinter.Button(mainwindow, text="*", command=multiply).grid(row=4, column=3, sticky="nsew")

tkinter.Button(mainwindow, text="0", command=zero).grid(row=5, column=0, sticky="nsew")
tkinter.Button(mainwindow, text="=", command=calculate).grid(row=5, column=1, columnspan=2, sticky="nsew")
tkinter.Button(mainwindow, text="/", command=divide).grid(row=5, column=3, sticky="nsew")

mainwindow.mainloop()