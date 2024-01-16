from tkinter import *

def button_press(num): #create a button press function with one parameter
    
    global equation_text #create a globval variable
    
    equation_text = equation_text + str(num) #converting whatever number recieved as a string
    equation_label.set(equation_text) #stringVar will be set to equation_text
    
    
def equals():
    
    
    global equation_text
    
    try:                                #execute this block of code 
    
        total = str(eval(equation_text)) #total number 
    
        equation_label.set(total) #the equation_label will be set to whatever our label is

        equation_text = total #if we want to reuse our total to perform a function again
    
    except ZeroDivisionError:
        
        equation_label.set("arithmatic error") #if there is a zero division error, this text will pop up
        
        equation_text = ""
        
    except SyntaxError:
        
        equation_label.set("syntax error") #if there is a zero division error, this text will pop up
        
        equation_text = ""
        
def clear():
    
    global equation_text #using the global vairable that is equation_text
    
    equation_label.set("") #set the equation label to "" so it becomes blank
    
    equation_text = ""

window = Tk()                              #create window
window.title("Calculator Program")         #window title
window.geometry("500x500")

equation_text = "" #string name equation

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg='white',width=24,height=2) #create a label
label.pack()

frame = Frame(window) #create a frame / container for all the buttons 
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, 
                 command=lambda: button_press(1)) #create a button for 1
button1.grid(row=0, column=0) #creates a grid for the button to be in (specific row and column)

button2 = Button(frame, text=2, height=4, width=9, font=35, 
                 command=lambda: button_press(2)) #create a button for 2
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, 
                 command=lambda: button_press(3)) #create a button for 3
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, 
                 command=lambda: button_press(4)) #create a button for 4
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, 
                 command=lambda: button_press(5)) #create a button for 5
button5.grid(row=1, column=1)

button6 = Button(frame, text=6,height=4, width=9, font=35, 
                 command=lambda: button_press(5)) #create a button for 6
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, 
                 command=lambda: button_press(7)) #create a button for 7
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, 
                 command=lambda: button_press(8)) #create a button for 8
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, 
                 command=lambda: button_press(9)) #create a button for 9
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, 
                 command=lambda: button_press(0)) #create a button for 0
button0.grid(row=3, column=0)

plus = Button(frame, text="+", height=4, width=9, font=35, 
                 command=lambda: button_press('+')) #create a button for +
plus.grid(row=0, column=3)

minus = Button(frame, text="-", height=4, width=9, font=35, 
                 command=lambda: button_press('-')) #create a button for -
minus.grid(row=1, column=3)

multiply = Button(frame, text="*", height=4, width=9, font=35, 
                 command=lambda: button_press('*')) #create a button for *
multiply.grid(row=2, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35, 
                 command=lambda: button_press('/')) #create a button for /
divide.grid(row=3, column=3)

equal = Button(frame, text="=", height=4, width=9, font=35, 
                 command=equals) #create a button for =
equal.grid(row=3, column=2)

decimal = Button(frame, text=".", height=4, width=9, font=35, 
                 command=lambda: button_press('.')) #create a button for .
decimal.grid(row=3, column=1)

clear = Button(window, text="clear", height=4, width=39, font=35, 
                 command=clear) #create a button for clear
clear.pack() #pack with the window rather than the gird


window.mainloop() #display the window




