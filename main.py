from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
import zipfile
import os
import shutil
import subprocess
import pandas as pd


def first_task():
    for i in range(len(test1.index)):
        script = subprocess.run(["python", "1.py", str(test1.loc[i, 'n']), str(test1.loc[i, 'm'])],
                                stdout=subprocess.PIPE)
        txt_test.insert(INSERT,
                        "№" + str(i) + " Вывод: " + str(script.stdout)[2:-1] + " Правильный ответ: " + str(
                            test1.loc[i, 'right_answer']) + "\n")


def repo_button_click():
    if repo_language_choice.get() == "Python":
        if os.path.exists("task1"):
            os.chdir("task1")
            first_task()


def open_file():
    global file
    file = filedialog.askopenfilename()
    txt_log.insert(INSERT, "Открыт файл: " + file + "\n")

    if os.path.exists(os.getcwd() + "\\repo"):
        shutil.rmtree(os.getcwd() + "\\repo")
        txt_log.insert(INSERT, "Папка с репозиториями очищена!\n")
    repo_zip = zipfile.ZipFile(file)
    repo_zip.extractall(os.getcwd() + "\\repo")
    txt_log.insert(INSERT, "Файл разархивирован в: " + os.getcwd() + "\\repo\n")

    os.chdir("repo")
    os.chdir(os.listdir()[0])
    txt_log.insert(INSERT, "Рабочая папка изменена  на:" + os.getcwd() + "\n")
    author = open("author.txt", "r")
    author_info = author.readlines()

    author.close()

    repo_author_info.configure(
        text="Фамилия: " + author_info[0] + "Имя: " + author_info[1] + "Язык: " + author_info[2])

    if os.path.exists("task1"):  # Проверка какие задания сделаны
        rad1.place(x=10, y=185)
    if os.path.exists("task2"):
        rad2.place(x=10, y=205)
    if os.path.exists("task3"):
        rad3.place(x=10, y=225)
    if os.path.exists("task4"):
        rad4.place(x=10, y=245)


##############################################
# Интерфейс
test1 = pd.read_csv("test_data/data_1.csv", sep=' ')
file = ''
window = Tk()  # Создание окна
window.title("PLAutoChecker v.0.1")  # Название окна
window.geometry('600x500')  # Размер окна

menu = Menu(window)
new_menu = Menu(menu, tearoff=0)
new_menu.add_command(label='Открыть',
                     command=open_file)
menu.add_cascade(label='Файл',
                 menu=new_menu)
window.config(menu=menu)

repo_language_label = Label(window,
                            text="Выбор языка:    ",
                            padx=5)
repo_author_info = Label(window,
                         text="Фамилия: \nИмя: \nЯзык: ",
                         bg='white',
                         width=30,
                         justify=LEFT,
                         padx=5,
                         anchor=W)
repo_author_info_head = Label(window,
                              text="Информация",
                              width=30,
                              justify=LEFT,
                              padx=5,
                              anchor=W)
txt_test_head = Label(window,
                      text="Ход теста",
                      width=30,
                      justify=LEFT,
                      padx=5,
                      anchor=W)
txt_log_head = Label(window,
                     text="Лог программы",
                     width=30,
                     justify=LEFT,
                     padx=5,
                     anchor=W)

tasks_head = Label(window,
                   text="Номер задания",
                   width=30,
                   justify=LEFT,
                   padx=5,
                   anchor=W)

rad1 = Radiobutton(window, text='task1', value=1)
rad2 = Radiobutton(window, text='task2', value=2)
rad3 = Radiobutton(window, text='task3', value=3)
rad4 = Radiobutton(window, text='task4', value=4)

repo_language_choice = Combobox(window, width=15)
repo_language_choice['values'] = ("Python", "Java", "C++")
repo_language_choice.current(0)

repo_button = Button(window,
                     text="Проверить",
                     command=repo_button_click,
                     width=30,
                     height=2,
                     padx=3,
                     bg='white')

sort_button = Button(window,
                     text="Сортировка",
                     command=repo_button_click,
                     width=20,
                     height=2,
                     padx=3,
                     bg='white')

delete_button = Button(window,
                       text="Очистить",
                       command=repo_button_click,
                       width=20,
                       height=2,
                       padx=3,
                       bg='white')

txt_test = scrolledtext.ScrolledText(window, width=40, height=17)
txt_log = scrolledtext.ScrolledText(window, width=70, height=6)

repo_author_info_head.place(x=10, y=5)
repo_author_info.place(x=10, y=25)

tasks_head.place(x=10, y=165)

repo_language_label.place(x=10, y=85)
repo_language_choice.place(x=121, y=85)
txt_test_head.place(x=250, y=5)
txt_log_head.place(x=10, y=370)
txt_test.place(x=250, y=25)
txt_log.place(x=10, y=390)
repo_button.place(x=10, y=120)
sort_button.place(x=250, y=310)
delete_button.place(x=420, y=310)

window.mainloop()
