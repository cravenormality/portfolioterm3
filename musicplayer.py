#Jessica Weinburger Python Final Project

from tkinter import *
import progressBar
from functools import partial
import pygame

songs = []

class Application(Frame):
    song_counter = 0
    current_list = []
    current_playing_index = 0
    current_focus_index = 0
    paused = False

    def __init__(self):
        Tk.__init__(self)
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.init()
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.sWidth=self.winfo_screenwidth()
        self.sHeight=self.winfo_screenheight()

        self.frame1 = Frame(height=self.precent(self.sHeight, 80), width=self.precent(self.sWidth, 100))
        
        self.play=Button(self, text = "Play", width = 5)
        self.play.pack(side=LEFT)
        self.pause=Button(self, text = "pause", width = 5, command = self.pause)
        self.pause.pack(side=LEFT)
        self.previous=Button(self, text ="previous", width = 5, command = self.playprevious)
        self.previous.pack(side=LEFT)
        self.stop=Button(self,text="stop", width = 5)
        self.stop.pack(side=LEFT)
        self.next=Button(self, text="next", width = 5, command = self.playnext)
        self.next.pack(side=LEFT)

    def perent(self, perc, value):
        return value*perc/100

    def increm(self, event):
        self.pbar.progress["length"]=self.percent(self.winfo_width(), 80)

    def isfocused(self,widget):
        return self.current_Focus_index==self.current_list.index(widget)

    def setfocus(Self, label, event):
        if self.current_focus_index!=0 and self.current_list.index(label)!=self.current_focus_index:
            self.current_list[self.current_focus_index].configure(bg="white")
        label.focus_set()
        self.color_config(label,"yellow",event)
        self.current_focus_index=self.current_list.index(label)

    def setFocusNext(self,event):
        if not self.current_focus_index>=len(self.current_list)-1:
            self.current_focus_index+=1
            self.setFocus(self.current_list[self.current_focus_index],event)

    def setFocusPrev(self,event):
        if not self.current_focus_index<=1:
            self.current_focus_index-=1
            self.setFocus(self.current_list[self.current_focus_index],event)

    def playsong(self, id, event):
        pygame.mixer.music.load(songs[id])
        pygame.mixer.music.play()
        self.current_playing_index = id

    def playnext(self):
        if len(self.current_list)>self.currrent_planying_index+1:
            self.playsong(self.current_playing_index-1, "")

    def pause(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.pause.configure(text="Play")
        else:
            pygame.mixer.music.unpause()
            self.ppause.configure(text="Pause")
        self.paused = not self.paused

    def addButton(self):
        add = Button(self, text="song.mp3", relief=Groove, state=DISABLED)
        add.pack(side=LEFT)
        add.place(y=self.song_counter)
        add.bind('<Enter>')
        add.bind('<Down>', self.setFocusNext)
        add.bind('<Up>', self.setFocusPrev)
        add.bind('<Leave>')
        add.bind('<Button-1>')
        self.current_list(add)
        add.configure(text=songs[self.current_list.index(add)])
        add.bind('<Double-Button-1>', partial(self.playSong, self.current_list.index(add)))
        add.bind('Return>', partial(self.playsong,self.current_list.index(add)))
        self.song_counter +=40


def main():
    root = Tk()
    root.title("Python Music Player")
    root.geometry(format(self.sHeight()), width=self.precent(self.sWidth()))
    app = Application(root)
    for _ in range(len(songs)-1):
        app.addButton()

main()
