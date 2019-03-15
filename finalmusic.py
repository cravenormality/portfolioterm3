#Jessica Weinburger
#3rd term final project - Python (Music Organizer)
# 4/5
#3/4/2019

import random

from tkinter import *

playlist = []
sold = []
moreinfo = []

class Record(object):
    def __init__(self, name, year, pressing, artist):
        self.name = name
        self.year = year
        self.pressing = pressing
        self.artist = artist
        self.moreinfo = Moreinfo(purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice)

class Moreinfo(object):
    def __init__(self, purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice):
        self.purchasedate = purchasedate
        self.purchaseloc = purchaseloc
        self.solddate = solddate
        self.soldlocation = soldlocation
        self.soldprice = soldprice
        self.purchaseprice = purchaseprice


class Application(Frame):
    def __init__(self, master):
        # Initialize the Frame
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.records = []
    def create_widget(self):
        label = Label(self, text="Record Title")
        label.grid(row=0, column = 0, sticky = W)
        name = Entry(self)
        name.grid(row = 0, column = 1, sticky = W)  
        submit = Button(self, text = "submit record")  




def main():
    root = Tk()
    root.title("Click Counter")
    root.geometry("200x50")
    app = Application(root)


main()