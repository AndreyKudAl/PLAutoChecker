from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from tkinter import scrolledtext
from tkinter.ttk import Combobox
import tkinter.messagebox as mb
import zipfile
import os
import shutil
import subprocess
import pandas as pd


def show_warning():
    msg = "Сначала необходимо открыть файл!"
    mb.showwarning("Предупреждение", msg)


def first_task():
    rw = ''
    for i in range(len(test1.index)):
        script = subprocess.run(["python", "1.py", str(test1.loc[i, 'n']), str(test1.loc[i, 'm'])],
                                stdout=subprocess.PIPE)
        if int(str(script.stdout)[2:-1]) == int(test1.loc[i, 'right_answer']):
            rw = 'YES'
        else:
            rw = 'ERROR'
        test_output_1.loc[len(test_output_1.index)] = [str(script.stdout)[2:-1], str(test1.loc[i, 'right_answer']), rw]
        print()

    txt_log.insert(INSERT, "Task1 проверен!\n")


def output_result():
    txt_test.delete(1.0, END)
    if tasks_choice.get() == "task1":
        txt_test.insert(INSERT, test_output_1)


def sort_errors():
    txt_test.delete(1.0, END)
    if tasks_choice.get() == "task1":
        txt_test.insert(INSERT, test_output_1.sort_values(by="RW"))


def repo_button_click():
    if file == '':
        show_warning()
        return
    if repo_language_choice.get() == "Python":
        if os.path.exists("task1"):
            os.chdir("task1")
            first_task()

    output_button.place(x=10, y=310)


def open_file():
    global file

    test_output_1.drop(test_output_1.index, inplace=True)  # Очищаем ДатаФрейм перед следующим прогоном

    os.chdir(default_path)
    tasks_choice['values'] = []
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
        tasks_choice['values'] = tuple(list(tasks_choice['values']) + ["task1"])

    if os.path.exists("task2"):
        tasks_choice['values'] = tuple(list(tasks_choice['values']) + ["task2"])

    if os.path.exists("task3"):
        tasks_choice['values'] = tuple(list(tasks_choice['values']) + ["task3"])

    if os.path.exists("task4"):
        tasks_choice['values'] = tuple(list(tasks_choice['values']) + ["task4"])


##############################################
# Интерфейс
default_path = os.getcwd()
test_output_1 = pd.DataFrame({
    'output': [],
    'right_answer': [],
    'RW': []

})
pd.options.display.max_rows = 2000  # Увеличиваем максимальный вывод значений датафрейма

test1 = pd.read_csv("test_data/data_1.csv", sep=' ')
file = ''
window = Tk()  # Создание окна
window.title("PLAutoChecker v.0.1")  # Название окна
window.geometry('875x500')  # Размер окна
window.resizable(False, False)

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

repo_language_choice = Combobox(window, width=15)
repo_language_choice['values'] = ("Python", "Java", "C++")
repo_language_choice['state'] = 'readonly'
repo_language_choice.current(0)

tasks_choice = Combobox(window, width=15)
tasks_choice['state'] = 'readonly'

txt_test = scrolledtext.ScrolledText(window, width=75, height=17)
txt_log = scrolledtext.ScrolledText(window, width=105, height=6)

repo_button = Button(window,
                     text="Проверить",
                     command=repo_button_click,
                     width=30,
                     height=2,
                     padx=3,
                     bg='white')

sort_button = Button(window,
                     text="Сортировка по индексу",
                     command=output_result,
                     width=20,
                     height=2,
                     padx=3,
                     bg='white')

sort2_button = Button(window,
                      text="Сортировка по ошибкам",
                      command=sort_errors,
                      width=20,
                      height=2,
                      padx=3,
                      bg='white')

output_button = Button(window,
                       text="Вывести",
                       command=output_result,
                       width=30,
                       height=2,
                       padx=3,
                       bg='white')

repo_author_info_head.place(x=10, y=5)
repo_author_info.place(x=10, y=25)

tasks_head.place(x=10, y=170)
tasks_choice.place(x=121, y=170)

repo_language_label.place(x=10, y=85)
repo_language_choice.place(x=121, y=85)
txt_test_head.place(x=250, y=5)
txt_log_head.place(x=10, y=370)
txt_test.place(x=250, y=25)
txt_log.place(x=10, y=390)
repo_button.place(x=10, y=120)

sort_button.place(x=250, y=310)
sort2_button.place(x=420, y=310)

window.mainloop()
