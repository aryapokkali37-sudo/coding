from tkinter import *
window = Tk()
window.title('window')
window.geometry('200x100')
lobel = Label(text='i like π and dogs')
fg="FF0000"
bg="DE15EB"
height=2
width=20
lobel.pack()
N_entry=Entry()
N_entry.pack()
N=N_entry.get
window.mainloop()

