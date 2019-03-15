from tkinter import *

class Application(Frame):
    
    def __init__(self,master):
        self.numberindex = 0
        self.numbers = ["0", "0"]
        self.operate = ""
        self.output = None
        super(Application, self).__init__(master)
        self.grid()
        self.createwidgets()

    def createwidgets(self):
        self.screen = Text(self, width = 20, height = 5, wrap = WORD)
        self.screen.grid(row = 0, column = 0, columnspan = 4)
        
        clearbutton = Button(self, text = "    C   ", command = self.clear)
        clearbutton.grid(row = 1, column = 0, sticky = W)

        button1 = Button(self, text = "    1    ", command = self.one)
        button1.grid(row = 4, column = 0, sticky = W)

        button2 = Button(self, text = "    2    ", command = self.two)
        button2.grid(row = 4, column = 1, sticky = W)

        button3 = Button(self, text = "    3    ", command = self.three)
        button3.grid(row = 4, column = 2, sticky = W)

        button4 = Button(self, text = "    4    ", command = self.four)
        button4.grid(row = 3, column = 0, sticky = W)
        
        button5 = Button(self, text = "    5    ", command = self.five)
        button5.grid(row = 3, column = 1, sticky = W)

        button6 = Button(self, text = "    6    ", command = self.six)
        button6.grid(row = 3, column = 2, sticky = W)

        button7 = Button(self, text = "    7    ", command = self.seven)
        button7.grid(row = 2, column = 0, sticky = W)

        button8 = Button(self, text = "    8    ", command = self.eight)
        button8.grid(row = 2, column = 1, sticky = W)

        button9 = Button(self, text = "    9    ", command = self.nine)
        button9.grid(row = 2, column = 2, sticky = W)

        button0 = Button(self, text = "    0    ", command = self.zero)
        button0.grid(row = 5, column = 1, sticky = W)

        buttondiv = Button(self, text = "    /    ", command = self.div)
        buttondiv.grid(row = 1, column = 3, sticky = W)

        buttonmult = Button(self, text = "    *    ", command = self.mult)
        buttonmult.grid(row = 2, column = 3, sticky = W)

        buttonmin = Button(self, text = "    -    ", command = self.sub)
        buttonmin.grid(row = 3, column = 3, sticky = W)

        buttonplus = Button(self, text = "    +   ", command = self.add)
        buttonplus.grid(row = 4, column = 3, sticky = W)

        buttonequ = Button(self, text = "    =    ", command = self.equals)
        buttonequ.grid(row = 5, column = 3, columnspan = 2, sticky = W)

        buttondec = Button(self, text = "    .     ", command = self.clear)
        buttondec.grid(row = 5, column = 0, columnspan = 2, sticky = W)


    def one(self):
        self.screen.insert(END, 1)
        self.numbers[self.numberindex] += "1"

    def two(self):
        self.screen.insert(END, 2)
        self.numbers[self.numberindex] += "2"

    def three(self):
        self.screen.insert(END, 3)
        self.numbers[self.numberindex] += "3"

    def four(self):
        self.screen.insert(END, 4)
        self.numbers[self.numberindex] += "4"

    def five(self):
        self.screen.insert(END, 5)
        self.numbers[self.numberindex] += "5"

    def six(self):
        self.screen.insert(END, 6)
        self.numbers[self.numberindex] += "6"

    def seven(self):
        self.screen.insert(END,7)
        self.numbers[self.numberindex] += "7"

    def eight(self):
        self.screen.insert(END, 8)
        self.numbers[self.numberindex] += "8"

    def nine(self):
        self.screen.insert(END, 9)
        self.numbers[self.numberindex] += "9"

    def zero(self):
        self.screen.insert(END, 0)
        self.numbers[self.numberindex] += "0"

    def div(self):
        self.screen.insert(END, "/")
        self.operate = "/"
        self.numberindex += 1

    def mult(self):
        self.screen.insert(END, "*")
        self.operate = "*"
        self.numberindex += 1

    def sub(self):
        self.screen.insert(END, "-")
        self.operate = "-"
        self.numberindex += 1

    def add(self):
        self.screen.insert(END, "+")
        self.operate = "+"
        self.numberindex += 1

    def equals(self):
        self.output = None
        if self.operate == "/":
            while True:
                if self.numbers[1] != 0:
                    self.screen.delete(0.0, END)
                    self.screen.insert(0.0, "ERR0R")
                else:
                    self.output = int(self.numbers[0])/int(self.numbers[1])

        elif self.operate == "*":
            self.output = int(self.numbers[0]) * int(self.numbers[1])

        elif self.operate == "-":
            self.output = int(self.numbers[0]) - int(self.numbers[1])

        elif self.operate == "+":
            self.output = int(self.numbers[0]) + int(self.numbers[1])

        self.screen.delete(0.0, END)
        self.screen.insert(0.0, self.output)
        self.numbers[0] = self.output
        self.numbers[1] = "0"
        self.numberindex = 0

    def clear(self):
        self.screen.delete(0.0, END)
        self.numberindex = 0
        self.output = None
        self.numbers = ["0", "0"]


root = Tk()
root.title("Calculator")

app = Application(root)

root.mainloop()
