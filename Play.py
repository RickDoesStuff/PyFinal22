## Plays
import queue
import time

import Utils.MusicUtils


class Play:
    queue = []  # the current queue
    nowPlaying = None  # the current playing song
    paused = True

    def __init__(self):
        pass

    def playAll(self, songList):
        """
        This function plays all musics in the songList.
        """
        self.setQueue(songList)
        self.skipCurrent()

        pass

    def shuffle(self):
        """
        Shuffle the current queue
        :return:
        """
        self.setQueue(self.getQueue().shuffle())

    def play(self, song):
        """
        play a specific song & runs through the queue
        :return:
        """

        self.nowPlaying = song
        self.resume()
        Utils.MusicUtils.playSong(song)

        time.sleep(1)  # sleep for 1 second between songs

        print("Song that ended:", self.nowPlaying)

        if len(self.getQueue()) > 0:
            songToPlay = self.removeFromQueue(0)
            print("Now playing:", songToPlay)
            self.play(songToPlay)  # recursion
        else:
            print("Queue is now empty!")

        return

    def stopMusic(self):
        """
        Stop the current song and end the queue
        :return:
        """
        self.nowPlaying = None
        self.pause()
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
        tempQueue = self.getQueue()  # copy the queue
        toReturn = tempQueue.pop(indexToRemove)  # return the song removed from the queue
        self.setQueue(tempQueue)  # set the queue
        return toReturn

    def addToQueue(self, songToAdd):
        """
        Add a song to the queue
        :param songToAdd:
        :return:
        """
        self.queue.append(songToAdd)

    def skipCurrent(self):
        """
        Skip the current song
        :return:
        """
        skippedSong = self.nowPlaying
        self.play(self.removeFromQueue(0))  # play the new song and remove it from the queue

        return skippedSong  # ret the song skipped

    def isPaused(self):
        """
        Get if the queue is paused
        :return:
        """
        return self.paused

    def pause(self):
        """
        Pause the song
        :return:
        """
        self.paused = True

    def resume(self):
        """
        resume the song
        :return:
        """
        self.paused = False
