import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
photo = tk.PhotoImage(file = 'other/siren.png')
window.iconphoto(False, photo)
window.geometry(f'308x435+1290+100')  # .minsize .maxsize
window.resizable(False,False)
window['bg'] = 'black'
window.title('Calculator')

def pressKey(event):
    print(repr(event.char))
    if event.char.isdigit():
        addDigit(event.char)
    elif event.char in '+-/*':
        addOperation(event.char)
    elif event.char == '=' or event.char == '\r':
        calculate()
    elif event.char == '\x08':
        deleteLastSymbol()
        
def addDigit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)
    calc['state'] = tk.DISABLED

def addOperation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value + operation)
    calc['state'] = tk.DISABLED

def calculate():
    value = calc.get()
    if value[-1] in "-+/*":
        value+=value[:-1] 
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    try:
        calc.insert(0,eval(value))
    except (NameError,SyntaxError):
        messagebox.showinfo('Error','Not valid value')
        calc.insert(0,'0')
    except ZeroDivisionError:
        messagebox.showinfo('Error','Zero? Not funny.')
        calc.insert(0,'0')
    calc['state'] = tk.DISABLED

def clearing():
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,'0')
    calc['state'] = tk.DISABLED

def deleteLastSymbol():
    value = calc.get()
    calc['state'] = tk.NORMAL
    if value[0] != '0':
        calc.delete(0,tk.END)
        if len(value) == 1 and value[0] != '0':
            calc.insert(0,'0')
        else:
            calc.insert(0,value[:-1])
    calc['state'] = tk.DISABLED

def addPoint(point):
    value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    if value[0] == '0' and len(value) == 1:
        calc.insert(0,value+point)
    else:
        if point in value:
            calc.insert(0,value)
        else:
            calc.insert(0,value+point)

    calc['state'] = tk.DISABLED

def buttonForDigits(digit):
    return tk.Button(text = digit,fg='white', bg='#F984E5',bd=0,font=('Lucida sans unicode',24),command = lambda : addDigit(digit))

def buttonForOperation(operation):
    return tk.Button(text=operation, fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',24, 'bold'),command = lambda : addOperation(operation))

def buttonForCalculation(operation):
    return tk.Button(text=operation, fg='white', bg='#F984E5', bd=0, font=('Lucida sans unicode',24, 'bold'),command = lambda : calculate())

def clearButton(textOf):
    return tk.Button(text=textOf, fg='#F984E5', bg='white', bd=0, font=('Lucida sans unicode',12, 'bold'),command = lambda : clearing())

def buttonDelete(textOf):
    return tk.Button(text=textOf, fg='#F984E5', bg='white', bd=0, font=('Lucida sans unicode',12, 'bold'),command = lambda : deleteLastSymbol())

def buttonForPoint(point):
    return tk.Button(text = point,fg='white', bg='#F984E5',bd=0,font=('Lucida sans unicode',24),command = lambda : addPoint(point))
    
window.bind('<Key>', pressKey)
calc = tk.Entry(
                window,bd=0, justify = tk.RIGHT, 
                font=('Lucida sans unicode',16), 
                bg='black',fg = 'white', 
                disabledforeground = 'white', 
                disabledbackground = 'black',
                )

calc.insert(0,'0')
calc['state'] = tk.DISABLED

calc.grid(row = 1, column=0, columnspan = 5,stick='wens')
buttonForDigits('1').grid(row = 2, column = 0, columnspan = 2, stick='wens',padx=1,pady=1) 
buttonForDigits('2').grid(row = 2, column = 2, stick='wens',padx=1,pady=1)
buttonForDigits('3').grid(row = 2, column = 3, stick='wens',padx=1,pady=1)
buttonForDigits('4').grid(row = 3, column = 0, columnspan = 2, stick='wens',padx=1,pady=1)
buttonForDigits('5').grid(row = 3, column = 2, stick='wens',padx=1,pady=1)
buttonForDigits('6').grid(row = 3, column = 3, stick='wens',padx=1,pady=1)
buttonForDigits('7').grid(row = 4, column = 0, columnspan = 2, stick='wens',padx=1,pady=1)
buttonForDigits('8').grid(row = 4, column = 2, stick='wens',padx=1,pady=1)
buttonForDigits('9').grid(row = 4, column = 3, stick='wens',padx=1,pady=1)
buttonForDigits('0').grid(row = 5, column = 2, stick='wens',padx=1,pady=1)

buttonForOperation('+').grid(row = 2, column = 4, stick='wens',padx=1,pady=1)
buttonForOperation('-').grid(row = 3, column = 4, stick='wens',padx=1,pady=1)
buttonForOperation('*').grid(row = 4, column = 4, stick='wens',padx=1,pady=1)
buttonForOperation('/').grid(row = 5, column = 4, stick='wens',padx=1,pady=1)

buttonForCalculation('=').grid(row = 5, column = 0, columnspan = 2,stick='wens',padx=1,pady=1)
buttonForPoint('.').grid(row = 5, column = 3, stick='wens',padx=1,pady=1)
clearButton('C').grid(row = 0, column = 0,padx=1,pady=1, stick='wens')
buttonDelete('D').grid(row = 0, column = 1,padx=1,pady=1, stick='wens')

window.grid_columnconfigure(0, minsize=38.25)
window.grid_columnconfigure(1, minsize=38.25)
window.grid_columnconfigure(2, minsize=76.5)
window.grid_columnconfigure(3, minsize=76.5)
window.grid_columnconfigure(4, minsize=76.5)
window.grid_columnconfigure(5, minsize=76.5)

window.grid_rowconfigure(0, minsize=42.5)
window.grid_rowconfigure(1, minsize=42.5)
window.grid_rowconfigure(2, minsize=87)
window.grid_rowconfigure(3, minsize=87)
window.grid_rowconfigure(4, minsize=87)
window.grid_rowconfigure(5, minsize=87)

window.mainloop()