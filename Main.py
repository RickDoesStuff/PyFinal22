from Utils import MusicUtils
from Utils import FileUtils


def main():
    songs = []
    fileNames = ["test.csv"]
    load(songs, fileNames)
    MusicUtils.init()

    print("\n\nPlaying\n\n")
    for musicPerInst in songs[0].getMusicPerInstList():
        for note in musicPerInst.getNotes():
            print(str(note))
            MusicUtils.playNote(note)


def load(songs, fileNames):
    for fileName in fileNames:
        songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type

    return


if __name__ == "__main__":
    main()
