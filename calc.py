from tkinter import *
def btnClick(numbers):
    global operator
    if numbers=="**0.5":
        text_Input.set("√" + str(operator))
        operator = operator + str(numbers)
    elif numbers=="**2":
        text_Input.set(str(operator) + "^2")
        operator = operator + str(numbers)
    elif numbers=="**(-1)":
        text_Input.set("1/" + str(operator))
        operator = operator + str(numbers)
    elif numbers=="*(-1)":
        operator = operator + str(numbers)
        evaluation()
    else:
        operator = operator + str(numbers)
        text_Input.set(operator)
    
def clearDisplay():
    global operator
    operator = ""
    text_Input.set("")
def evaluation():
    global operator
    solve = str(eval(operator))
    text_Input.set(solve)
    operator = solve
root = Tk()
root.title("Simple Calculator")
operator = ""
text_Input = StringVar() 
inp_fld = Entry(root, width=35, text = text_Input,borderwidth=5, fg="white", bg="grey")
inp_fld.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

butn0 = Button(root, text="0", padx="25", pady="10", bg="light blue",command = lambda:btnClick(0))#, command=)
butn1 = Button(root, text="1", padx="25", pady="10", bg="light blue",command = lambda:btnClick(1))#, command=)
butn2 = Button(root, text="2", padx="25", pady="10", bg="light blue",command = lambda:btnClick(2))#, command=)
butn3 = Button(root, text="3", padx="25", pady="10", bg="light blue",command = lambda:btnClick(3))#, command=)
butn4 = Button(root, text="4", padx="25", pady="10", bg="light blue",command = lambda:btnClick(4))#, command=)
butn5 = Button(root, text="5", padx="25", pady="10", bg="light blue",command = lambda:btnClick(5))#, command=)
butn6 = Button(root, text="6", padx="25", pady="10", bg="light blue",command = lambda:btnClick(6))#, command=)
butn7 = Button(root, text="7", padx="25", pady="10", bg="light blue",command = lambda:btnClick(7))#, command=)
butn8 = Button(root, text="8", padx="25", pady="10", bg="light blue",command = lambda:btnClick(8))#, command=)
butn9 = Button(root, text="9", padx="25", pady="10", bg="light blue",command = lambda:btnClick(9))#, command=)
butn10 = Button(root, text="÷", padx="25", pady="10", bg="#507877",command = lambda:btnClick("/"))#, command=)
butn11 = Button(root, text="×", padx="25", pady="10", bg="#507877",command = lambda:btnClick("*"))#, command=)
butn12 = Button(root, text="-", padx="26", pady="10", bg="#507877",command = lambda:btnClick("-"))#, command=)
butn13 = Button(root, text="+", padx="25", pady="10", bg="#507877",command = lambda:btnClick("+"))#, command=)
butn14 = Button(root, text="=", padx="25", pady="35", bg="light green",command = evaluation)#, command=)
butn15 = Button(root, text="+/-", padx="23", pady="10", bg="#87566f",command = lambda:btnClick("*(-1)"))#, command=)
butn16 = Button(root, text=".", padx="26", pady="10", bg="#87566f",command = lambda:btnClick("."))#, command=)
butn17 = Button(root, text="CLEAR", padx="76", pady="12", bg="orange", fg="white",command = clearDisplay )#, command=)
butn18 = Button(root, text="1/x", padx="20", pady="10", bg="#87566f",command = lambda:btnClick("**(-1)"))#, command=)
butn19 = Button(root, text="x^2", padx="18", pady="10", bg="#87566f",command = lambda:btnClick("**2"))#, command=)
butn20 = Button(root, text="√x", padx="20", pady="10", bg="#87566f",command = lambda:btnClick("**0.5"))#, command=)

butn0.grid(row=5, column=1)
butn1.grid(row=4, column=0)
butn2.grid(row=4, column=1)
butn3.grid(row=4, column=2)
butn4.grid(row=3, column=0)
butn5.grid(row=3, column=1)
butn6.grid(row=3, column=2)
butn7.grid(row=2, column=0)
butn8.grid(row=2, column=1)
butn9.grid(row=2, column=2)
butn10.grid(row=1, column=3)
butn11.grid(row=2, column=3)
butn12.grid(row=3, column=3)
butn13.grid(row=4, column=3)
butn14.grid(row=5, column=3, rowspan=2)
butn15.grid(row=5, column=0)
butn16.grid(row=5, column=2)
butn17.grid(row=6, column=0, columnspan=3)
butn18.grid(row=1, column=0)
butn19.grid(row=1, column=1)
butn20.grid(row=1, column=2)

root.mainloop()
