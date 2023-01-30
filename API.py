#Задание №62 Проверка доступности сайта с уведомлением. 
# Реализовать программу которая будет проверять доступность сайтов с заданным интервалом. 
# Количество сайтов неограничено. 
# Интервал проверки для каждого сайта- заданный польователем(они могут быть для каждого сайта разные).

#Module libs A
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import time
#Module core C

#Module core A
def clicked1():
        try: 
                int(txt16.get())
                for i in range (int(txt16.get())):
                        try:
                                int(txt6.get())
                                try:
                                        response1 = requests.get(f'{txt1.get()}', timeout = (int(txt6.get())))
                                        print(response1.status_code)
                                        if response1.status_code >=100 and response1.status_code < 400:
                                                lbl12['text'] = 'Сайт доступен'
                                                lbl12['fg'] = 'green'
                                        else:
                                                lbl12['text'] = 'Сайт недоступен'
                                                lbl12['fg'] = 'red'                      
                                except:
                                        lbl12['text'] = 'Сайт недоступен'
                                        lbl12['fg'] = 'red'
                        except:
                                try:
                                        response1 = requests.get(f'{txt1.get()}', timeout = 1 )
                                        print(response1.status_code)
                                        if response1.status_code >=100 and response1.status_code < 400:
                                                lbl12['text'] = 'Сайт доступен'
                                                lbl12['fg'] = 'green'
                                        else:
                                                bl12['text'] = 'Сайт недоступен'
                                                lbl12['fg'] = 'red'                      
                                except:
                                        lbl12['text'] = 'Сайт недоступен'
                                        lbl12['fg'] = 'red'
                        lbl18['text'] = i+1
                        try:
                                time.sleep(int(txt11.get()))
                        except:
                                time.sleep(1)
        except:
                for i in range (1):
                        try:
                                int(txt6.get())
                                try:
                                        response1 = requests.get(f'{txt1.get()}', timeout = (int(txt6.get())))
                                        print(response1.status_code)
                                        if response1.status_code >=100 and response1.status_code < 400:
                                                lbl12['text'] = 'Сайт доступен'
                                                lbl12['fg'] = 'green'
                                        else:
                                                lbl12['text'] = 'Сайт недоступен'
                                                lbl12['fg'] = 'red'                      
                                except:
                                        lbl12['text'] = 'Сайт недоступен'
                                        lbl12['fg'] = 'red'
                        except:
                                try:
                                        response1 = requests.get(f'{txt1.get()}', timeout = 1 )
                                        print(response1.status_code)
                                        if response1.status_code >=100 and response1.status_code < 400:
                                                lbl12['text'] = 'Сайт доступен'
                                                lbl12['fg'] = 'green'
                                        else:
                                                bl12['text'] = 'Сайт недоступен'
                                                lbl12['fg'] = 'red'                      
                                except:
                                        lbl12['text'] = 'Сайт недоступен'
                                        lbl12['fg'] = 'red'
                        lbl18['text'] = i+1
                        try:
                                time.sleep(int(txt11.get()))
                        except:
                                time.sleep(1)

def clicked2():
        try: 
                int(txt16.get())
                for i in range (int(txt16.get())):
                        try:
                                int(txt7.get())  
                                try:
                                        response2 = requests.get(f'{txt2.get()}', timeout = (int(txt7.get())))
                                        print(response2.status_code)
                                        if response2.status_code >=100 and response2.status_code < 400:
                                                lbl13['text'] = 'Сайт доступен'
                                                lbl13['fg'] = 'green'
                                        else:
                                                lbl13['text'] = 'Сайт недоступен'
                                                lbl13['fg'] = 'red'
                                except:
                                        lbl13['text'] = 'Сайт недоступен'
                                        lbl13['fg'] = 'red'
                        except:
                                try:
                                        response2 = requests.get(f'{txt2.get()}', timeout = 1 )
                                        print(response2.status_code)
                                        if response2.status_code >=100 and response2.status_code < 400:
                                                lbl13['text'] = 'Сайт доступен'
                                                lbl13['fg'] = 'green'
                                        else:
                                                lbl13['text'] = 'Сайт недоступен'
                                                lbl13['fg'] = 'red'
                                except:
                                        lbl13['text'] = 'Сайт недоступен'
                                        lbl13['fg'] = 'red'
                        lbl19['text'] = i+1
                        try:
                                time.sleep(int(txt12.get()))
                        except:
                                time.sleep(1)
        except:
                for i in range (1):
                        try:
                                int(txt7.get())  
                                try:
                                        response2 = requests.get(f'{txt2.get()}', timeout = (int(txt7.get())))
                                        print(response2.status_code)
                                        if response2.status_code >=100 and response2.status_code < 400:
                                                lbl13['text'] = 'Сайт доступен'
                                                lbl13['fg'] = 'green'
                                        else:
                                                lbl13['text'] = 'Сайт недоступен'
                                                lbl13['fg'] = 'red'
                                except:
                                        lbl13['text'] = 'Сайт недоступен'
                                        lbl13['fg'] = 'red'
                        except:
                                try:
                                        response2 = requests.get(f'{txt2.get()}', timeout = 1 )
                                        print(response2.status_code)
                                        if response2.status_code >=100 and response2.status_code < 400:
                                                lbl13['text'] = 'Сайт доступен'
                                                lbl13['fg'] = 'green'
                                        else:
                                                lbl13['text'] = 'Сайт недоступен'
                                                lbl13['fg'] = 'red'
                                except:
                                        lbl13['text'] = 'Сайт недоступен'
                                        lbl13['fg'] = 'red'
                        lbl19['text'] = i+1
                        try:
                                time.sleep(int(txt12.get()))
                        except:
                                time.sleep(1)

                
def clicked3():
        try: 
                int(txt16.get())
                for i in range (int(txt16.get())):
                        try:
                                int(txt8.get())
                                try:
                                        response3 = requests.get(f'{txt3.get()}', timeout = (int(txt8.get())))
                                        print(response3.status_code)
                                        if response3.status_code >=100 and response3.status_code < 400:
                                                lbl14['text'] = 'Сайт доступен'
                                                lbl14['fg'] = 'green'
                                        else:
                                                lbl14['text'] = 'Сайт недоступен'
                                                lbl14['fg'] = 'red'
                                except:
                                        lbl14['text'] = 'Сайт недоступен'
                                        lbl14['fg'] = 'red'
                        except:
                                try:
                                        response3 = requests.get(f'{txt3.get()}', timeout = 1 )
                                        print(response3.status_code)
                                        if response3.status_code >=100 and response3.status_code < 400:
                                                lbl14['text'] = 'Сайт доступен'
                                                lbl14['fg'] = 'green'
                                        else:
                                                lbl14['text'] = 'Сайт недоступен'
                                                lbl14['fg'] = 'red'
                                except:
                                        bl14['text'] = 'Сайт недоступен'
                                        lbl14['fg'] = 'red'
                        lbl20['text'] = i+1
                        try:
                                time.sleep(int(txt13.get()))
                        except:
                                time.sleep(1)
        except:
                for i in range (1):
                        try:
                                int(txt8.get())
                                try:
                                        response3 = requests.get(f'{txt3.get()}', timeout = (int(txt8.get())))
                                        print(response3.status_code)
                                        if response3.status_code >=100 and response3.status_code < 400:
                                                lbl14['text'] = 'Сайт доступен'
                                                lbl14['fg'] = 'green'
                                        else:
                                                lbl14['text'] = 'Сайт недоступен'
                                                lbl14['fg'] = 'red'
                                except:
                                        lbl14['text'] = 'Сайт недоступен'
                                        lbl14['fg'] = 'red'
                        except:
                                try:
                                        response3 = requests.get(f'{txt3.get()}', timeout = 1 )
                                        print(response3.status_code)
                                        if response3.status_code >=100 and response3.status_code < 400:
                                                lbl14['text'] = 'Сайт доступен'
                                                lbl14['fg'] = 'green'
                                        else:
                                                lbl14['text'] = 'Сайт недоступен'
                                                lbl14['fg'] = 'red'
                                except:
                                        bl14['text'] = 'Сайт недоступен'
                                        lbl14['fg'] = 'red'
                        lbl20['text'] = i+1
                        try:
                                time.sleep(int(txt13.get()))
                        except:
                                time.sleep(1)

def clicked4():
        try:
                int(txt16.get())
                for i in range (int(txt16.get())):
                        try:
                                int(txt9.get())
                                try:
                                        response4 = requests.get(f'{txt4.get()}', timeout = (int(txt9.get())))
                                        print(response4.status_code)
                                        if response4.status_code >=100 and response4.status_code < 400:
                                                lbl15['text'] = 'Сайт доступен'
                                                lbl15['fg'] = 'green'
                                        else:
                                                lbl15['text'] = 'Сайт недоступен'
                                                lbl15['fg'] = 'red'
                                except:
                                        lbl15['text'] = 'Сайт недоступен'
                                        lbl15['fg'] = 'red'
                        except:
                                try:
                                        response4 = requests.get(f'{txt4.get()}', timeout = 1 )
                                        print(response4.status_code)
                                        if response4.status_code >=100 and response4.status_code < 400:
                                                lbl15['text'] = 'Сайт доступен'
                                                lbl15['fg'] = 'green'
                                        else:
                                                lbl15['text'] = 'Сайт недоступен'
                                                lbl15['fg'] = 'red'
                                except:
                                        lbl15['text'] = 'Сайт недоступен'
                                        lbl15['fg'] = 'red'
                        lbl21['text'] = i+1
                        try:
                                time.sleep(int(txt14.get()))
                        except:
                                time.sleep(1)
        except:
                for i in range (1):
                        try:
                                int(txt9.get())
                                try:
                                        response4 = requests.get(f'{txt4.get()}', timeout = (int(txt9.get())))
                                        print(response4.status_code)
                                        if response4.status_code >=100 and response4.status_code < 400:
                                                lbl15['text'] = 'Сайт доступен'
                                                lbl15['fg'] = 'green'
                                        else:
                                                lbl15['text'] = 'Сайт недоступен'
                                                lbl15['fg'] = 'red'
                                except:
                                        lbl15['text'] = 'Сайт недоступен'
                                        lbl15['fg'] = 'red'
                        except:
                                try:
                                        response4 = requests.get(f'{txt4.get()}', timeout = 1 )
                                        print(response4.status_code)
                                        if response4.status_code >=100 and response4.status_code < 400:
                                                lbl15['text'] = 'Сайт доступен'
                                                lbl15['fg'] = 'green'
                                        else:
                                                lbl15['text'] = 'Сайт недоступен'
                                                lbl15['fg'] = 'red'
                                except:
                                        lbl15['text'] = 'Сайт недоступен'
                                        lbl15['fg'] = 'red'
                        lbl21['text'] = i+1
                        try:
                                time.sleep(int(txt14.get()))
                        except:
                                time.sleep(1)
                
def clicked5():
        try:
                int(txt16.get())
                for i in range (int(txt16.get())):
                        try:
                                int(txt10.get())
                                try:
                                        response5 = requests.get(f'{txt5.get()}', timeout = (int(txt10.get())))
                                        print(response5.status_code)
                                        if response5.status_code >=100 and response5.status_code < 400:
                                                lbl16['text'] = 'Сайт доступен'
                                                lbl16['fg'] = 'green'
                                        else:
                                                lbl16['text'] = 'Сайт недоступен'
                                                lbl16['fg'] = 'red'
                                except:
                                        lbl16['text'] = 'Сайт недоступен'
                                        lbl16['fg'] = 'red'
                        except:
                                try:
                                        response5 = requests.get(f'{txt5.get()}', timeout = 1 )
                                        print(response5.status_code)
                                        if response5.status_code >=100 and response5.status_code < 400:
                                                lbl16['text'] = 'Сайт доступен'
                                                lbl16['fg'] = 'green'
                                        else:
                                                lbl16['text'] = 'Сайт недоступен'
                                                lbl16['fg'] = 'red'
                                except:
                                        lbl16['text'] = 'Сайт недоступен'
                                        lbl16['fg'] = 'red'
                        lbl22['text'] = i+1
                        try:
                                time.sleep(int(txt15.get()))
                        except:
                                time.sleep(1)
        except:
                for i in range (1):
                        try:
                                int(txt10.get())
                                try:
                                        response5 = requests.get(f'{txt5.get()}', timeout = (int(txt10.get())))
                                        print(response5.status_code)
                                        if response5.status_code >=100 and response5.status_code < 400:
                                                lbl16['text'] = 'Сайт доступен'
                                                lbl16['fg'] = 'green'
                                        else:
                                                lbl16['text'] = 'Сайт недоступен'
                                                lbl16['fg'] = 'red'
                                except:
                                        lbl16['text'] = 'Сайт недоступен'
                                        lbl16['fg'] = 'red'
                        except:
                                try:
                                        response5 = requests.get(f'{txt5.get()}', timeout = 1 )
                                        print(response5.status_code)
                                        if response5.status_code >=100 and response5.status_code < 400:
                                                lbl16['text'] = 'Сайт доступен'
                                                lbl16['fg'] = 'green'
                                        else:
                                                lbl16['text'] = 'Сайт недоступен'
                                                lbl16['fg'] = 'red'
                                except:
                                        lbl16['text'] = 'Сайт недоступен'
                                        lbl16['fg'] = 'red'
                        lbl22['text'] = i+1
                        try:
                                time.sleep(int(txt15.get()))
                        except:
                                time.sleep(1)

#Module core B
def clicked6():
        return(clicked1(), clicked2(), clicked3(), clicked4(), clicked5())
        
#Module int A
window = Tk()
window.title("Дубровин Константин УБ-23")
window.geometry('1430x600')
lbl = Label(window, text = '_____________________________________________')
lbl.grid(column = 1, row = 0)

#Module int B
lbl1 = Label(window, text = 'Для проверки введите имя сайта: ')
lbl1.grid(column = 1, row = 1)
lbl2 = Label(window, text = '1. ') 
lbl2.grid(column = 1, row = 2)
txt1 = Entry(window ,width = 30)
txt1.grid(column = 2, row = 2)
txt1.insert(0, 'https://www.onlinegdb.com/')
lbl3 = Label(window, text = '2. ') 
lbl3.grid(column = 1, row = 3)
txt2 = Entry(window ,width = 30)
txt2.grid(column = 2, row = 3)
txt2.insert(0, 'https://www.onlinegdb.com/')
lbl4 = Label(window, text = '3. ') 
lbl4.grid(column = 1, row = 4)
txt3 = Entry(window ,width = 30)
txt3.grid(column = 2, row = 4)
txt3.insert(0, 'https://www.onlinegdb.com/')
lbl5 = Label(window, text = '4. ') 
lbl5.grid(column = 1, row = 5)
txt4 = Entry(window ,width = 30)
txt4.grid(column = 2, row = 5)
txt4.insert(0, 'https://www.onlinegdb.com/')
lbl6 = Label(window, text = '5. ') 
lbl6.grid(column = 1, row = 6)
txt5 = Entry(window ,width = 30)
txt5.grid(column = 2, row = 6)
txt5.insert(0, 'https://www.onlinegdb.com/')

#Module int C
lbl7 = Label(window, text = '_____________________________________________')
lbl7.grid(column = 1, row = 7)
lbl8 = Label(window, text = 'Введите необходимое время проверки сайтов(сек.):')
lbl8.grid(column = 3, row = 1 )
txt6 = Entry(window, width = 7)
txt6.grid(column = 3, row = 2)
txt6.insert(0, '1')
txt7 = Entry(window, width = 7)
txt7.grid(column = 3, row = 3)
txt7.insert(0, '1')
txt8 = Entry(window, width = 7)
txt8.grid(column = 3, row = 4)
txt8.insert(0, '1')
txt9 = Entry(window, width = 7)
txt9.grid(column = 3, row = 5)
txt9.insert(0, '1')
txt10 = Entry(window, width = 7)
txt10.grid(column = 3, row = 6)
txt10.insert(0, '1')
lbl9 = Label(window, text = 'Введите необходимое кол-во повторений проверки:')
lbl9.grid(column = 1, row = 9 )
txt16 = Entry(window, width = 30)
txt16.grid(column = 2, row = 9)
txt16.insert(0, '1')

#Module int D
lbl10 = Label(window, text = 'Введите необходимый интервал проверки сайтов(сек.): ')
lbl10.grid(column = 4, row = 1)
txt11 = Entry(window, width = 7)
txt11.grid(column = 4, row = 2)
txt11.insert(0, '1')
txt12 = Entry(window, width = 7)
txt12.grid(column = 4, row = 3)
txt12.insert(0, '1')
txt13 = Entry(window, width = 7)
txt13.grid(column = 4, row = 4)
txt13.insert(0, '1')
txt14 = Entry(window, width = 7)
txt14.grid(column = 4, row = 5)
txt14.insert(0, '1')
txt15 = Entry(window, width = 7)
txt15.grid(column = 4, row = 6)
txt15.insert(0, '1')

#Module int E
lbl10 = Label(window, text = '_____________________________________________')
lbl10.grid(column = 1, row = 10)
btn1 = Button(window, text = 'Найти', command = clicked1)
btn1.grid(column = 5, row = 2)
btn2 = Button(window, text = 'Найти', command = clicked2)
btn2.grid(column = 5, row = 3)
btn3 = Button(window, text = 'Найти', command = clicked3)
btn3.grid(column = 5, row = 4)
btn4 = Button(window, text = 'Найти', command = clicked4)
btn4.grid(column = 5, row = 5)
btn5 = Button(window, text = 'Найти', command = clicked5)
btn5.grid(column = 5, row = 6)
btn6 = Button(window, text = 'Найти разом', command = clicked6)
btn6.grid(column = 1, row = 11)

#Module int F
lbl11 = Label(window, text = 'Результат проверки:')
lbl11.grid(column = 6, row = 1)
lbl12 = Label(window, text = 'None')
lbl12.grid(column = 6, row = 2)
lbl13 = Label(window, text = 'None')
lbl13.grid(column = 6, row = 3)
lbl14 = Label(window, text = 'None')
lbl14.grid(column = 6, row = 4)
lbl15 = Label(window, text = 'None')
lbl15.grid(column = 6, row = 5)
lbl16 = Label(window, text = 'None')
lbl16.grid(column = 6, row = 6)

#Module int G
lbl17 = Label(window, text = 'Пройдено кругов проверки:')
lbl17.grid(column = 7, row = 1)
lbl18 = Label(window, text = 'None')
lbl18.grid(column = 7, row = 2)
lbl19 = Label(window, text = 'None')
lbl19.grid(column = 7, row = 3)
lbl20 = Label(window, text = 'None')
lbl20.grid(column = 7, row = 4)
lbl21 = Label(window, text = 'None')
lbl21.grid(column = 7, row = 5)
lbl22 = Label(window, text = 'None')
lbl22.grid(column = 7, row = 6)


window.mainloop()