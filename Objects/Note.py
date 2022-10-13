class Note:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        pass

    def getName(self):
        """
        Get the name of a note
        :return:
        """
        return self.name

    def setName(self, name):
        """
        Set the name of a note
        :param name:
        :return:
        """
        self.name = name

    def getLength(self):
        """
        Get the length of a note
        :return:
        """
        return self.length

    def setLength(self, length):
        """
        Set the new length of a note
        :param length:
        :return:
        """
        self.length = length
