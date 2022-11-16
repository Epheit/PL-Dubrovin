from tkinter import *
from tkinter import ttk, filedialog
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

def clicked():
    a = txt1.get()
    b = txt2.get()
    res = 0
    c = combo1.get()
    if c == '+':
        res = float(a) + float(b)
    if c == '-':
        res = float(a) - float(b)
    if c == '*':
        res = float(a) * float(b)
    if c == '/':
        res = float(a) / float(b)
    lbl2['text'] = res

def clacked():
    if rad1.instate(['selected']) == True and rad2.instate(['selected']) == True and rad3.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали все три варианта.')
    elif rad1.instate(['selected']) == True and rad2.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали варианты 1 и 2.')
    elif rad1.instate(['selected']) == True and rad3.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали варианты 1 и 3.')
    elif rad2.instate(['selected']) == True and rad3.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали варианты 2 и 3.')
    elif rad1.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали вариант 1.')
    elif rad2.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали вариант 2.')
    elif rad3.instate(['selected']) == True:
        messagebox.showinfo('Информация', 'Вы выбрали вариант 3.')
    else:
        messagebox.showinfo('Информация', 'Вы не выбрали вариант перед нажатием кнопки выбора, попробуйте снова.')

def clocked():
    f = filedialog.askopenfilename()
    with open(f, 'r+', encoding = 'utf-8-sig')as file:
        line = file.read()
        txt3.insert('1.0', line)
        txt3.place(x=0, y=0)

window = Tk()
window.title("Дубровин Константин Юрьевич, УБ-23")
window.geometry('1000x600')
tab_control = ttk.Notebook(window)
tab1= ttk.Frame(tab_control)
tab_control.add(tab1, text = '                                        Калькулятор                                        ')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = '                                        Чекбоксы                                        ')
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text = '                                        Работа с текстом                                        ')
tab_control.pack(expand = 1, fill='both')

txt1 = Entry(tab1 ,width=10)
txt1.grid(column = '1', row = '0')
combo1 = Combobox(tab1)
combo1.grid(column = '2', row = '0')
combo1['values'] = ('+', '-', '*', '/')
txt2 = Entry(tab1, width= 10)
txt2.grid(column= '3', row = '0')
btn1 = Button(tab1, text = '=', command=clicked)
btn1.grid(column = '4', row = '0')
lbl2 = Label(tab1, text = '')
lbl2.grid(column = '5', row = '0')

chk1 = BooleanVar()
chk2 = BooleanVar()
chk3 = BooleanVar()
rad1 = Checkbutton(tab2, text='Первый вариант',  var = chk1)
rad2 = Checkbutton(tab2, text='Второй вариант',  var = chk2)
rad3 = Checkbutton(tab2, text='Третий вариант',  var = chk3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn2 = Button(tab2, text = 'Выбрать', command=clacked)
btn2.grid(column = '1', row = '2')

menu = Menu(window)
item = Menu(menu, tearoff = 0)
item.add_command(label='Загрузить файл')
menu.add_cascade(label='Файл', menu=item, command = clocked)
window.config(menu=menu)
txt3 = Text(tab3, width = 124, height = 50)
txt3.pack(side=LEFT)
window.mainloop()