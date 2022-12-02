# Music Utils
import pygame as pg
import time as t
import threading

import Main
import Songbook


def init():
    pg.mixer.init()
    pg.init()
    pg.mixer.set_num_channels(50)  # amt of notes


def playSong(song, play):
    """
    Play the song out loud
    :param play: The play obj
    :param song: The song obj
    :return: nothing
    """
    print("\n\nPlaying\n\n")

    for musicPerInst in song.getMusicPerInstList():
        for note in musicPerInst.getNotes():
            print(str(note))
            if play.isPaused():
                #print("***" + str(Songbook.threads))
                #Songbook.threads[0].join()
                #print("***" + str(Songbook.threads))
                return
            playNote(note)

    return


def playNote(note):
    """
    Play the note out load for the correct length of the note
    :param note: The note object
    :return: nothing
    """
    # t.sleep(1)  # wait 1 second before playing the note

    # print("note to be played:", str(note))
    pg.mixer.Sound("PianoNotes/" + str(note.getName()) + ".wav").play()

    t.sleep(note.getLength())

    # print("note that played:", str(note))  # the note played

    return
