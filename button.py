import pygame, sys, math
class Button:

#x = 550 
#y = 275

#buttonColor = (255, 0, 0)
#buttonColor2 = (178, 34, 34)

        def __init__(self, buttonLabel, buttonColor, buttonColor2, x, y, w, h):
                self.hovering = False
                self.clicked = False
                self.buttonColor = buttonColor
                self.buttonColor2 = buttonColor2
                self.upperLeftX = x
                self.upperLeftY = y
                self.width = w
                self.height = h
                self.buttonLabel = buttonLabel 

        def mouseButtonOverlap(self):
                mouse = pygame.mouse.get_pos()
                if self.upperLeftX + self.width > mouse[0] > self.upperLeftX and self.upperLeftY + self.height > mouse[1] > self.upperLeftY:
                        self.hovering = True
                        #print(self.hovering)
                else:
                        self.hovering = False
                        #print(self.hovering)

        def centreText(self, textSurface):
                boxCentX = self.width/2
                boxCentY = self.height/2
                textCentX = textSurface.get_width()/2
                textCentY = textSurface.get_height()/2
                dx = boxCentX - textCentX
                dy = boxCentY - textCentY
                textboxX = self.upperLeftX + dx
                textboxY = self.upperLeftY + dy
                return (textboxX, textboxY)
                

        def renderButton(self, screen, gameFont):
                buttonString =  gameFont.render(self.buttonLabel, True, (255, 255, 255))
                if self.hovering:
                        pygame.draw.rect(screen, self.buttonColor2, (self.upperLeftX, self.upperLeftY, self.width, self.height), 0)
                else:
                        pygame.draw.rect(screen, self.buttonColor, (self.upperLeftX, self.upperLeftY, self.width, self.height), 0)
                screen.blit(buttonString, self.centreText(buttonString))
                
        def buttonClicked(self):
                if self.hovering == True and pygame.mouse.get_pressed()[0] == True:
                        self.clicked = True
                        print(self.clicked)
                else:
                        self.clicked = False
                        print(self.clicked)
