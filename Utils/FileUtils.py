import csv

from Objects.MusicPerInst import MusicPerInst
from Objects.Note import Note
from Objects.Song import Song


class FileUtils:
    def __init__(self):
        pass

    def fileToSong(self, fileName):
        """

        :param fileName:
        :return:
        """

        with open(fileName, newline="") as file:
            reader = csv.reader(file)
            notes = []
            title = None
            inst = None
            key = None
            sig = None
            for row in reader:
                if len(row) == 4:  # if a row in the file has 4 items, it's the header, and it should define everything
                    title = row[0]
                    inst = row[1]
                    key = row[2]
                    sig = row[3]
                    continue
                note = Note(row[0], row[1])
                notes.append(note)

            musicPerInst = MusicPerInst(notes, inst, key)
            song = Song(title, musicPerInst, sig, 0)
            # song.strPrint()
            return song
        print("Error: Exited with statement early #fileToSong")
        return None
