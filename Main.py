import sys

import Songbook
from Utils import MusicUtils
from Utils import FileUtils
from Gui import Button
from Gui import Gui


def main():
    songs = []
    fileNames = ["test.csv","DemonsIG.csv","FurElise.csv"]
    load(songs, fileNames)
    MusicUtils.init()


    #Button.newMethod()
    try:
        Gui.newMethod(songs)
    except:
        sys.exit()

def load(songs, fileNames):
    """
    Loads all the songs from the list into the song book
    :param songs:
    :param fileNames:
    :return:
    """
    for fileName in fileNames:
        Songbook.songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type

    return


if __name__ == "__main__":
    main()
