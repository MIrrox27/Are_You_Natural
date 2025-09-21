from tkinter import *
from tkinter import messagebox
import random

app = Tk()
app.geometry('400x250+750+350')
app.title('Notes')
app.overrideredirect(True)  # убрать рамку окна (окно не закрыть)
app.attributes('-topmost', True)  # поверх всех окон


def win_block():
    pass

def rand_x():
    return random.randint(0, 350)  # Уменьшил максимальное значение, чтобы кнопка не выходила за пределы окна

def rand_y():
    return random.randint(0, 200)  # Уменьшил максимальное значение, чтобы кнопка не выходила за пределы окна

def new_position1(event):
    No.place(x=rand_x(), y=rand_y())
def new_position2(event):
    Yes.place(x=rand_x(), y=rand_y())

def com1():
    messagebox.showinfo('блять...', 'А ведь я знал что ты пидор...')
    app.quit()  # Закрываем приложение

lbl1 = Label(app, text="Ты натурал?")
lbl1.pack()

Yes = Button(app, text='Да', cursor='hand2')
Yes.place(x=100, y=100)  # Устанавливаем начальную позицию кнопки "Да"

No = Button(app, text='Нет', cursor='hand2', command=com1,)  # Убираем лишний вызов функции
No.place(x=210, y=100)

# Привязываем событие наведения курсора к кнопке "Нет"
No.bind("<Enter>", new_position1)
Yes.bind("<Enter>", new_position2)

app.mainloop()
