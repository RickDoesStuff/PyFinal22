import csv

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
            if isinstance(row[0], str) and isinstance(row[1], str):  # it is either a header or new instrument
                if "/" in row[1]:  # it is a header bc it contains time sig
                    title = row[0]
                    sig = row[1]
                else:
                    if key is not None:  # if there are no keys skip this part, that means we are not at the start
                        instPer.append(MusicPerInst(notes, inst, key))  # only do this if we are not at start
                        notes = []
                    # always going to run this part if it's a new instrument
                    inst = row[0]
                    key = row[1]
            else:  # it's not a header or new instrument
                note = Note(row[0], row[1])
                notes.append(note)

        song = Song(title, instPer, sig, 0)

        return song
    print("Error: Exited with statement early #fileToSong")
    return None
