from sys import maxsize
from move import add_numbers as add
from move import find_numbers as show
from tkinter import *
import tkinter as tk
import main

def pressKey(event):
    print(repr(event.char)) 
    
window = tk.Tk()
window.geometry(f'600x400+1290+100')
window.minsize(600,400)
window.resizable(True,True)
window['bg'] = 'black'
window.title('Phonebook 0.2')

window.grid_columnconfigure(0, minsize=200)
window.grid_columnconfigure(1, minsize=200)
window.grid_columnconfigure(2, minsize=200)
window.grid_rowconfigure(0, minsize=50)

window.bind('<Key>', pressKey)

def interface_for_add():
    tk.Label(window,text='Введите имя: ', fg='white', bg='black', bd=0, font=('Lucida sans unicode',8, 'bold'), anchor = 'w',justify=tk.LEFT).grid(row = 1, column = 0) 
    tk.Label(window,text='Введите номер телефона: ', fg='white', bg='black', bd=0, font=('Lucida sans unicode',8, 'bold'), anchor = 'w',justify=tk.LEFT).grid(row = 2, column = 0)
    name = tk.Entry(
                window,bd=0, justify = tk.CENTER, 
                font=('Lucida sans unicode',12), 
                bg='white',fg = 'black', 
                disabledforeground = 'black', 
                disabledbackground = 'white',
                )
    number = tk.Entry(
                window,bd=0, justify = tk.CENTER, 
                font=('Lucida sans unicode',12), 
                bg='white',fg = 'black', 
                disabledforeground = 'black', 
                disabledbackground = 'white',
                )
    name.grid(row = 1, column = 1,columnspan=2, stick='wens',padx=1,pady=1)
    number.grid(row = 2, column = 1,columnspan=2, stick='wens',padx=1,pady=1)
    
    tk.Button(window,text='Ok', fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',8, 'bold'),command = lambda : add.add_number(name.get(), number.get(),name,number)).grid(
        row = 3, column = 2, stick='wens',padx=1,pady=1)
    tk.Button(window,text='Cansel', fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',8, 'bold'),command = lambda : show.show_numbers(window)).grid(
        row = 3, column = 1, stick='wens',padx=1,pady=1)

def PhoneBook():
    tk.Button(text='Добавить номер', fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',12, 'bold'),command = lambda : interface_for_add()).grid(
            row = 0, column = 0, stick='wens',padx=1,pady=1) 
    tk.Button(text='Показать номера', fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',12, 'bold'),command = lambda : show.show_numbers(window)).grid(
            row = 0, column = 1, stick='wens',padx=1,pady=1)
    tk.Button(text='Импорт номеров', fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',12, 'bold'),command = lambda : imp.start_import()).grid(
            row = 0, column = 2, stick='wens',padx=1,pady=1) 
      
 
PhoneBook()  


window.mainloop()