from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.records = []
    def create_widget(self):
        self.txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.txt.grid(row = 0, column = 0, columnspan = 4, sticky = N)

        clear = Button(self, text = "C", command = self.clear)
        clear.grid(row = 1, column = 0, columnspan = 4, sticky = W) 

        buttondiv = Button(self, text = "/", command = self.divide)
        buttondiv.grid(row = 1, column = 4, columnspan = 4, sticky = W)  

        button7 = Button(self, text = "7", command = self.seven)
        button7.grid(row = 2, column = 1, columnspan = 4, sticky = W)  

        button8 = Button(self, text = "8", command = self.eight)
        button8.grid(row = 2, column = 2, columnspan = 4, sticky = W) 

        button9 = Button(self, text = "9", command = self.nine)
        button9.grid(row = 2, column = 3, columnspan = 4, sticky = W) 

        button4 = Button(self, text = "4", command = self.four)
        button4.grid(row = 3, column = 1, columnspan = 4, sticky = W) 

        button5 = Button(self, text = "5", command = self.five)
        button5.grid(row = 3, column = 2, columnspan = 4, sticky = W) 

        button6 = Button(self, text = "6", command = self.six)
        button6.grid(row = 3, column = 3, columnspan = 4, sticky = W) 

        buttonmul = Button(self, text = "*", command = self.multiple)
        buttonmul.grid(row = 2, column = 4, columnspan = 4, sticky = W)

        buttonsub = Button(self, text = "-", command = self.subtract)
        buttonsub.grid(row = 3, column = 4, columnspan = 4, sticky = W) 

        button1 = Button(self, text = "1", command = self.one)
        button1.grid(row = 4, column = 1, columnspan = 4, sticky = W) 

        button2 = Button(self, text = "2", command = self.two)
        button2.grid(row = 4, column = 2, columnspan = 4, sticky = W) 

        button3 = Button(self, text = "3", command = self.three)
        button3.grid(row = 4, column = 3, columnspan = 4, sticky = W)

        buttonplus = Button(self, text = "+", command = self.plus)
        buttonplus.grid(row = 4, column = 4, columnspan = 4, sticky = W)  

        button0 = Button(self, text = "0", command = self.zero)
        button0.grid(row = 5, column = 2, columnspan = 4, sticky = W) 

        buttondec = Button(self, text = ".", command = self.decimal)
        buttondec.grid(row = 5, column = 3, columnspan = 4, sticky = W) 

        buttonequ = Button(self, text = "=", command = self.equal)
        buttonequ.grid(row = 5, column = 4, columnspan = 4, sticky = W) 


    def clear(self):
        pass

    def divide(self):
        pass
    
    def seven(self):
        pass

    def eight(self):
        pass

    def nine(self):
        pass

    def multiple(self):
        pass
    
    def four(self):
        pass

    def five(self):
        pass

    def six(self):
        pass

    def subtract(self):
        pass
    
    def one(self):
        pass
    
    def two(self):
        pass

    def three(self):
        pass
    
    def plus(self):
        pass
    
    def zero(self):
        pass

    def decimal(self):
        pass

    def equal(self):
        pass


def main():
    root = Tk()
    root.title("Calculator")
    app = Application(root)


main()