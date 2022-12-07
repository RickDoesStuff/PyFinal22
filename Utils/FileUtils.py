import csv
import pygame
from Objects.MusicPerInst import MusicPerInst
from Objects.Note import Note
from Objects.Song import Song


def fileToSong(fileName):
    """
    Converts a file to a song type
    :param String fileName:
    :return Song:
    """

    with open(fileName, newline="") as file:
        reader = csv.reader(file)

        instPer = []

        title = None
        sig = None
        notes = []
        inst = None
        key = None
        for row in reader:
            if len(row) == 3:  # it is either a header or new instrument
                if "/" in row[1]:  # it is a header bc it contains time sig
                    title = row[0]
                    sig = row[1]
                    print("Header found")
                else: # it is a
                    if key is not None:  # if there are no keys skip this part, that means we are not at the start
                        instPer.append(MusicPerInst(notes, inst, key))  # only do this if we are not at start
                        notes = []
                        print("notes were cleared and inst list appended: key!=None: ", key)
                    # always going to run this part if it's a new instrument
                    inst = row[0]
                    key = row[1]
                    print("new inst and key: ", inst, key)
            else:  # it's not a header or new instrument
                try:
                    note = Note(row[0], round(float(row[1]), 1), row[2], row[3], row[4]) # note name, note length, note volume, note fadout time, boolean to pause
                    #pygame.mixer.Sound("PianoNotes/"+row[0]+".wav").set_volume(float(row[2]))
                    #pygame.mixer.fadeout(int(row[3]))
                    #if row[4] == True:
                    #    pygame.mixer.pause()

                    notes.append(note)


                    print("New note added: ", str(note))
                except IndexError:
                    note = Note(row[0], round(float(row[1]), 1), 0.5,1000,False) # note name, note length
                    notes.append(note)
                    print("New note added: ", str(note))

        instPer.append(MusicPerInst(notes, inst, key))
        print("list was appended")
        song = Song(title, instPer, sig, 0)

        return song

    print("Error: Exited with statement early #fileToSong")
    return None
