## Plays
import queue


class Play:

    queue = [] # the current queue
    nowPlaying = None # the current playing song
    def __init__(self):
        pass

    def playAll(self):
        """
        This function plays all musics in the music list.
        """
        return

    def shuffle(self):
        """
        This function calls getQueue() then convert getQueue() into a list, then shuffles the list,
        then sets the queue into a list
        :return:
        """

        return

    def play(self):
        """
        play a specific song
        :return:
        """
        return

    def pauseMusic(self):
        """
        pause the song and queue
        :return:
        """
        return

    def stopMusic(self):
        """
        Stop the current song and end the queue
        :return:
        """
        for song in queue:
            queue.pop()



    def getQueue(self):
        """
        get the current queue
        :return:
        """
        return self.queue

    def setQueue(self, newQueue):
        """
        overwrites the current queue with a new queue
        :param queue:
        :return:
        """
        # check if newQueue is a valid list of songs

        queue=newQueue

    def removeFromQueue(self, indexToRemove):
        """
        Removes a song from the queue
        :param indexToRemove:
        :return:
        """

        if indexToRemove < len(queue) and indexToRemove >= 0:
            return queue.pop(indexToRemove)
        print("removeFromQueue error")
        return None

    def addToQueue(self, songToAdd):
        """
        Add a song to the queue
        :param songToAdd:
        :return:
        """
        # check if songToAdd is a valid song type

        queue.append(songToAdd)

    def skipQueue(self):
        """
        Skip the current song
        :return:
        """
        return skippedSong