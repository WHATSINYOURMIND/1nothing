import tkinter as tk
root = tk.Tk()
root.title("Radio Buttons")
root.geometry('350x200')
root.resizable(0,0)
radio1 = tk.Radiobutton(root, text='First', value = 1)
radio2 = tk.Radiobutton(root, text='Second', value = 2)
radio3 = tk.Radiobutton(root, text='Third', value = 3)
radio1.grid(column = 0, row=0)
radio2.grid(column = 5, row=0)
root.mainloop()