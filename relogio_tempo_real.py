from tkinter import *
import time

class App(Frame):
    def __init__(root,master=None):
        Frame.__init__(root, master)
        root.master = master
        root.label = Label(text="", fg="Red", font=("Helvetica", 18))
        root.label.place(x=50,y=80)
        root.update_clock()



    def update_clock(root):
        now = time.strftime("%H:%M:%S")
        root.label.configure(text=now)
        root.after(1000, root.update_clock)



class Window(Frame):
    def __init__(root, master=None):
        Frame.__init__(root, master)
        root.master = master
        root.pack(fill=BOTH, expand=1)

root = Tk()

#atualização do relogio
app = App(root)
root.after(1000, app.update_clock)

root.mainloop()