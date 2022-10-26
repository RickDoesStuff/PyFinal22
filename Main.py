from Utils import MusicUtils
from Utils import FileUtils

def main():
    songs = []
    fileNames = ["test.csv"]
    load(songs, fileNames)
    MusicUtils.init()
    #print(str(songs[0]))
    #songs[0].strPrint()
    """
    song = songs[0]
    print(str(song))
    song.strPrint()
    print("======")
    for i in song.getMusicPerInstList():
        print(str(i))

    print("\n\n songs")
    song1 = songs[0]
    song1.strPrint()
    print("\n\n musicPer")
    musicPerInstList = song1.getMusicPerInstList()
    musicPerInst = musicPerInstList[0]
    musicPerInst.strPrint()
    print("\n\n notes")
    notes = musicPerInst.getNotes()
    print(notes)
    """
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

