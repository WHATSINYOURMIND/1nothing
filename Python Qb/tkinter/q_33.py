import tkinter as tk
parent = tk.Tk()
# create the widget.
mytext = tk.Text(parent)
# insert a string at the beginning
mytext.insert('1.0', "- Python exercises, solution -")
# insert a string into the current text
mytext.insert('end', ' Practice,')
# delete the first and last character (including a newline character)
mytext.delete('1.19')
mytext.delete('end - 5 chars')
mytext.pack()
parent.mainloop()


