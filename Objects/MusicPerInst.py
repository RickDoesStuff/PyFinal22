class MusicPerInst:

    def __init__(self, notes, instrument, key):
        self.notes = notes
        self.instrument = instrument
        self.key = key
        pass

    def getNotes(self):
        """
        Get the notes being played
        :return:
        """
        return self.notes

    def setNotes(self, notes):
        """
        Set the notes being played
        :param notes:
        :return:
        """
        self.notes = notes

    def getInstrument(self):
        """
        Get the instrument
        :return:
        """
        return self.instrument

    def setInstrument(self, instrument):
        """
        Set the instrument
        :param instrument:
        :return:
        """
        self.instrument = instrument

    def getKey(self):
        """
        Get the key of the instrument
        :return:
        """
        return self.key

    def setKey(self, key):
        """
        Set the key of the instrument
        :param key:
        :return:
        """
        self.key = key

    def __str__(self):
        return "[" + str(self.notes) + ", " + str(self.instrument) + ", " + str(self.key) + "]"

    def strPrint(self):
        print("[\"" + str(self.instrument) + "\", \"" + str(self.key) + "\"]")
        for note in self.notes:
            print(note)
