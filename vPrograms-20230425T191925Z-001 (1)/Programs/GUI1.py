from tkinter import *
root=Tk()
c=Canvas(root,bg='blue',height=1000,width=1200,cursor='pencil')

l=c.create_line(10,10,30,50,width=4,fill='white')
r=c.create_rectangle(500,200,700,600,width=2,fill='gray',outline='black',activefill='green')
o=c.create_oval(100,100,400,300,width=3,fill='yellow',outline='red',activefill='green')
p=c.create_polygon(10,10,200,200,300,200,width=4,fill='yellow',outline='black',activefill='blue')
a=c.create_arc(300,100,100,200,start=180,extent=180,width=3,style='arc')
f=('Times',40,'bold italic underline')
t=c.create_text(500,100,text='Vidyalankar',font=f,fill='gold')
c.pack()#Canvas ko root window ke upar bithayega
root.mainloop()
