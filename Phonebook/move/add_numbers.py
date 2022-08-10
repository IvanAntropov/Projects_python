import tkinter as tk
import interface
from tkinter import messagebox as mb

def add_number(name,number,named,numberd):
    if name == '' and number == '':
        mb.showinfo('Error','Окна не заполнены')
    elif name == '' or number == '':
        mb.showinfo('Error','Одно из окон не заполнено')
    else:
        path = 'phonebooks/phonebook.txt'
        with open(path, 'a') as fa:
            fa.write('{}: {}\n'
                    .format(name, number))
        named.delete(0,tk.END)
        numberd.delete(0,tk.END)
        mb.showinfo('Done','Контакт успешно добавлен!')
    
    
