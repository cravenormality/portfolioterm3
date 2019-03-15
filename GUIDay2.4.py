from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create instruction label
        self.inst_lbl = Label(self, text = "Enter password for the secret life")
        self.inst_lbl.grid(row = 100, column = 500, columnspan = 2, sticky = N)

        self.pw_lbl = Label(self, text = "Password")
        self.pw_lbl.grid(row = 200, column = 500, columnspan = 1000, sticky = N)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 300, column = 500, columnspan = 1000, sticky = N)

        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 400, column = 500, columnspan = 1000, sticky = N)

        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 500, column = 500, columnspan = 2, sticky = N)

    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "42"
        else:
            message = "That's not the correct password, so I can't share the secret with you"
        self.secret_txt.delete(0,0, END)
        self.secret_txt.insert(0,0, message)


root = Tk()
root.title("Click Counter")
root.geometry("1000x500")
app = Application(root)

root.mainloop()
