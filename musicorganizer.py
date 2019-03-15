#Jessica Weinburger
#3rd term final project - Python (Music Organizer)
# 4/5
#3/4/2019

import random

playlist = []
sold = []
moreinfo = []

def addvinyl():
    songs = input("Type the vinyl name")
    if songs not in playlist:
        playlist.append(songs)
        print(playlist)
        moreinfoans = input("would you like to add more info about that vinyl? y or n")
        if moreinfoans == "y":
            moreinfos()
        else:
            main()
    else:
        print("That album already exist in your playlist.")
        answer = input("Would you like to try again? y or n")
        if answer == "y":
            addvinyl()
        else:
            print("Thank you for coming.")
            main()
        answer2 = input("Would you like to add another vinyl? y or n")
        if answer2 == "y":
            addvinyl()
        else:
            print("thank you for adding your vinyl.")
            main()

def deletevinyl():
    song = input("Type the vinyl name here")
    if song in playlist:
        playlist.remove(song)
        print("That song was successfuly removed")
        sold.append(song)
        solddate = input("please enter the date you sold the vinyl")
    else:
        print("Please input a valid vinyl name")

def moreinfos():
    songs3 = input("please enter the vinyl name you would like to edit")
    if songs3 in playlist:
        artist = input("please enter the artist")
        bought = input("please enter the date you bought the vinyl")
        place = input("please enter the place you bought the vinyl")
        info = input("please enter any other info you know about the vinyl")
        return artist, bought, place, info
    else:
        print("There was an error fetching your requested vinyl please try again")
        moreinfos()

def randomvinyl():
    pass

def main():
    print("Welcome to The Vinyl Sorter. Below is a selection please choose one to continue.")
    addvinyl()
    deletevinyl()
    print(sold)
    print(playlist)
    moreinfos()

main()

        
        