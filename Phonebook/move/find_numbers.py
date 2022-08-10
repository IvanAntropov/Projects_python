import tkinter as tk
import interface
from tkinter import messagebox as mb
from tkinter import *
from tkinter import scrolledtext, ttk

def find_numbers(window,name,number,text):
    path = 'phonebooks/phonebook.txt'
    with open(path, 'r') as fr:
        list_of_numbers = fr.read().split('\x08')
    text.configure(state='normal')
    text.delete(0,tk.END)
    for i in range(len(list_of_numbers)):
        if name in list_of_numbers[i] or number in list_of_numbers[i]:
            text.insert(END,list_of_numbers[i])
    text.configure(state='disabled')
    