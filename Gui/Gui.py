import sys
import pygame
from Gui import Button
from Play import Play
from Utils import FileUtils
from Utils import MusicUtils


def newMethod(self, songs=0):
    """
    This method sets up the Gui for the music player program.
    :return:
    """
    pygame.init()
    newSurface = pygame.display.set_mode((600, 600))
    newSurface.fill("black")
    width = newSurface.get_width()
    height = newSurface.get_height()

    buttonList = []
    pauseButton(buttonList, newSurface)
    resumeButton(buttonList, newSurface)
    playAllButton(buttonList, newSurface)
    stopButton(buttonList, newSurface)
    addTestToQueueButton(buttonList, newSurface)
    playTestButton(buttonList, newSurface)

    noteListWhite = ["A1", "A3", "A4", "A5", "A6"]
    noteListBlack = ["A1#", "A2#", "A4#", "A5#", "A6#"]

    x = 200
    y = 500
    for note in noteListWhite:
        playPianoKeyButton(buttonList, newSurface, 0, 0, 0, "white", note, x, y)
        x += 25

    for note in noteListBlack:
        playPianoKeyButton(buttonList, newSurface, 240, 255, 255, "black", note, x, y)
        x += 25

    quitProgramButton(buttonList, newSurface)

    while True:
        for moment in pygame.event.get():
            if moment.type == pygame.QUIT:
                pygame.quit()
            if moment.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                for button in buttonList:
                    if isHovering(button, mouse):
                        clickButton(newSurface, button, buttonList)
                        print("clicked")

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
    buttonList.append(Button.Button(newSurface, 0, 80, 170, "white", 100, 150,
                                    100, 150, 20, "PlayAll"))


def playAllButtonClick():
    """
    Calls playAll() in Play.py when the button is clicked
    :return:
    """
    Play.playAll()


def pauseButton(buttonList, newSurface):
    """
    Create a pause button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 180, 30, 50, "white", 300, 0,
                                    100, 150, 20, "Pause"))


def pauseButtonClick():
    """
    Calls pause() in Play.py when the button is clicked
    :return:
    """
    Play.pause(Play)


def resumeButton(buttonList, newSurface):
    """
    Creates a play button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 0, 80, 170, "white", 100, 50,
                                    100, 150, 20, "Resume"))


def resumeButtonClick():
    """
    Calls play() in Play.py when the button is clicked
    :return:
    """
    Play.resume(Play)


def stopButton(buttonList, newSurface):
    """
    Creates a stop button and puts it on the screen
    :return:
    """
    buttonList.append(Button.Button(newSurface, 0, 80, 170, "red", 300, 150, 100, 150, 20, "stop"))


def stopButtonClick():
    """
    Calls stop() in Play.py when the button is click
    :return:
    """
    Play.stopMusic(Play)


def addTestToQueueButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 0, 80, 170, "white", 400, 150,
                                    100, 150, 20, "Add Test"))


def addTestToQueueButtonClick():
    Play.addToQueue(Play, "test.csv")


def playTestButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 0, 80, 170, "white", 400, 50,
                                    100, 150, 20, "Play Test"))


def playTestButtonClick():
    MusicUtils.playSong(FileUtils.fileToSong("a1.csv"))


def drawButton(newSurface, button, x=0):
    if button.getRed() + x > 255:
        # print("Red value > 255")
        x = 255 - button.getRed()
    pygame.draw.rect(newSurface, (button.getRed() + x, button.getGreen(), button.getBlue()),
                     [button.getXAxis(), button.getYAxis(), button.getButtonWidth(), button.getButtonHeight()])


def quitProgramButton(buttonList, newSurface):
    buttonList.append(Button.Button(newSurface, 0, 80, 100, "white", 300, 400,
                                    100, 150, 20, "quit program"))


def quitProgramButtonClick():
    print("Thanks for using the program!")
    exit()


def isHovering(button, mouse):
    return button.getXAxis() <= mouse[0] <= button.getXAxis() + button.getButtonWidth() \
           and button.getYAxis() <= mouse[1] <= button.getYAxis() + button.getButtonHeight()


def playPianoKeyButton(buttonList, newSurface, r, g, b, color, name, xPos, yPos, j=75, k=25, l=10):
    buttonList.append(Button.Button(newSurface, r, g, b, color, xPos, yPos,
                                    j, k, l, name))
    return


def playButtonClick(note):
    MusicUtils.playSong(FileUtils.fileToSong(note))
    pass


def clickButton(newSurface, button, buttonList):
    """
    This function checks which button to click on.
    :param newSurface: the surface that is being clicking in
    :param button: the button that is being click on
    :param buttonList: the list of buttons to check in
    :return:
    """
    if button == buttonList[0]:
        pauseButtonClick()
    elif button == buttonList[1]:
        resumeButtonClick()
    elif button == buttonList[2]:
        playAllButtonClick()
    elif button == buttonList[3]:
        stopButtonClick()
    elif button == buttonList[4]:
        addTestToQueueButtonClick()
    elif button == buttonList[5]:
        playTestButtonClick()
    elif button == buttonList[6]:
        playButtonClick("a1.csv")
    elif button == buttonList[7]:
        playButtonClick("a3.csv")
    elif button == buttonList[8]:
        playButtonClick("a4.csv")
    elif button == buttonList[9]:
        playButtonClick("a5.csv")
    elif button == buttonList[10]:
        playButtonClick("a6.csv")
    elif button == buttonList[11]:
        playButtonClick("a-1.csv")
    elif button == buttonList[12]:
        playButtonClick("a-2.csv")
    elif button == buttonList[13]:
        playButtonClick("a-4.csv")
    elif button == buttonList[14]:
        playButtonClick("a-5.csv")
    elif button == buttonList[15]:
        playButtonClick("a-6.csv")
    elif button == buttonList[16]:
        quitProgramButtonClick()
