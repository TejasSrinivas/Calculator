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
               padx = 30, pady = 15,
               fg = 'white', justify = 'center',
               bd = 8, text = 'C', bg='red').grid(row = 1, column = 0)

##Modulus
btnMod = Button(root, font = ('arial', 30, 'bold'),
                padx = 30, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '%', bg='orange').grid(row = 1, column = 1)

##Division
btnDiv = Button(root, font = ('arial', 30, 'bold'),
                padx = 30, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '/', bg='orange').grid(row = 1, column = 2)


##Multiplication
btnmul = Button(root, font = ('arial', 30, 'bold'),
                padx = 30, pady = 15,
                fg = 'black', justify = 'center',
                bd = 8, text = '*', bg='orange').grid(row = 1, column = 3)

root.mainloop()