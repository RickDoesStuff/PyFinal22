# Music Utils
import pygame as pg
import threading
import time as t


def init():
    pg.mixer.init()
    pg.init()
    pg.mixer.set_num_channels(12)  # amt of notes


def playSong(song):
    """
    Play the song out loud
    :param song: The song obj
    :return: nothing
    """

    return


def playNote(note):
    """
    Play the note out load for the correct length of the note
    :param note: The note object
    :return: nothing
    """
    #t.sleep(1)  # wait 1 second before playing the note

    print("note to be played:", str(note))
    pg.mixer.Sound("PianoNotes/" + str(note.getName()) + ".wav").play()

    t.sleep(note.getLength())

    print("note that played:", str(note))  # the note played

    return
