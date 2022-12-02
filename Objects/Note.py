class Note:

    def __init__(self, name, length, volume=.50, fadeout=1000, pause=False):
        self.name = name
        self.length = length
        self.volume = volume
        self.fadeout = fadeout
        self.pause = pause
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

    def getFadeout(self):
        """
        Get the time a note takes to fade out
        :param fadeout:
        :return:
        """
        return self.fadeout
    def setFadeout(self, fadeout):
        """
        Set the time a note takes to fade out
        :return:
        """
        self.fadeout = fadeout

    def getVolume(self):
        """
        Get the volume of a note
        :param fadeout:
        :return:
        """
        return self.volume
    def setVolume(self, volume):
        """
        Set the volume of a note
        :return:
        """
        self.volume = volume

    def getPause(self):
        """
        Get if the note should pause the sound
        :return:
        """
        return self.pause
    def setPause(self, pause):
        """
        Set if the note should pause the music or not
        :return:
        """
        self.pause = pause

    def __str__(self):
        return "[\'" + str(self.getName()) + "\', \'" + str(self.getLength()) + "\']"
