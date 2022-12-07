## Plays
import queue
import threading
import time
from Objects import Song
import Songbook
import Utils.MusicUtils
from Utils import GenUtils


class Play:
    queue = []  # the current queue
    nowPlaying = None  # the current playing song
    paused = False

    def __init__(self):
        pass

    def playAll(self, songList):
        """
        This function plays all musics in the songList.
        """
        self.setQueue(GenUtils.deepCopy(songList))
        self.skipCurrent()

        pass

    def shuffle(self):
        """
        Shuffle the current queue
        :return:
        """
        self.getQueue().shuffle()

    def play(self, song):
        """
        play a specific song & runs through the queue
        :return:
        """

        self.nowPlaying = song
        self.resume()
        Utils.MusicUtils.playSong(song, self)

        time.sleep(1)  # sleep for 1 second between songs

        print("Song that ended:", song.getTitle())

        if self.getQueue() is None:
            print("Queue is now empty!")

        elif len(self.getQueue()) > 0:
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

        if len(Songbook.threads) > 0:
            thread = Songbook.threads[0]

        return

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
        tempQueue = GenUtils.deepCopy(self.getQueue())  # copy the queue
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
#        newSong = Song.Song(self.nowPlaying.getTitle(), self.nowPlaying.getMusicPerInstList(),
#                            self.nowPlaying.getTimeSig(), self.nowPlaying.getCurrentPosition())
#        self.queue.insert(0, newSong)
        self.paused = True
        #this is not complete, and feel free to change it.



    def resume(self):
        """
        resume the song
        :return:
        """
        self.paused = False

    def getSong(self):
        """
        return the song
        :return: the current song
        """
        return self.nowPlaying
