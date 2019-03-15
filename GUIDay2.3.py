from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        """Create button which displays number of clicks"""
        self.bttn = Label(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)

root = Tk()
root.title("Click Counter")
root.geometry("200x50")
app = Application(root)

root.mainloop()