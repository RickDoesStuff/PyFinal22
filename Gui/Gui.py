import sys
import pygame
import pygame.key
import threading
import time

import Songbook
from Gui import Button
from Play import Play
from Utils import FileUtils
from Utils import MusicUtils

def newMethod(self, songs=0):
    """
    This method sets up the Gui for the music player program.
    :return:
    """
    play = Play()
    pygame.init()
    newSurface = pygame.display.set_mode((600, 600))
    newSurface.fill("black")
    width = newSurface.get_width()
    height = newSurface.get_height()

    buttonList = []
#    buttonList.append(Button.Button(newSurface, 100, 100, 100, "white", 190, 465,
#                                    120, 340, 20, ))
    pauseButton(buttonList, newSurface)
    resumeButton(buttonList, newSurface)
    playAllButton(buttonList, newSurface)
    stopButton(buttonList, newSurface)
    addTestToQueueButton(buttonList, newSurface)
    playTestButton(buttonList, newSurface)

#    noteListWhite = ["C3", "C-3", "D3", "D-3", "E3", "F3", "F-3", "G3", "G-3", "A3", "A-3", "B3", "C4"]
#    noteListBlack = []
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "C3", 200, 500)
    playPianoKeyButton(buttonList, newSurface, 60, 60, 60, "white", "C-3", 225, 475)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "D3", 250, 500)
    playPianoKeyButton(buttonList, newSurface, 60, 60, 60, "white", "D-3", 275, 475)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "E3", 300, 500)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "F3", 325, 500)
    playPianoKeyButton(buttonList, newSurface, 60, 60, 60, "white", "F-3", 350, 475)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "G3", 375, 500)
    playPianoKeyButton(buttonList, newSurface, 60, 60, 60, "white", "G-3", 400, 475)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "A3", 425, 500)
    playPianoKeyButton(buttonList, newSurface, 60, 60, 60, "white", "A-3", 450, 475)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "B3", 475, 500)
    playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", "C4", 500, 500)


#    x = 200
#    y = 500
#    for note in noteListWhite:
#        playPianoKeyButton(buttonList, newSurface, 0, 0, 0, "white", note, x, y)
#        x += 25

#    for note in noteListBlack:
#        playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", note, x, y)
#        x += 25
    quitProgramButton(buttonList, newSurface)

    playDemonsButton(buttonList, newSurface)
    playFurEliseButton(buttonList, newSurface)
    running = True
    while running is True:
        for moment in pygame.event.get():
            if moment.type == pygame.QUIT:
                running = False
                print("hi")
                sys.exit()
            if moment.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                for button in buttonList:
                    if isHovering(button, mouse):
                        thread = threading.Thread(target=clickButton, args=(newSurface, button, buttonList, play,))
                        #clickButton(newSurface, button, buttonList, play)
                        thread.start()
                        Songbook.threads.append(thread)
                        print("clicked")

            if pygame.key.get_pressed()[pygame.K_1]:
                playButtonClick("c3.csv", play)
            if pygame.key.get_pressed()[pygame.K_2]:
                playButtonClick("d3.csv", play)
            if pygame.key.get_pressed()[pygame.K_3]:
                playButtonClick("e3.csv", play)
            if pygame.key.get_pressed()[pygame.K_4]:
                playButtonClick("f3.csv", play)
            if pygame.key.get_pressed()[pygame.K_5]:
                playButtonClick("g3.csv", play)
            if pygame.key.get_pressed()[pygame.K_6]:
                playButtonClick("a3.csv", play)
            if pygame.key.get_pressed()[pygame.K_7]:
                playButtonClick("b3.csv", play)
            if pygame.key.get_pressed()[pygame.K_8]:
                playButtonClick("c4.csv", play)
            if pygame.key.get_pressed()[pygame.K_q]:
                playButtonClick("c-3.csv", play)
            if pygame.key.get_pressed()[pygame.K_w]:
                playButtonClick("d-3.csv", play)
            if pygame.key.get_pressed()[pygame.K_r]:
                playButtonClick("f-3.csv", play)
            if pygame.key.get_pressed()[pygame.K_t]:
                playButtonClick("g-3.csv", play)
            if pygame.key.get_pressed()[pygame.K_y]:
                playButtonClick("a-3.csv", play)

        mouse = pygame.mouse.get_pos()
        for button in buttonList:  ##highlights buttons that are hovered over
            if isHovering(button, mouse):  # checks if mouse is hovering over button
                drawButton(newSurface, button, 60)  # highlights box
            else:
                drawButton(newSurface, button)  # keeps box same color

            buttonFont = pygame.font.SysFont("Serif", button.getFontSize())
            text = buttonFont.render(button.getButtonText(), True, button.getTextColor())
            newSurface.blit(text, ((button.getXAxis() + button.getButtonWidth() / 2 -  ##adds text
                                    (button.getFontSize() // 2) * (len(button.getButtonText())) // 2),
                                   button.getYAxis() + button.getButtonHeight() / 2 - button.getFontSize() // 2))
        pygame.display.update()


def playAllButton(buttonList, newSurface):
    """
    Creates a resume button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 0, 80, 170, "white", 50, 150,
                                    100, 150, 20, "PlayAll"))


def playAllButtonClick(play):
    """
    Calls playAll() in Play.py when the button is clicked
    :return:
    """
    play.playAll(Songbook.songs)


def pauseButton(buttonList, newSurface):
    """
    Create a pause button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 180, 30, 50, "white", 225, 10,
                                    100, 150, 20, "Pause"))


def pauseButtonClick(play):
    """
    Calls pause() in Play.py when the button is clicked
    :return:
    """
    play.pause()


def resumeButton(buttonList, newSurface):
    """
    Creates a play button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 0, 170, 40, "white", 50, 10,
                                    100, 150, 20, "Resume"))


def resumeButtonClick(play):
    """
    Calls play() in Play.py when the button is clicked
    :return:
    """
    #play.play(play.getSong())
    play.resume()


def stopButton(buttonList, newSurface):
    """
    Creates a stop button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 180, 30, 50, "white", 225, 150, 100, 150, 20, "Stop"))


def stopButtonClick(play):
    """
    Calls stop() in Play.py when the button is click
    :return:
    """
    play.stopMusic()


def addTestToQueueButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 170, 80, 170, "white", 400, 10,
                                    0, 0, 0, ""))


def addTestToQueueButtonClick(play):
    play.addToQueue("test.csv", play)


def playTestButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 170, 80, 170, "white", 50, 290,
                                    100, 150, 20, "Play Test"))


def playTestButtonClick(play):
    play.play(FileUtils.fileToSong("test.csv"))

def playDemonsButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 170, 80, 170, "white", 50, 500,
                                    100, 150, 20, "Demons by IG"))

def playFurEliseButtonClick(plays):

    plays.play(FileUtils.fileToSong("FurElise.csv"))

def playFurEliseButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 170, 80, 170, "white", 400, 10,
                                    100, 150, 20, "Fur Elise"))

def playDemonsButtonClick(plays):

    plays.play(FileUtils.fileToSong("DemonsIG.csv"))

def drawButton(newSurface, button, x=0):
    if button.getRed() + x > 255:
        # print("Red value > 255")
        x = 255 - button.getRed()
    pygame.draw.rect(newSurface, (button.getRed() + x, button.getGreen(), button.getBlue()),
                     [button.getXAxis(), button.getYAxis(), button.getButtonWidth(), button.getButtonHeight()])


def quitProgramButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 100, 0, 0, "white", 225, 290,
                                    100, 150, 20, "Quit Program"))


def quitProgramButtonClick():
    threading.Thread = threading.main_thread()
    pygame.event = pygame.event.get(pygame.QUIT)
    #pygame.event = pygame.event.get(pygame.QUIT)
    #print("Thanks for using the program!")
    #pygame.event = pygame.event.get(pygame.QUIT)
    #exit()
    #print("hi")






def isHovering(button, mouse):
    return button.getXAxis() <= mouse[0] <= button.getXAxis() + button.getButtonWidth() \
           and button.getYAxis() <= mouse[1] <= button.getYAxis() + button.getButtonHeight()


def playPianoKeyButton(buttonList, newSurface, r, g, b, color, name, xPos, yPos, j=75, k=25, l=10):
    buttonList.append(Button.Button(newSurface, r, g, b, color, xPos, yPos,
                                    j, k, l, name))
    return


def playButtonClick(note, play):

    MusicUtils.playSong(FileUtils.fileToSong(note), play)
    pygame.mixer.fadeout(1500)

    pass


def clickButton(newSurface, button, buttonList, play):
    """
    This function checks which button to was clicked on.
    :param newSurface: the surface that is being clicking in
    :param button: the button that is being click on
    :param buttonList: the list of buttons to check in
    :return:
    """

    if button == buttonList[0]:
        pauseButtonClick(play)
    elif button == buttonList[1]:
        resumeButtonClick(play)
    elif button == buttonList[2]:
        playAllButtonClick(play)
    elif button == buttonList[3]:
        stopButtonClick(play)
    elif button == buttonList[4]:
        addTestToQueueButtonClick(play)
    elif button == buttonList[5]:
        playTestButtonClick(play)
    elif button == buttonList[6]:
        playButtonClick("c3.csv", play)
    elif button == buttonList[7]:
        playButtonClick("c-3.csv", play)
    elif button == buttonList[8]:
        playButtonClick("d3.csv", play)
    elif button == buttonList[9]:
        playButtonClick("d-3.csv", play)
    elif button == buttonList[10]:
        playButtonClick("e3.csv", play)
    elif button == buttonList[11]:
        playButtonClick("f3.csv", play)
    elif button == buttonList[12]:
        playButtonClick("f-3.csv", play)
    elif button == buttonList[13]:
        playButtonClick("g3.csv", play)
    elif button == buttonList[14]:
        playButtonClick("g-3.csv", play)
    elif button == buttonList[15]:
        playButtonClick("a3.csv", play)
    elif button == buttonList[16]:
        playButtonClick("a-3.csv", play)
    elif button == buttonList[17]:
        playButtonClick("b3.csv", play)
    elif button == buttonList[18]:
        playButtonClick("c4.csv", play)
    elif button == buttonList[19]:
        quitProgramButtonClick()
    elif button == buttonList[20]:
        playDemonsButtonClick(play)
    elif button == buttonList[21]:
        playFurEliseButtonClick(play)

