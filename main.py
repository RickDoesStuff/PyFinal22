from Utils.FileUtils import FileUtils


class Main:
    def __init__(self):
        pass

    def load(self):
        return


def main():
    songs = []
    songs.append(FileUtils.fileToSong("test.csv", "test.csv"))  # testing the file utils
    print(str(songs[0]))
    songs[0].strPrint()


if __name__ == "__main__":
    main()
