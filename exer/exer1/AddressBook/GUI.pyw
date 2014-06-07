from Tkinter import *
import tkSimpleDialog
import addressbook


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.quitbutton = Button(frame, text="QUIT", underline=0, command=frame.quit)
        self.quitbutton.pack(side=LEFT)

        self.runbutton = Button(frame, text="RUN", underline=0, command=self.run)
        self.runbutton.pack(side=LEFT)

    def run(self):
        name = tkSimpleDialog.askstring("find people","Please enter the name")
        i = addressbook.contacts[name]
        print i


root = Tk()
app = App(root)

root.mainloop()
