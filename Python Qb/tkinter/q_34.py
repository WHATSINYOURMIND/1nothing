import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
root = tk.Tk()
root.title("Progressbar")
root.geometry('300x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(root, length=220, style='black.Horizontal.TProgressbar')
bar['value'] = 80
bar.grid(column=0, row=0)
root.mainloop()
