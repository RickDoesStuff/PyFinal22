import Songbook
from Utils import MusicUtils
from Utils import FileUtils
from Gui import Button
from Gui import Gui


def main():
    songs = []
    fileNames = ["test.csv"]
    load(songs, fileNames)
    MusicUtils.init()


    #Button.newMethod()
    Gui.newMethod(songs)

def load(songs, fileNames):
    for fileName in fileNames:
        Songbook.songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type

    return


if __name__ == "__main__":
    main()
