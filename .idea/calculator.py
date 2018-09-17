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


root.mainloop()