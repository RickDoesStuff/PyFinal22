from Utils.FileUtils import fileToSong


def main():
    songs = []
    fileNames = ["test.csv"]
    load(songs, fileNames)
    print(str(songs[0]))
    songs[0].strPrint()


def load(songs, fileNames):
    for fileName in fileNames:
        songs.append(fileToSong(fileName))  # Load all the files as the song type

    return


if __name__ == "__main__":
    main()

