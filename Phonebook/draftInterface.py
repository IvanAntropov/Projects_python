from xml.dom.pulldom import START_ELEMENT
from move import add_numbers as add
from move import find_numbers as findN
from tkinter import *
import tkinter as tk
import main
from tkinter import *
from tkinter import scrolledtext

def pressKey(event):
    print(repr(event.char)) 

window = tk.Tk()
window.geometry(f'896x250+550+250')
window.minsize(896,366)
window.resizable(False,False)
window['bg'] = 'black'
window.title('Phonebook 0.2')

path = 'phonebooks/phonebook.txt'
with open(path, 'r') as fr:
    list_of_numbers = fr.read().split('\x08')
text = scrolledtext.ScrolledText(window, bg="black",fg='white', wrap=WORD, state='normal',font=('Lucida sans unicode',8))
text.grid(row = 0, column = 2,rowspan=5,pady=2)   
for i in range(len(list_of_numbers)):
    if list_of_numbers[i] != '':
        text.insert(END, list_of_numbers[i])
text.configure(state='disabled')


tk.Label(window,text='Имя: ', fg='white', bg='black', bd=0, font=('Lucida sans unicode',8, 'bold'), anchor = 'w',justify=tk.CENTER).grid(row = 0, column = 0) 
tk.Label(window,text='Номер телефона: ', fg='white', bg='black', bd=0, font=('Lucida sans unicode',8, 'bold'), anchor = 'w',justify=tk.CENTER).grid(row = 1, column = 0)
name = tk.Entry(
            window,bd=0, justify = tk.CENTER, 
            font=('Lucida sans unicode',8), 
            bg='white',fg = 'black', 
            disabledforeground = 'black', 
            disabledbackground = 'white',
            )
number = tk.Entry(
            window,bd=0, justify = tk.CENTER, 
            font=('Lucida sans unicode',8), 
            bg='white',fg = 'black', 
            disabledforeground = 'black', 
            disabledbackground = 'white',
            )
name.grid(row = 0, column = 1, stick='wens',padx=5,pady=5)
number.grid(row = 1, column = 1, stick='wens',padx=5,pady=5)

tk.Button(text='Добавить', fg='black', bg='#F984E5', bd=0, font=('Lucida sans unicode',12,'bold'),command = lambda : add.add_number(name.get(), number.get(),name,number)).grid(
        row = 2, column = 0,columnspan=2, stick='wens',padx=5,pady=5) 
tk.Button(text='Найти', fg='black', bg='#F984E5', bd=0, font=('Lucida sans unicode',12,'bold'),command = lambda : findN.find_numbers(window,name.get(),number.get(),text)).grid(
        row = 3, column = 0,columnspan=2, stick='wens',padx=5,pady=5)
tk.Button(text='Показать номера', fg='black', bg='#F984E5', bd=0, font=('Lucida sans unicode',12,'bold'),command = lambda : imp.start_import()).grid(
        row = 4, column = 0,columnspan=2, stick='wens',padx=5,pady=5) 

window.grid_columnconfigure(0, minsize=100)
window.grid_columnconfigure(1, minsize=200)
window.grid_columnconfigure(2, minsize=300)
window.grid_rowconfigure(0, minsize=15)
window.grid_rowconfigure(1, minsize=15)
window.grid_rowconfigure(2, minsize=15)
window.grid_rowconfigure(3, minsize=15)
window.grid_rowconfigure(4, minsize=15)

window.bind('<Key>', pressKey)

window.mainloop()