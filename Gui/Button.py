import pygame
from Utils import MusicUtils
from Utils import FileUtils
import PianoNotes
class Button:


#    def load(songs, fileNames):
#        for fileName in fileNames:
#            songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type
#        return

#    songs = []
#    fileNames = ["test.csv"]
#    load(songs, fileNames)
#    MusicUtils.init()
    def __init__(self, songs, newSurface, redShade=200, greenShade=30, blueShade=80,
                textColor="white", xAxis=200, yAxis=0, buttonHeight=50, buttonWidth=150, fontSize=20,
                buttonText="test"):

        self.yAxis = yAxis
        self.xAxis = xAxis
        self.newSurface = newSurface
        self.redShade = redShade
        self.blueShade = blueShade
        self.greenShade = greenShade
        self.buttonHeight = buttonHeight
        self.buttonWidth = buttonWidth
        self.textColor = textColor
        self.buttonText = buttonText
        self.fontSize = fontSize
        self.songs = songs
        
        #pygame.draw.rect(newSurface, (redShade,greenShade,blueShade), [xAxis, yAxis, buttonWidth, buttonHeight])
        #pygame.draw.rect(newSurface, (redShade + 60, blueShade, greenShade), [xAxis,
        #                 yAxis, buttonWidth, buttonHeight])



        backgroundColor = (redShade,greenShade,blueShade)
        pygame.init()
        newSurface = pygame.display.set_mode((600,600))
        newSurface.fill("black")
        width = newSurface.get_width()
        height = newSurface.get_height()
        buttonFont = pygame.font.SysFont("Serif", fontSize)
        text = buttonFont.render(buttonText, True, textColor)
        color = (redShade,blueShade,greenShade)
#        while True:
#            for moment in pygame.event.get():
#                if moment.type == pygame.QUIT:
#                    pygame.quit()
#
#                if moment.type == pygame.MOUSEBUTTONDOWN:
#                    if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+50:
#                        print("\n\nPlaying\n\n")
#                        for musicPerInst in songs[0].getMusicPerInstList():
#                            for note in musicPerInst.getNotes():
#                                print(str(note))
#                                MusicUtils.playNote(note)

#            mouse = pygame.mouse.get_pos()

#            if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+50:
#                pygame.draw.rect(newSurface,(redShade+60,blueShade,greenShade), [width/2,height/2,150,50])
#            else:
#                pygame.draw.rect(newSurface, color, [width/2, height/2, 150,50])
#            newSurface.blit(text, (width/2+10,height/2 +10))
#            pygame.display.update()

    def getXAxis(self):
        return self.xAxis

    def getYAxis(self):
        return self.yAxis

    def getRed(self):
        return self.redShade

    def getGreen(self):
        return self.greenShade

    def getBlue(self):
        return self.blueShade

    def getButtonWidth(self):
        return self.buttonWidth

    def getButtonHeight(self):
        return self.buttonHeight

    def getButtonText(self):
        return self.buttonText

    def getTextColor(self):
        return self.textColor

    def getFontSize(self):
        return self.fontSize

    def getSongs(self):
        return self.songs