# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:14:47 2018

@author: tejas
"""

from tkinter import *

def btn(number):
    global operator
    operator = operator + str(number)
    def_input_text.set(operator)


def Equal():
    global operator
    total = float(eval(operator))
    def_input_text.set(total)
    operator = ''

def clear():
    global operator
    operator = ''
    def_input_text.set('')
    Display.insert(0, '')


root = Tk()
root.title('Calculator')
root.configure(background='black')

operator = ''
def_input_text = StringVar(value='')

##height = root.winfo_screenwidth(), root.winfo_screenheight()

##root.geometry('%dx%d+0+0' % (width,height))

Display = Entry(root, font = ('arial', 30 , 'bold'),
                fg='white', bg='black', justify='right',
                bd=50, textvariable = def_input_text)
Display.grid(columnspan=4)

##==================================================================================
##Row 1

##Clear
btnAC = Button(root, font = ('arial', 30, 'bold'),
               padx = 27, pady = 15,
               fg = 'white', justify = 'center',
               bd = 8, text = 'C', bg='red',
               command = clear).grid(row = 1, column = 0)

##Modulus
# btnMod = Button(root, font = ('arial', 30, 'bold'),
#                 padx = 25, pady = 15,
#                 fg = 'black', justify = 'center',
#                 bd = 8, text = '%', bg='orange').grid(row = 1, column = 1)

# Open Braces

btnOB = Button(root, font = ('arial', 30, 'bold'),
               padx = 35, pady = 15,
               fg = 'black',
               bd = 8, text = '(', bg='orange',
               command = lambda:btn('(')).grid(row = 1, column = 1)

btnCB = Button(root, font = ('arial', 30, 'bold'),
               padx = 35, pady = 15,
               fg = 'black',
               bd = 8, text = ')', bg='orange',
               command = lambda:btn(')')).grid(row = 1, column = 2)

##Division
btnDiv = Button(root, font = ('arial', 30, 'bold'),
                padx = 36, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '/', bg='orange',
                command = lambda:btn('/')).grid(row = 1, column = 3)




##=================================================================================
##Row 2
btn7 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '7',  bg='white',
              command = lambda:btn(7)).grid(row = 2, column = 0)

btn8 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '8', bg='white',
              command = lambda:btn(8)).grid(row = 2, column = 1)

btn9 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '9', bg='white',
              command = lambda:btn(9)).grid(row = 2, column = 2)

##Multiplication
btnmul = Button(root, font = ('arial', 30, 'bold'),
                padx = 30, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '*', bg='orange',
                command = lambda:btn('*')).grid(row = 2, column = 3)

# ===============================================================================================
##Row 3

btn4 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '4', bg='white',
              command = lambda:btn(4)).grid(row = 3, column = 0)

btn5 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '5', bg='white',
              command = lambda:btn(5)).grid(row = 3, column = 1)

btn6 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '6', bg='white',
              command = lambda:btn(6)).grid(row = 3, column = 2)

##Minus Operator/ Subtraction
btnMinus = Button(root, font = ('arial', 30, 'bold'),
                  padx = 32, pady = 15,
                  fg = 'black',
                  bd = 8, text = '-', bg='orange',
                  command = lambda:btn('-')).grid(row = 3, column = 3)



##==================================================================================
##Row 4


btn1 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '1', bg='white',
              command = lambda:btn(1)).grid(row = 4, column = 0)

btn2 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '2', bg='white',
              command = lambda:btn(2)).grid(row = 4, column = 1)

btn3 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '3', bg='white',
              command = lambda:btn(3)).grid(row = 4, column = 2)

##Addition Operator
btnPlus = Button(root, font = ('arial', 30, 'bold'),
                 padx = 30, pady = 15,
                 fg = 'black',
                 bd = 8, text = '+', bg='orange',
                 command = lambda:btn('(')).grid(row = 4, column = 3)

##==================Row 5==================================

btn0 = Button(root, font = ('arial', 30, 'bold'),
              padx = 95, pady = 15,
              fg = 'black',
              bd = 8, text = '0', bg='white',
              command = lambda:btn(0)).grid(row = 5, column = 0, columnspan = 2)

btnDec = Button(root, font = ('arial', 30, 'bold'),
                padx = 35, pady = 15,
                fg = 'black',
                bd = 8, text = '.', bg='orange',
                command = lambda:btn('.')).grid(row = 5, column = 2)


btnEqu = Button(root, font = ('arial', 30, 'bold'),
                padx = 30, pady = 15,
                fg = 'black',
                bd = 8, text = '=', bg='orange',
                command = Equal).grid(row = 5, column = 3)


root.mainloop()