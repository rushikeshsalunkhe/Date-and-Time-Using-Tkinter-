#wap button info date time  wala
from tkinter import *  #tk method button label 
from tkinter.messagebox import *   #invalid wale promt milte hai isse 
from datetime import *
from webbrowser import *

root = Tk()
root.title("date n time app ")
root.geometry("400x400+200+200")

def f1():
	d = datetime.now().date()
	showwarning("Date", d)


def f2():
	t = datetime.now().time()
	showwarning("Time", t)

def f3():
	dt = datetime.now()
	showerror("Date Time", dt)

def f4():
	open ("www.google.com")
btnDate = Button(root, text = "Date " , font = ('arial ' , 20 , 'bold') , width= 10 , command = f1 )
btnTime = Button(root, text = "Time " , font = ('arial ' , 20 , 'bold') , width= 10 , command = f2)
btnDateTime = Button(root, text = "datentime " , font = ('arial ' , 20 , 'bold') , width= 10 , command=f3  )
btnVisitUs= Button(root, text = "Visitus " , font = ('arial ' , 20 , 'bold') , width= 10, command=f4 )



btnDate.pack(pady=10)
btnTime.pack(pady=10)
btnDateTime.pack(pady=10)
btnVisitUs.pack(pady=10)




root.mainloop()