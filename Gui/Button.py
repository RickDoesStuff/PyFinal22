import pygame

class Button:


    def __init__(self, newSurface, redShade=200, greenShade=30, blueShade=80,
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


        backgroundColor = (redShade,greenShade,blueShade)
        pygame.init()
        newSurface = pygame.display.set_mode((600,600))
        newSurface.fill("black")
        width = newSurface.get_width()
        height = newSurface.get_height()
        buttonFont = pygame.font.SysFont("Serif", int(fontSize))
        text = buttonFont.render(buttonText, True, textColor)
        color = (redShade,blueShade,greenShade)

    def getXAxis(self):
        """
        This method returns the xAxis from the constructor
        :return:
        xAxis from constructor
        """
        return self.xAxis

    def getYAxis(self):
        """
        This method returns the yAxis from the constructor
        :return:
        yAxis from constructor
        """
        return self.yAxis

    def getRed(self):
        """
        This method returns the shade of red from the constructor
        :return:
        redShade from constructor
        """
        return self.redShade

    def getGreen(self):
        """
        This method returns the shade of green from the constructor
        :return:
        greenShade from constructor
        """
        return self.greenShade

    def getBlue(self):
        """
        This method returns the shade of blue from the constructor
        :return:
        blueShade from constructor
        """
        return self.blueShade

    def getButtonWidth(self):
        """
        This method returns the buttonWidth from the constructor
        :return:
        buttonWidth from constructor
        """
        return self.buttonWidth

    def getButtonHeight(self):
        """
        This method returns the buttonHeight from the constructor
        :return:
        buttonHeight from constructor
        """
        return self.buttonHeight

    def getButtonText(self):
        """
        This method returns the text in a button from the constructor
        :return:
        buttonText from constructor
        """
        return self.buttonText

    def getTextColor(self):
        """
        This method returns the color of text of the button from the constructor
        :return:
        textColor from constructor
        """
        return self.textColor

    def getFontSize(self):
        """
        This method returns the fontSize of text in a button from the constructor
        :return:
        fontSize from constructor
        """
        return self.fontSize

    #def getSongs(self):
        """
        This method returns the song list from the constructor
        :return:
        songs from constructor
        """
    #    return self.songs