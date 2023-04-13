import tkinter as tk
import time

# Starting Tkinter and setting button height/width
win = tk.Tk()
win.title("Calculator")
win.geometry("323x315")
buttonHEIGHT = 2
buttonWIDTH = 10
store = 0
display = 0
operator = None
# Commands for buttons    
def CLEARALL():
    global store, display, operator
    store, display, operator = 0, 0, None
    calcDisplay.config(text=display)
    storeDisplay.config(text=store)
def BACK():
    global display
    temp = str(display)[:-1]
    if "." in temp:
        display = float(temp)
    else:
        display = int(temp)
    calcDisplay.config(text=display)
def ONE():
    global display
    if display == 0:
        display = 1
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "1"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def TWO():
    global display
    if display == 0:
        display = 2
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "2"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def THREE():
    global display
    if display == 0:
        display = 3
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "3"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def FOUR():
    global display
    if display == 0:
        display = 4
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "4"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def FIVE():
    global display
    if display == 0:
        display = 5
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "5"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def SIX():
    global display
    if display == 0:
        display = 6
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "6"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def SEVEN():
    global display
    if display == 0:
        display = 7
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "7"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def EIGHT():
    global display
    if display == 0:
        display = 8
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "8"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def NINE():
    global display
    if display == 0:
        display = 9
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "9"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)
def ZERO():
    global display
    if display == 0:
        display = 0
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "0"
        if "." in temp:
            display = float(temp)
        else:
            display = int(temp)
        calcDisplay.config(text=display)  
def DECIMAL():
    global display
    if display == 0:
        display = "0."
        calcDisplay.config(text=display)
    else:
        temp = str(display) + "."
        display = temp
        calcDisplay.config(text=display)
def ADD():
    global store, display, operator
    if operator == None:
        store = display
        display = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
        operator = "ADD"
    else:
        if type(store) == float or type(display) == float:
            end = float(store) + float(display)
            display = end
            store = 0
        else:
            end = store + display
            display = end
            store = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
def SUB():
    global store, display, operator
    if operator == None:
        store = display
        display = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
        operator = "SUB"
    else:
        if type(store) == float or type(display) == float:
            end = float(store) - float(display)
            display = end
            store = 0
        else:
            end = store - display
            display = end
            store = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
def MULTI():
    global store, display, operator
    if operator == None:
        store = display
        display = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
        operator = "MULTI"
    else:
        if type(store) == float or type(display) == float:
            end = float(store) * float(display)
            display = end
            store = 0
        else:
            end = store * display
            display = end
            store = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")    
def DIV():
    global store, display, operator
    if operator == None:
        store = display
        display = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
        operator = "DIV"
    else:
        if display == 0:
            calcDisplay.config(text="ERROR: CAN'T DIVIDE BY ZERO")
            store = 0
            storeDisplay.config(text=store)
        if type(store) == float or type(display) == float:
            end = float(store) / float(display)
            display = end
            store = 0
        else:
            end = store / display
            if ".0" in str(end):
                temp = str(end)[:-2]
                display = int(temp)
            else:
                display = end
            store = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
def MODU():
    global store, display, operator
    if operator == None:
        store = display
        display = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
        operator = "MODU"
    else:
        if type(store) == float or type(display) == float:
            end = float(store) % float(display)
            display = end
            store = 0
        else:
            end = store % display
            display = end
            store = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
def EXPON():
    global store, display, operator
    if operator == None:
        store = display
        display = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")
        operator = "EXPON"
    else:
        if type(store) == float or type(display) == float:
            end = float(store) ** float(display)
            display = end
            store = 0
        else:
            end = store ** display
            display = end
            store = 0
        calcDisplay.config(text=display)
        storeDisplay.config(text=f"Storing Value: {store}")   
def RECIP():
    global display
    if display == 0:
        display = "ERROR: CAN'T DIVIDE BY ZERO"
        calcDisplay.config(text=display)
    else:
        temp = 1 / display
        display = temp
        calcDisplay.config(text=display)
def PLUSMINUS():
    global display
    temp = display * -1
    display = temp
    calcDisplay.config(text=display)
def SQRT():
    global display
    temp = display ** 0.5
    if ".0" in str(temp):
        pmet = str(temp)[:-2]
        display = int(pmet)
    else:
        display = temp
    calcDisplay.config(text=display)
def EQUAT():
    global operator
    if operator == "ADD":
        ADD()
        operator = None
    elif operator == "SUB":
        SUB()
        operator = None
    elif operator == "MULTI":
        MULTI()
        operator = None
    elif operator == "DIV":
        DIV()
        operator = None
    elif operator == "MODU":
        MODU()
        operator = None
    elif operator == "EXPON":
        EXPON()
        operator = None

# Making the screen
calcDisplay = tk.Label(win, text=f"{display}", height= buttonHEIGHT, width=4*buttonWIDTH, anchor="e")
calcDisplay.grid(column=0, row=0, columnspan=4)

storeDisplay = tk.Label(win, text=f"Storing Value: {store}", height=buttonHEIGHT, width=4*buttonWIDTH, anchor="e")
storeDisplay.grid(column=0, row=7, columnspan=4)

# Making the buttons we will need
one = tk.Button(win, text="1", height= buttonHEIGHT, width=buttonWIDTH, command=ONE)
two = tk.Button(win, text="2", height= buttonHEIGHT, width=buttonWIDTH, command=TWO)
three = tk.Button(win, text="3", height= buttonHEIGHT, width=buttonWIDTH, command=THREE)
four = tk.Button(win, text="4", height= buttonHEIGHT, width=buttonWIDTH, command=FOUR)
five = tk.Button(win, text="5", height= buttonHEIGHT, width=buttonWIDTH, command=FIVE)
six = tk.Button(win, text="6", height= buttonHEIGHT, width=buttonWIDTH, command=SIX)
seven = tk.Button(win, text="7", height= buttonHEIGHT, width=buttonWIDTH, command=SEVEN)
eight = tk.Button(win, text="8", height= buttonHEIGHT, width=buttonWIDTH, command=EIGHT)
nine = tk.Button(win, text="9", height= buttonHEIGHT, width=buttonWIDTH, command=NINE)
zero = tk.Button(win, text="0", height= buttonHEIGHT, width=buttonWIDTH, command=ZERO)
equat = tk.Button(win, text="=", height= buttonHEIGHT, width=buttonWIDTH, command=EQUAT)
add = tk.Button(win, text="+", height= buttonHEIGHT, width=buttonWIDTH, command=ADD)
sub = tk.Button(win, text="-", height= buttonHEIGHT, width=buttonWIDTH, command=SUB)
multi = tk.Button(win, text="X", height=buttonHEIGHT, width=buttonWIDTH, command=MULTI)
div = tk.Button(win, text="÷", height= buttonHEIGHT, width=buttonWIDTH, command=DIV)
sqrt = tk.Button(win, text="sqrt", height= buttonHEIGHT, width=buttonWIDTH, command=SQRT)
expon = tk.Button(win, text="x^y", height= buttonHEIGHT, width=buttonWIDTH, command=EXPON)
recip = tk.Button(win, text="1/x", height= buttonHEIGHT, width=buttonWIDTH, command=RECIP)
modu = tk.Button(win, text="%", height= buttonHEIGHT, width=buttonWIDTH, command=MODU)
clearALL = tk.Button(win, text="CE", height= buttonHEIGHT, width=22, command=CLEARALL)
back = tk.Button(win, text="BACK", height= buttonHEIGHT, width=buttonWIDTH, command=BACK)
PlusMinus = tk.Button(win, text="+/-", height= buttonHEIGHT, width=buttonWIDTH, command=PLUSMINUS)
decimal = tk.Button(win, text=".", width=buttonWIDTH, height= buttonHEIGHT, command=DECIMAL)

# Putting the buttons on the screen
modu.grid(column=0, row=1)
clearALL.grid(column=1, row=1, columnspan=2)
back.grid(column=3, row=1)
recip.grid(column=0, row=2)
expon.grid(column=1, row=2)
sqrt.grid(column=2, row=2)
div.grid(column=3, row=2)
seven.grid(column=0, row=3)
eight.grid(column=1, row=3)
nine.grid(column=2, row=3)
multi.grid(column=3, row=3)
four.grid(column=0, row=4)
five.grid(column=1, row=4)
six.grid(column=2, row=4)
sub.grid(column=3, row=4)
one.grid(column=0, row=5)
two.grid(column=1, row=5)
three.grid(column=2, row=5)
add.grid(column=3, row=5)
PlusMinus.grid(column=0, row=6)
zero.grid(column=1, row=6)
decimal.grid(column=2, row=6)
equat.grid(column=3, row=6)

win.mainloop()