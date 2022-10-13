import csv


class FileUtils:
    def __init__(self):
        pass

    def readFile(self, fileName):
        """

        :param fileName:
        :return:
        """
        print("Here")
        with open(fileName, newline="") as file:
            reader = csv.reader(file)
            print("csv.reader(file): " + str(reader))
            print("\n rows: \n")
            for row in reader:
                print(row[0] + " (" + str(row[1]) + ")")
            print()
        print("Closed")