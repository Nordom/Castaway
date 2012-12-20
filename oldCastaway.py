"""
    Castaway.py
"""

import pygame,sys, random
pygame.init()
pygame.mixer.init()

HEALTH = "Good"
FOOD = 0
WOOD = 0
STONE = 0


class Dhistlbl(pygame.sprite.Sprite):    #dhistlbl = Day history label
    """ Is the daily history. This label accepts a list of strings,
        creates a multi-line label to display text same properties
        as Day, Weather, and Health labels. It is 77 characters wide.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.textLines = [
            #123456789|123456789|123456789|123456789|123456789|123456789|1234567", #Used a guide for max text lines
            "You feel tired from spending yesterday's morning hacking away at",
            "trees with your STONE AXE. You managed to collect 3 LOGS and",
            "15 KINDLING.",
            "After finding 3 plant seeds, in the afternoon, from a plant that",
            "somewhat resemembles wheat on the far side of the island you feel",
            "pretty excited.",
            "You gather some strenght resting in the evening."
            "",
            "", # leave bank for the comLabel to center on
            ]
        self.font = pygame.font.Font("goodfoot.ttf", 24 ) #24 is the font size
        self.fgColor = ((0x00, 0x00, 0x00))#Black
        self.bgColor = ((0xFF, 0xF1,0x93)) #(0xFF, 0xF1,0x93) is the paper color
        self.ySize = len(self.textLines) * 24
        self.size = (631, self.ySize) #Width is 631, 1 is to fit the last font block completely
        self.topleft = (70, 140)
        self.bottom = (140 + self.ySize)
        self.invs = False
        
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        numLines = len(self.textLines)
        vSize = self.image.get_height() / numLines
        
        for lineNum in range(numLines):
            currentLine = self.textLines[lineNum]
            fontSurface = self.font.render(currentLine, True, self.fgColor, self.bgColor)
            xPos = 0
            yPos = lineNum * 25
            self.image.blit(fontSurface, (xPos, yPos))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft

        #Makes lable invisable when True
        if self.invs == False:
           self.fgColor = ((0x00, 0x00, 0x00))
        else:      #makes the button invisble when self.invs = True 
            self.fgColor = ((0xFF, 0xF1,0x93))

class Daylabel(pygame.sprite.Sprite):
    """ a basic label that displays the day number. 
        properties: 
        font: font to use
        text: text to display
        fgColor: foreground color
        bgColor: background color
        center: position of label's center
        size: (width, height) of label
        invs: Hides the label when set to True
    """
    def __init__(self, nextdayupdate):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("goodfoot.ttf", random.randint(50,60)) #randoms a font size between 50 - 60 to give it more of a hand written effect
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (140, 100)
        self.size = (190, 80)
        self.invs = False

    def update(self):
        self.text = "Day %d" %(nextdayupdate.day)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text, set xPos to 0 to left aline
        xPos = (self.image.get_width() - fontSurface.get_width())/2
               
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

        #Makes lable invisable when True
        if self.invs == False:
           self.fgColor = ((0x00, 0x00, 0x00))
        else:      #makes the button invisble when self.invs = True 
            self.fgColor = ((0xFF, 0xF1,0x93))

class Healthlabel(pygame.sprite.Sprite):
    """ a basic label that displays the status of the players health
        properties: 
        font: font to use
        text: text to display
        fgColor: foreground color
        bgColor: background color
        center: position of label's center
        size: (width, height) of label
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("goodfoot.ttf", random.randint(50, 60)) #randoms a font size between 50 - 60 to give it more of a hand written effect
        self.text = "Health: %s" %(HEALTH)
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (395, 100)
        self.size = (320, 80)
        self.invs = False

    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text, set xPos to 0 to left aline
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

        #Makes lable invisable when True
        if self.invs == False:
           self.fgColor = ((0x00, 0x00, 0x00))
        else:      #makes the button invisble when self.invs = True 
            self.fgColor = ((0xFF, 0xF1,0x93))

class Weatherlabel(pygame.sprite.Sprite):
    """ a basic label that displays the current days weather information
        properties: 
        font: font to use
        text: text to display
        fgColor: foreground color
        bgColor: background color
        center: position of label's center
        size: (width, height) of label
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("goodfoot.ttf", random.randint(50,60)) #randoms a font size between 50 - 60 to give it more of a hand written effect 
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (630, 100)
        self.size = (180, 80)
        self.invs = False

    def update(self):
        self.text = "%s" %(nextdayupdate.weather)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text, set xPos to 0 to left aline
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

        #Makes lable invisable when True
        if self.invs == False:
           self.fgColor = ((0x00, 0x00, 0x00))
        else:      #makes the button invisble when self.invs = True 
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class Comlabel(pygame.sprite.Sprite):
    #Comlabel = Command label
    """ a basic label displays current comand functions:

        #What would you like to do today?
        #You have:  (it displays your current inventory)

        properties: 
        font: font to use
        text: text to display
        fgColor: foreground color
        bgColor: background color
        center: position of label's center
        size: (width, height) of label
    """
    def __init__(self, dhistlbl):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.textToday = [
            "What will you do today?",
            "", # Leave bank for buttons to line up this line
            ]
            
        self.textInventory = [
            "You have:",
            "   Food = %d" %(FOOD),
            "   Wood = %d" %(WOOD),
            "   Stone = %d" %(STONE),
            "", # Leave bank for buttons to line up this line
            ]
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))#(0xFF, 0xF1,0x93) is the paper color
        self.ySize = len(self.textToday) * 24
        self.size = (600, self.ySize)
        self.topleft = (70, dhistlbl.bottom)
        self.bottom = (dhistlbl.bottom + self.ySize)

        self.invs = False
        self.today = True
        self.inventory = False

    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        numLinesToday = len(self.textToday)
        numLinesInventory = len(self.textInventory)
        vSize = self.image.get_height() / numLinesInventory
 
        if self.today == True: #displays today's text
            self.ySize = len(self.textToday) * 24
            self.size = (600, self.ySize)
            self.topleft = (70, dhistlbl.bottom)
            self.bottom = (dhistlbl.bottom + self.ySize)
            for lineNum in range(numLinesToday):
                currentLine = self.textToday[lineNum]
                fontSurface = self.font.render(currentLine, True, self.fgColor, self.bgColor)
                xPos = 0
                yPos = lineNum * 25
                self.image.blit(fontSurface, (xPos, yPos))
                
        elif self.inventory == True: #displays inventory text
            self.ySize = len(self.textInventory) * 24
            self.size = (600, self.ySize)
            self.topleft = (70, dhistlbl.bottom)
            self.bottom = (dhistlbl.bottom + self.ySize)
            for lineNum in range(numLinesInventory):
                currentLine = self.textInventory[lineNum]
                fontSurface = self.font.render(currentLine, True, self.fgColor, self.bgColor)
                xPos = 0
                yPos = lineNum * 25
                self.image.blit(fontSurface, (xPos, yPos))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft

        #Makes lable invisable when True
        if self.invs == False:
           self.fgColor = ((0x00, 0x00, 0x00))
        else:      #makes the button invisble when self.invs = True 
            self.fgColor = ((0xFF, 0xF1,0x93))

class Paper(pygame.sprite.Sprite):
    def __init__(self, background):
        pygame.sprite.Sprite.__init__(self)
        self.background = background

        self.STILL = 0
        self.MOVING = 1

        self.loadImages()
        self.image = self.paperStill
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        self.frame = 0
        self.delay = 4
        self.pause = 0
        self.state = self.STILL
       
    def update(self):
        #nextdayupdate.nextDay = False #makes sure the turn does not advance while the animation loops
        
        if self.state == self.STILL:
            self.image = self.paperStill
        else:
            #clears the screen while the pages change
            daylabel.invs = True
            weatherlabel.invs = True
            healthlabel.invs = True
            dhistlbl.invs = True
            comlabel.invs = True
            gatherbutton.invs = True
            harvbutton.invs = True
            searchbutton.invs = True
            buildbutton.invs = True
            checkbutton.invs = True
            nextdaybutton.invs = True
            
            self.pause += 1
            if self.pause >= self.delay:
            #reset pause and advance the animation
                self.pause = 0
                self.frame += 1
                
                if self.frame >= len(self.paperImages):
                    self.frame = 0
                    self.state = self.STILL
                    self.image = self.paperStill

                    #draws the text back on the screen after the pages have turned
                    daylabel.invs = False
                    weatherlabel.invs = False
                    healthlabel.invs = False
                    dhistlbl.invs = False
                    comlabel.invs = False
                    gatherbutton.invs = False
                    harvbutton.invs = False
                    searchbutton.invs = False
                    buildbutton.invs = False
                    checkbutton.invs = False
                    nextdaybutton.invs = False

                if self.frame == (len(self.paperImages) - 1):
                    nextdayupdate.nextDay = True #advances the day/turn by one on the last frame of animation
            
                else:
                    self.image = self.paperImages[self.frame]


    def loadImages(self):
        self.paperStill = pygame.image.load('CastawayImages/Castaway - paperanimation 014.gif')
        self.paperStill = self.paperStill.convert()
        transColor = self.paperStill.get_at((1,1))
        self.paperStill.set_colorkey(transColor)

        self.paperImages = []
        for i in range(1,15):
            imgName = 'CastawayImages/Castaway - paperanimation 0%d.gif' % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1,1))
            tmpImage.set_colorkey(transColor)
            self.paperImages.append(tmpImage)

class Gatherbutton(pygame.sprite.Sprite):
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, comlabel):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Gather"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.size = (100, 30)
        self.center = (125, comlabel.bottom)
        self.bottom = (comlabel.bottom + 10) #+30 from adding y size of the surface to get the bottom
        self.active = False
        self.clicked = False
        self.invs = False
            
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text, set xPos to 0 to left aline.
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
        
        #if not invs, button can receive input, 
        if self.invs == False:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        else:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))

class GathFbutton(pygame.sprite.Sprite):
    #GathFbutton = Gather food button
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, gatherbutton):
        pygame.sprite.Sprite.__init__(self)
        self.top = gatherbutton.bottom
        self.topleft = (75, self.top)
        self.bottom = (gatherbutton.bottom + 30)
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Food"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
        self.food = 0
            
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2

        self.gather = gatherbutton.clicked
        self.gathinvs = gatherbutton.invs #value for it gather button is invisible

        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
        
        if self.gather == False or self.gathinvs == True:
            self.invs = True
        elif self.gather == True or self.gathinvs == False:
            self.invs = False
        #if not invs, button can receive input, 
        if self.invs == False:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        if self.invs == True:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class GathWbutton(pygame.sprite.Sprite):
    #GathWbutton = Gather wood button
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, gatherbutton, gathfbutton):
        pygame.sprite.Sprite.__init__(self)
        self.top = gathfbutton.bottom
        self.topleft = (75, self.top)
        self.bottom = (gathfbutton.bottom + 30)
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Wood"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
        self.wood = 0
        
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2

        self.gather = gatherbutton.clicked
        self.gathinvs = gatherbutton.invs #value for it gather button is invisible
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
        
        if self.gather == False or self.gathinvs == True:
            self.invs = True
        elif self.gather == True or self.gathinvs == False:
            self.invs = False
        #if not invs, button can receive input, 
        if self.invs == False:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        if self.invs == True:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class GathSbutton(pygame.sprite.Sprite):
    #GathSbutton = Gather stone button
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, gatherbutton, gathwbutton):
        pygame.sprite.Sprite.__init__(self)
        self.top = gathwbutton.bottom
        self.topleft = (75, self.top)
        self.bottom = gathwbutton.bottom + 30
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Stone"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
        self.stone = 0
        
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2

        self.gather = gatherbutton.clicked
        self.gathinvs = gatherbutton.invs #value for it gather button is invisible
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
        
        if self.gather == False or self.gathinvs == True:
            self.invs = True
        elif self.gather == True or self.gathinvs == False:
            self.invs = False
        #if not invs, button can receive input, 
        if self.invs == False:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        if self.invs == True:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class Harvbutton(pygame.sprite.Sprite):
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, comlabel):
        pygame.sprite.Sprite.__init__(self)
        self.top = comlabel.bottom
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Harvest"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (225, self.top)
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
                    
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
        
        #if not invs, button can receive input, 
        if self.invs != True:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        else:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class Buildbutton(pygame.sprite.Sprite):
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, comlabel):
        pygame.sprite.Sprite.__init__(self)
        self.top = comlabel.bottom
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Build"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (325, self.top)
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
            
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
        
        #if not invs, button can receive input, 
        if self.invs != True:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        else:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class Searchbutton(pygame.sprite.Sprite):
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, comlabel):
        pygame.sprite.Sprite.__init__(self)
        self.top = comlabel.bottom
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Search"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (425, self.top)
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
            
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
        
        #if not invs, button can receive input, 
        if self.invs != True:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:
                self.fgColor = ((0xFF, 0x00, 0x00))
            else:
                self.fgColor = ((0x00, 0x00, 0x00))

        else:      #makes the button invisble when self.invs = True and Check gear is clicked
            self.fgColor = ((0xFF, 0xF1,0x93))
            
class Checkbutton(pygame.sprite.Sprite):
    """ a button based on the label 
        same properties as label +
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, comlabel):
        pygame.sprite.Sprite.__init__(self)
        self.top = comlabel.bottom
        self.font = pygame.font.Font("goodfoot.ttf", 24)
        self.text = "Check gear"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (100, 480)
        self.size = (100, 30)
        self.active = False
        self.clicked = False
        self.invs = False
            
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
        
        #if not invs, button can receive input, 
        if self.invs != True:
            self.fgColor = ((0x00, 0x00, 0x00))
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        
            if self.clicked == True:                # turns off Gather, Harvest, Build, Search, Buttons
                self.fgColor = ((0xFF, 0x00, 0x00))
                comlabel.today = False
                comlabel.inventory = True                
                gatherbutton.invs = True
                harvbutton.invs = True
                buildbutton.invs = True
                searchbutton.invs = True             
                
            else:                                    #turns on Gather, Harvest, Build, Search, Buttons
                self.fgColor = ((0xED, 0xC5, 0x15))
                comlabel.today = True
                comlabel.inventory = False
                gatherbutton.invs = False
                harvbutton.invs = False
                buildbutton.invs = False
                searchbutton.invs = False

        else:      #makes the button invisble when self.invs = True 
            self.fgColor = ((0xFF, 0xF1,0x93))

class Nextdaybutton(pygame.sprite.Sprite):
    """ a button the advances the day 
        same properties as label + button
        active: True if user is clicking on sprite
                False if user is not currently clicking
        clicked: True when user releases mouse over a 
                 currently active button
    """

    def __init__(self, comlabel, paper):
        pygame.sprite.Sprite.__init__(self)
        self.top = comlabel.bottom
        self.font = pygame.font.Font("goodfoot.ttf", 36)
        self.text = "next day"
        self.fgColor = ((0x00, 0x00, 0x00))
        self.bgColor = ((0xFF, 0xF1,0x93))
        self.center = (650, 480)
        self.size = (150, 60)
        self.active = False
        self.clicked = False
        self.invs = False
        self.nextDay = False
        
    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        transColor = self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text, set xPos to 0 to left aline to background rect
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
        #if not invs, buttons can receive input, 
        if self.invs != True:
            #check for mouse input
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.fgColor = ((0xFF, 0xFF, 0xFF))
                    self.active = True
                    
            #check for mouse release
            if self.active == True:
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.active = False
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.clicked =  not self.clicked
                        paper.state = paper.MOVING
                        
                        
            if paper.state == paper.MOVING: # turns other buttons off
                self.fgColor = ((0xFF, 0x00, 0x00))
                              
            else: #turns other buttons back on
                self.fgColor = ((0xED, 0xC5, 0x15))
                
class Nextdayupdate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.day = 1
        self.seasonDay = random.randint(1,364)
        self.nextDay = False
        self.weather = "Sunny"
        self.season = "typhoon season"

    def update(self):
        if self.nextDay == True:
            self.nextDay = False
            
            self.day += 1
            self.seasonDay += 1

            #Season update
            if self.seasonDay >=365:
                self.seasonDay = 1

            if self.seasonDay == self.seasonDay in range(1, 56) or self.seasonDay in range(316, 364): # rainy season (winter months) 15 weeks long
                self.season = "rainy season"                                
            elif self.seasonDay == self.seasonDay in range(57, 126):                #growing season (spring months) 10 weeks long
                self.season = "growing season"
            elif self.seasonDay == self.seasonDay in range(127, 168):               #typhoon season (Months that typhoons hit) 6 weeks long
                self.season = "typhoon season"
            elif self.seasonDay == self.seasonDay in range(169, 252):               #Hot season ( Summer months) 12 weeks long
                self.season = "hot season"
            elif self.seasonDay == self.seasonDay in range(253, 315):               #cool months (fall months) 9 weeks long
                self.season = "cool season"
            elif self.seasonDay >=366:
                print("there is something wrong with the seasons")

            #Weather update
            if self.season == "rainy season":
                weather = random.randint(1,100)
                if weather == weather in range(1,30):
                    self.weather = "Rain"
                elif weather == weather in range(31,45):
                    self.weather = "Drizzling"
                elif weather == weather in range(46, 50):
                    self.weather = "Windy"
                elif weather == weather in range(51 - 70):
                    self.weather = "Sunny"
                elif weather == weather in range(71 - 80):
                    self.weather = "Cool"
                elif weather == weather in range(81 - 90):
                    self.weather = "Warm"
                elif weather == weather in range(91 - 95):
                    self.weather = "Hot"
                elif weather == weather in range(96 - 100):
                    self.weather = "Cold"
                
            elif self.season == "growing season":
                weather = random.randint(1,100)
                if weather == weather in range(1,20):
                    self.weather = "Rain"
                elif weather == weather in range(21,30):
                    self.weather = "Drizzling"
                elif weather == weather in range(31, 45):
                    self.weather = "Windy"
                elif weather == weather in range(46,60):
                    self.weather = "Sunny"
                elif weather == weather in range(71, 75):
                    self.weather = "Cool"
                elif weather == weather in range(75, 90):
                    self.weather = "Warm"
                elif weather == weather in range(91, 95):
                    self.weather = "Hot"
                elif weather == weather in range(96, 100):
                    self.weather = "Cold"            

            elif self.season == "typhoon season":
                weather = random.randint(1,100)
                if weather == weather in range(1,30):
                    self.weather = "Rain"
                elif weather == weather in range(31,40):
                    self.weather = "Drizzling"
                elif weather == weather in range(41, 50):
                    self.weather = "Windy"
                elif weather == weather in range(51, 60):
                    self.weather = "Sunny"
                elif weather == weather in range(61, 70):
                    self.weather = "Cool"
                elif weather == weather in range(71, 80):
                    self.weather = "Warm"
                elif weather == weather in range(81, 85):
                    self.weather = "Hot"
                elif weather == weather in range(86 - 100):
                    self.weather = "Typhoon"
                
            elif self.season == "hot season":
                weather = random.randint(1,100)
                if weather == weather in range(1,10):
                    self.weather = "Rain"
                elif weather == weather in range(11,15):
                    self.weather = "Drizzling"
                elif weather == weather in range(16, 20):
                    self.weather = "Windy"
                elif weather == weather in range(21,40):
                    self.weather = "Sunny"
                elif weather == weather in range(41, 45):
                    self.weather = "Cool"
                elif weather == weather in range(56, 60):
                    self.weather = "Warm"
                elif weather == weather in range(61, 80):
                    self.weather = "Hot"
                elif weather == weather in range(81,100):
                    self.weather = "Very hot"
                                                 
            elif self.season == "cool season":
                weather = random.randint(1,100)
                if weather == weather in range(1,20):
                    self.weather = "Rain"
                elif weather == weather in range(21,30):
                    self.weather = "Drizzling"
                elif weather == weather in range(31, 35):
                    self.weather = "Windy"
                elif weather == weather in range(36,50):
                    self.weather = "Sunny"
                elif weather == weather in range(51, 70):
                    self.weather = "Cool"
                elif weather == weather in range(71, 80):
                    self.weather = "Warm"
                elif weather == weather in range(98, 100):
                    self.weather = "Snow"
                elif weather == weather in range(81, 97):
                    self.weather = "Cold" 
            else:
                print("There is something wrong with the weather")

            #Health update
        
            
             #Delete when weather history is not needed 
            print(self.day, self.seasonDay, self.season, self.weather, weather)
                        
            
            
                            
class Lines(pygame.sprite.Sprite):
    def __init__(self):
        self.delete = 1
                
class Reportnode(object):   
    def __init__(self, health,):
        self.description = desc

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Castaway")

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
screen.blit(background, (0, 0))

nextdayupdate = Nextdayupdate()

paper = Paper(background)
daylabel = Daylabel(nextdayupdate)
weatherlabel = Weatherlabel()
healthlabel = Healthlabel()
dhistlbl = Dhistlbl()
comlabel = Comlabel(dhistlbl)
gatherbutton = Gatherbutton(comlabel)
gathfbutton = GathFbutton(gatherbutton)
gathwbutton = GathWbutton(gatherbutton, gathfbutton)
gathsbutton = GathSbutton(gatherbutton, gathwbutton)
harvbutton = Harvbutton(comlabel)
searchbutton = Searchbutton(comlabel)
buildbutton = Buildbutton(comlabel)
checkbutton = Checkbutton(comlabel)
nextdaybutton = Nextdaybutton(comlabel, paper)


backgroundSprites = pygame.sprite.Group(paper)
GUISprites = pygame.sprite.Group(daylabel,weatherlabel, healthlabel, dhistlbl, comlabel)
GUIBUTTONS = pygame.sprite.Group(gatherbutton, gathfbutton, gathwbutton, gathsbutton, harvbutton, buildbutton, searchbutton, checkbutton, nextdaybutton)
GameUpdate = pygame.sprite.Group(nextdayupdate)

clock = pygame.time.Clock()
mainLoop = True


while mainLoop:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            mainLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paper.state = paper.MOVING
                if paper.state == paper.MOVING: # turns other buttons off
                    nextdaybutton.fgColor = ((0xFF, 0x00, 0x00))
                
                
    
    backgroundSprites.clear(screen, background)

    GameUpdate.update()
    backgroundSprites.update()
    GUISprites.update()
    GUIBUTTONS.update()
                                                                  
    backgroundSprites.draw(screen)
    GUISprites.draw(screen)
    GUIBUTTONS.draw(screen)

    pygame.display.flip()


