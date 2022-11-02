from inspect import getmembers

import pygame
import time
from Gui import Button
from Utils import FileUtils
from Utils import MusicUtils
import PianoNotes
class Gui:

    songs = []
    fileNames = ["test.csv"]
    MusicUtils.init()
    def load(songs, fileNames):
        for fileName in fileNames:
            songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type
        return
    load(songs, fileNames)

#    def draw(self):
#        self.screen.fill(self.color)  # clear screen

#        self.Gui.draw(self.screen)


    def newMethod(songs):


        pygame.init()
        newSurface = pygame.display.set_mode((600, 600))
        newSurface.fill("black")
        width = newSurface.get_width()
        height = newSurface.get_height()

        buttonList = []
        buttonList.append(Button.Button(songs, newSurface, 180, 30, 50, "blue", 300, 0,
                                        100, 150, 20, "TEST"))
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

                        if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+50:
                            print("\n\nPlaying\n\n")
                            for musicPerInst in songs[0].getMusicPerInstList():
                                for note in musicPerInst.getNotes():
                                    print(str(note))
                                    MusicUtils.playNote(note)

            mouse = pygame.mouse.get_pos()

            for button in buttonList:
                if button.getXAxis() <= mouse[0] <= button.getXAxis()+button.getButtonWidth()\
                        and button.getYAxis() <= mouse[1] <= button.getYAxis()+button.getButtonHeight():
                    pygame.draw.rect(newSurface, (button.getRed()+60,button.getGreen(),button.getBlue()),
                        [button.getXAxis(),button.getYAxis(),button.getButtonWidth(), button.getButtonHeight()])
       #         if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+50:
       #             pygame.draw.rect(newSurface,(red+60,blue,green), [width/2,height/2,150,50])
                else:
                    pygame.draw.rect(newSurface, (button.getRed(),button.getGreen(),button.getBlue()),
                        [button.getXAxis(),button.getYAxis(),button.getButtonWidth(), button.getButtonHeight()])
    #             pygame.draw.rect(newSurface, color, [width/2, height/2, 150,50])
                buttonFont = pygame.font.SysFont("Serif", button.getFontSize())
                text = buttonFont.render(button.getButtonText(), True, button.getTextColor())
                newSurface.blit(text, (button.getXAxis()+button.getButtonWidth()/2,
                                       button.getYAxis()+button.getButtonHeight()/2))
            pygame.display.update()
#        while running:
#            for moment in pygame.event.get():
#                temp+=1
#                newSurface.fill("black")
#                Button.Button()

#                firstRect = pygame.Rect(temp,temp,temp,temp)
#                pygame.draw.rect(newSurface, "white", firstRect)
#                pygame.display.flip()
#                if moment.type == pygame.QUIT:
#                    running = False

    newMethod(songs)

    #




