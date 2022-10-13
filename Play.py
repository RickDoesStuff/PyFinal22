## Plays
import queue


class Play:
    queue = []  # the current queue
    nowPlaying = None  # the current playing song
    paused = True

    def __init__(self):
        pass

    def playAll(self):
        """
        This function plays all musics in the music list.
        """
        # WIP
        pass

    def shuffle(self):
        """
        Shuffle the current queue
        :return:
        """
        self.setQueue(self.getQueue().shuffle())

    def play(self, song):
        """
        play a specific song
        :return:
        """

        self.setNowPlaying(song)
        if self.isPaused():
            self.setPaused(False)
        return

    def stopMusic(self):
        """
        Stop the current song and end the queue
        :return:
        """
        self.nowPlaying = None
        self.setQueue(None)

    def getQueue(self):
        """
        get the current queue
        :return:
        """
        return self.queue

    def setQueue(self, queue):
        """
        overwrites the current queue with a new queue
        :param queue:
        :return:
        """
        self.queue = queue

    def removeFromQueue(self, indexToRemove):
        """
        Removes a song from the queue
        :param indexToRemove:
        :return:
        """
        tempQueue = self.getQueue() # copy the queue
        toReturn = tempQueue.pop(indexToRemove) # return the song removed from the queue
        self.setQueue(tempQueue) # set the queue
        return toReturn

    def addToQueue(self, songToAdd):
        """
        Add a song to the queue
        :param songToAdd:
        :return:
        """
        if self.getQueue() is not None: # I might not need this if statement, do testing with appending to a None list
            self.queue.append(songToAdd)
        else:
            self.queue = [songToAdd]

    def skipCurrent(self):
        """
        Skip the current song
        :return:
        """
        skippedSong = self.getNowPlaying()

        self.play(self.removeFromQueue(0)) # play the new song and remove it from the queue

        return skippedSong # ret the song skipped

    def isPaused(self):
        """
        Get if the queue is paused
        :return:
        """
        return self.paused

    def setPaused(self, paused):
        """
        Set if the queue is paused
        :param paused:
        :return:
        """
        self.paused = paused
