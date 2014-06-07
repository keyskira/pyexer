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
        try:
            i = addressbook.contacts[name]
            print i
        except KeyError:
            print "No such people"





root = Tk()
root.minsize(500,500)
app = App(root)

root.mainloop()
