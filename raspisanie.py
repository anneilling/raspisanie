from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
aken=Tk()
aken.title("Расписание")
aken.geometry("955x710")
aken.configure(bg="white")
def uus_aken(ind:int):
    if askyesno("Küsimus","Kas teen lahti?"):
        showinfo("Vatus","Teen aken lahti")
    else:
        showinfo("Vastus","Panen aken kinni")
        aken.destroy()
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    #texts

Label(aken, borderwidth=1, relief="solid",text=" ", width=20,height=5).grid(row=0, column=0) #номерурока
Label(aken, borderwidth=1, relief="solid",text=" 0 ", width=10,height=5).grid(row=0, column=1)
Label(aken, borderwidth=1, relief="solid",text=" 1 ", width=10,height=5).grid(row=0, column=2)
Label(aken, borderwidth=1, relief="solid",text=" 2 ", width=10,height=5).grid(row=0, column=3)
Label(aken, borderwidth=1, relief="solid",text=" 3 ", width=10,height=5).grid(row=0, column=4)
Label(aken, borderwidth=1, relief="solid",text=" 4 ", width=10,height=5).grid(row=0, column=5)
Label(aken, borderwidth=1, relief="solid",text=" 5 ", width=10,height=5).grid(row=0, column=6)
Label(aken, borderwidth=1, relief="solid",text=" 6 ", width=10,height=5).grid(row=0, column=7)
Label(aken, borderwidth=1, relief="solid",text=" 7 ", width=10,height=5).grid(row=0, column=8)
Label(aken, borderwidth=1, relief="solid",text=" 8 ", width=10,height=5).grid(row=0, column=9)
Label(aken, borderwidth=1, relief="solid",text=" 9 ", width=10,height=5).grid(row=0, column=10)
Label(aken, borderwidth=1, relief="solid",text=" 10 ", width=10,height=5).grid(row=0, column=11)


Label(aken, borderwidth=0, relief="solid", text="7.40-8.25", width=10,height=2).grid(row=0, column=1,sticky=S) #времяуроков
Label(aken, borderwidth=0, relief="solid", text="8.30-9.15", width=10,height=2).grid(row=0, column=2,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="9.20-10.05", width=10,height=2).grid(row=0, column=3,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="10.10-10.55", width=10,height=2).grid(row=0, column=4,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="11.00-11.45", width=10,height=2).grid(row=0, column=5,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="11.50-12.35", width=10,height=2).grid(row=0, column=6,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="12.40-13.25", width=10,height=2).grid(row=0, column=7,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="13.30-14.15", width=10,height=2).grid(row=0, column=8,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="14.20-15.05", width=10,height=2).grid(row=0, column=9,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="15.10-15.55", width=10,height=2).grid(row=0, column=10,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="16.00-16.45", width=10,height=2).grid(row=0, column=11,sticky=S)


Label(aken, borderwidth=1, relief="solid",text="Esmaspäev", width=20,height=8).grid(row=1, column=0) #днинедели
Label(aken, borderwidth=1, relief="solid",text="Teisipäev", width=20,height=8).grid(row=2, column=0)
Label(aken, borderwidth=1, relief="solid",text="Kolmapäev", width=20,height=8).grid(row=3, column=0)
Label(aken, borderwidth=1, relief="solid",text="Neljapäev", width=20,height=8).grid(row=4, column=0)
Label(aken, borderwidth=1, relief="solid",text="Reede", width=20,height=8).grid(row=5, column=0)


Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=1) #1урок
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=1)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=1)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=1)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=1)



Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=2) #понедельник
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=3)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=4)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=5)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=6)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=7)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=8)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=9)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=10)
Label(aken, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=11)


Label(aken, borderwidth=1, bg="#cab4c7", relief="solid",text="Eesti keel", width=10,height=4).grid(row=1, column=2,sticky=S)
Label(aken, relief="solid",borderwidth=0, bg="#cab4c7" ,text="B234", width=5,height=1).grid(row=1, column=2,sticky=SW)
Label(aken, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8).grid(row=1, column=3, sticky=N+S+W+E, columnspan=2)
Label(aken, borderwidth=1, bg="#fcb9d0", relief="solid",text="Matemaatika", width=10,height=8).grid(row=1, column=5, sticky=N+S+W+E, columnspan=2)
Label(aken, borderwidth=1, bg="#94ed80", relief="solid",text="Keel ja kirjandus", width=10,height=8).grid(row=1, column=8, sticky=N+S+W+E, columnspan=2)
Label(aken, borderwidth=1, bg="#fcb9d0", relief="solid",text="Tugiõpe\n(matema\natika)", width=10,height=8).grid(row=1, column=10, sticky=N+S+W+E)





























aken.mainloop()
