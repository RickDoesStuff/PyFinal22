class Song:

    def __init__(self, title, musicPerInstList, timeSig, currentPosition):
        self.title = title
        self.musicPerInstList = musicPerInstList
        self.timeSig = timeSig
        self.currentPosition = currentPosition

        pass

    def getTitle(self):
        """
        Get the title of the song
        :return:
        """
        return self.title

    def setTitle(self, title):
        """
        Set a new title for a song
        :param title:
        :return:
        """
        self.title = title

    def getMusicPerInstList(self):
        """

        :return:
        """
        return self.musicPerInstList

    def setMusicPerInstList(self, musicPerInstList):
        """

        :param musicPerInstList:
        :return:
        """
        self.musicPerInstList = musicPerInstList

    def addMusicPerInstList(self, musicPerInst):
        """
        Add an instrument to the song
        :param musicPerInst:
        :return:
        """

        instList = self.getMusicPerInstList()
        instList = instList.append(musicPerInst)
        self.setMusicPerInstList(instList)

    def delMusicPerInstList(self, instrumentIndex):
        pass  # WIP

    def getTimeSig(self):
        """

        :return:
        """
        return self.timeSig

    def setTimeSig(self, timeSig):
        """

        :param timeSig:
        :return:
        """
        self.timeSig = timeSig

    def getCurrentPosition(self):
        """

        :return:
        """
        return self.currentPosition

    def setCurrentPosition(self, currentPosition):
        """

        :param currentPosition:
        :return:
        """
        self.currentPosition = currentPosition

    def incPosition(self):
        """

        :return:
        """
        self.currentPosition += 1

    def __str__(self):
        return "[\"" + str(self.title) + "\", \"" + str(self.musicPerInstList) + "\", \"" + \
               str(self.timeSig) + "\", \"" + str(self.currentPosition) + "\"]"

    def strPrint(self):
        print("[\"" + str(self.title) + "\", \"" + str(self.timeSig) + "\", \"" + str(self.currentPosition) + "\"]")
        self.musicPerInstList.strPrint()
