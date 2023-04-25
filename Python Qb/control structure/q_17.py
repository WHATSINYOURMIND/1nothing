import tkinter as tk
parent = tk.Tk()
parent.title("Welcome to tkinter")
my_label = tk.Label(parent, text="Sarah", font=("Arial Bold", 60))
my_label.grid(column=0,row=0)
parent.mainloop()
