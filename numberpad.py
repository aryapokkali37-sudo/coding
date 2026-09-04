from tkinter import *
window = Tk()
window.title('number pad')
window.geometry('420x100')

numes=[[9,8,7],[6,5,4],[3,2,1],['π',0,'∑']]

for i in range(4):
    window.columnconfigure(1,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=75)
    for l in range(0,3):
        fr=Frame(
            master=window,
            relief=SUNKEN,
            borderwidth=2
        )
        fr.grid(column=i,row=l)
        lbl=Label(master=fr,text=numes[i][l],bg='#d0efff')
        lbl.pack(padx=3,pady=3)