import pygame

from Gui import Button
from Utils import FileUtils
from Utils import MusicUtils
class Gui:

    songs = []
    fileNames = ["test.csv"]
    MusicUtils.init()
    def load(songs, fileNames):
        """
        this method loads a song list
        :param fileNames:
        :return:
        """

        for fileName in fileNames:
            songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type
        return
    load(songs, fileNames)

    def newMethod(songs):
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
        buttonList.append(Button.Button(songs, newSurface, 180, 30, 50, "white", 300, 0,
                                        100, 150, 20, "TEST SONG"))
        buttonList.append(Button.Button(songs, newSurface, 0, 80, 170, "white", 100, 50,
                                        100, 150, 20, "TEST SONG"))
        buttonList.append(Button.Button([FileUtils.fileToSong("a1.csv")], newSurface, 0, 80, 170, "white", 100, 150,
                                        100, 150, 20, "Play A1"))


        while True:
            for moment in pygame.event.get():
                if moment.type == pygame.QUIT:
                    pygame.quit()

                if moment.type == pygame.MOUSEBUTTONDOWN:
                    i = 0
                    for button in buttonList:
                        if button.getXAxis() <= mouse[0] <= button.getXAxis() + button.getButtonWidth() \
                                and button.getYAxis() <= mouse[1] <= button.getYAxis() + button.getButtonHeight():
                            print("\n\nPlaying\n\n")
                            for musicPerInst in button.getSongs()[0].getMusicPerInstList():
                                for note in musicPerInst.getNotes():
                                    print(str(note))
                                    MusicUtils.playNote(note)

                        print("hi")

            mouse = pygame.mouse.get_pos()

            for button in buttonList:
                if button.getXAxis() <= mouse[0] <= button.getXAxis()+button.getButtonWidth()\
                        and button.getYAxis() <= mouse[1] <= button.getYAxis()+button.getButtonHeight():
                    pygame.draw.rect(newSurface, (button.getRed()+60,button.getGreen(),button.getBlue()),
                        [button.getXAxis(),button.getYAxis(),button.getButtonWidth(), button.getButtonHeight()])

                else:
                    pygame.draw.rect(newSurface, (button.getRed(),button.getGreen(),button.getBlue()),
                        [button.getXAxis(),button.getYAxis(),button.getButtonWidth(), button.getButtonHeight()])

                buttonFont = pygame.font.SysFont("Serif", button.getFontSize())
                text = buttonFont.render(button.getButtonText(), True, button.getTextColor())
                newSurface.blit(text, ((button.getXAxis()+button.getButtonWidth()/2-
                                        (button.getFontSize()//2)*(len(button.getButtonText()))//2),
                                       button.getYAxis()+button.getButtonHeight()/2-button.getFontSize()//2))
            pygame.display.update()

    newMethod(songs)





