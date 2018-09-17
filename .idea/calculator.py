# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:14:47 2018

@author: tejas
"""

from tkinter import *

root = Tk()
root.title('Calculator')
root.configure(background='black')

Display = Entry(root, font = ('arial', 30 , 'bold'),
                fg='white', bg='black', justify='right',
                bd=50)
Display.grid(columnspan=4)

##==================================================================================
##Row 1

##Clear
btnAC = Button(root, font = ('arial', 30, 'bold'),
               padx = 27, pady = 15,
               fg = 'white', justify = 'center',
               bd = 8, text = 'C', bg='red').grid(row = 1, column = 0)

##Modulus
btnMod = Button(root, font = ('arial', 30, 'bold'),
                padx = 25, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '%', bg='orange').grid(row = 1, column = 1)

##Division
btnDiv = Button(root, font = ('arial', 30, 'bold'),
                padx = 36, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '/', bg='orange').grid(row = 1, column = 2)


##Multiplication
btnmul = Button(root, font = ('arial', 30, 'bold'),
                padx = 30, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '*', bg='orange').grid(row = 1, column = 3)

##=================================================================================
##Row 2
btn7 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '7',  bg='white').grid(row = 2, column = 0)

btn8 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '8', bg='white').grid(row = 2, column = 1)

btn9 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '9', bg='white').grid(row = 2, column = 2)

##Minus Operator/ Subtraction
btnMinus = Button(root, font = ('arial', 30, 'bold'),
                  padx = 32, pady = 15,
                  fg = 'black',
                  bd = 8, text = '-', bg='orange').grid(row = 2, column = 3)

##Row 3

btn4 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '4', bg='white').grid(row = 3, column = 0)

btn5 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '5', bg='white').grid(row = 3, column = 1)

btn6 = Button(root, font = ('arial', 30, 'bold'),
              padx = 30, pady = 15,
              fg = 'black',
              bd = 8, text = '6', bg='white').grid(row = 3, column = 2)

##Addition Operator
btnPlus = Button(root, font = ('arial', 30, 'bold'),
                 padx = 30, pady = 15,
                 fg = 'black',
                 bd = 8, text = '+', bg='orange').grid(row = 3, column = 3)


root.mainloop()