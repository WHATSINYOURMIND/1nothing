from tkinter import *
from tkinter import messagebox
root=Tk()

def hellocallback():
    s1=e1.get()
    s2=e2.get()
    if s1=='SSS' and s2=='PYTHON':
        messagebox.showinfo('Welcome','Successful login...')
    else:
        messagebox.showerror('Error','Inavlid User...')
        
f=Frame(root,height=400,width=500)
f.pack()
l1=Label(f,text='Username',width=20,height=2)
l2=Label(f,text='Password',width=20,height=2)
l3=Label(f,text='Favourite Subject',width=20,height=2)
l4=Label(f,text='Gender',width=20,height=2)
e1=Entry(f,width=20)
e2=Entry(f,width=20,show='*')
c1=Checkbutton(f,text="CP")
c2=Checkbutton(f,text="JAVA")
c3=Checkbutton(f,text="Python")
var=IntVar()#Group create karana
r1=Radiobutton(f,text='Male',variable=var,value=1)
r2=Radiobutton(f,text='Female',variable=var,value=2)
b=Button(f,text='SHOW',width=15,height=3,command=hellocallback)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
c1.grid(row=2,column=1)
c2.grid(row=2,column=2)
c3.grid(row=2,column=3)
l4.grid(row=3,column=0)
r1.grid(row=3,column=1)
r2.grid(row=3,column=2)
b.grid(row=4,column=0)
root.mainloop()


