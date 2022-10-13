import csv

from Objects.Note import Note


class FileUtils:
    def __init__(self):
        pass

    def fileToSong(self, fileName):
        """

        :param fileName:
        :return:
        """
        print("Here")

        with open(fileName, newline="") as file:
            reader = csv.reader(file)
            print("csv.reader(file): " + str(reader))
            print("\n rows: \n")
            notes=[]
            for row in reader:
                note = Note(row[0], row[1])
                notes.append(note)
        # return toReturn
