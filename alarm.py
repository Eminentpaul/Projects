import tkinter as tk
from tkinter import *
from tkinter import messagebox as mg
import os, time, winsound


def createWidget():
    label1 = Label(root, text="Enter the Time in HH:MM - ")
    label1.grid(row=0, column=0, padx=5, pady=5)

    global entry1

    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    label2 = Label(root, text="Enter a Message - ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2

    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1, padx=5, pady=5)

    butt = Button(root, text='Submit', width=10, command=submit)
    butt.grid(row=2, column=1)

    global label3
    label3 = Label(root, text="")
    label3.grid(row=3, column=0)


def message1():
    global entry1, label3
    Alarmtimelabel = entry1.get()
    label3.config(text='The Alarm is Counting....')
    mg.showinfo("Alarm Clock", f'The Alarm time is: {Alarmtimelabel}')


def submit():
    global entry1, entry2, label3
    Alarmtime = entry1.get()
    message1()
    currenttime = time.strftime("%H:%M")
    alarm_message = entry2.get()
    print(f'Teh Alarm time is: {Alarmtime}')

    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)

    if Alarmtime == currenttime:
        print("Playing Alarm Sound...")
        winsound.PlaySound("*", winsound.SND_ASYNC)
        label3.config(text="Alarm Sound Playing>>>>")
        mg.showinfo("Alarm Messgae", f'The Message is: {alarm_message}')


root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")

createWidget()

root.mainloop()
