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
    def __init__(self, name, year, pressing, artist, purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice, num):
        self.name = name
        self.year = year
        self.pressing = pressing
        self.artist = artist
        self.moreinfo = Moreinfo(purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice)
        self.num = playlist[i]

    def menu():
        choice = input("Would you like to add a vinyl (1), look up more info (2), add more info(3), or randomly generate a vinyl(4)")
        if choice == "1":
            Record.addvinyl()
        elif choice == "2":
            lookmoreinfo()
        elif choice == "3":
            moreinfo(purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice)
        elif choice == "4":
            rangen()
        else:
            quit = input("would you like to quit? y or n")
            if quit == "n":
                Record.menu()
            else:
                input("press enter")
        
    def addvinyl():
        while True:
            name = input("Please input the name of the vinyl")
            year = input("Please input the year the vinyl was made?")
            pressing = input("please input the pressing (Designs or colors)?")
            artist = input("please input the artist name")
            choice2 = input("would you like to add more information? y or n")
            if choice2 == "y":
                Record.moreinfo(purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice)
            else:
                choice3 = input("Would you like to add another vinyl? y or n")
                if choice3 == "y":
                    Record.addvinyl()
                else:
                    Record.menu()




class Moreinfo(object):
    def __init__(self, purchasedate, purchaseloc, solddate, soldlocation, soldprice, purchaseprice):
        self.purchasedate = purchasedate
        self.purchaseloc = purchaseloc
        self.solddate = solddate
        self.soldlocation = soldlocation
        self.soldprice = soldprice
        self.purchaseprice = purchaseprice


##class Application(Frame):
##    def __init__(self, master):
##        # Initialize the Frame
##        super(Application, self).__init__(master)
##        self.grid()
##        self.create_widget()
##        self.records = []
##    def create_widget(self):
##        label = Label(self, text="Record Title")
##        label.grid(row=0, column = 0, sticky = W)
##        name = Entry(self)
##        name.grid(row = 0, column = 1, sticky = W)  
##        submit = Button(self, text = "submit record", command = self.submit)
##        submit.grid(row=1, column = 1, columnspan = 2, sticky = W)
##
##
##    def submit(self):
##        print(name)




def main():
##    root = Tk()
##    root.title("Click Counter")
##    root.geometry("200x50")
##    app = Application(root)
      Record.menu()

    


main()
