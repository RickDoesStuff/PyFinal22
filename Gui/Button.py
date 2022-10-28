import pygame
from Utils import MusicUtils
from Utils import FileUtils
import PianoNotes
class Button:


    def load(songs, fileNames):
        for fileName in fileNames:
            songs.append(FileUtils.fileToSong(fileName))  # Load all the files as the song type
        return

    songs = []
    fileNames = ["test.csv"]
    load(songs, fileNames)
    MusicUtils.init()

    def newMethod(songs):
        pygame.init()
        newSurface = pygame.display.set_mode((600,600))
        newSurface.fill("black")
        width = newSurface.get_width()
        height = newSurface.get_height()
        buttonFont = pygame.font.SysFont("Serif", 20)
        text = buttonFont.render("Play Test Music", True, "white")
        red = 100
        blue = 30
        green = 0
        color = (red,blue,green)
        while True:
            for moment in pygame.event.get():
                if moment.type == pygame.QUIT:
                    pygame.quit()

                if moment.type == pygame.MOUSEBUTTONDOWN:

                    if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+50:
                        print("\n\nPlaying\n\n")
                        for musicPerInst in songs[0].getMusicPerInstList():
                            for note in musicPerInst.getNotes():
                                print(str(note))
                                MusicUtils.playNote(note)

            mouse = pygame.mouse.get_pos()

            if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+50:
                pygame.draw.rect(newSurface,(red+60,blue,green), [width/2,height/2,150,50])
            else:
                pygame.draw.rect(newSurface, color, [width/2, height/2, 150,50])
            newSurface.blit(text, (width/2+10,height/2 +10))
            pygame.display.update()


    newMethod(songs)


