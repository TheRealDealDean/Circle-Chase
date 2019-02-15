import pygame, sys, math
class Button:

#x = 550 
#y = 275

#buttonColor = (255, 0, 0)
#buttonColor2 = (178, 34, 34)

        def __init__(self, buttonColor, buttonColor2, x, y, w, h):
                self.hovering = False
                self.buttonColor = buttonColor
                self.buttonColor2 = buttonColor2
                self.upperLeftX = x
                self.upperLeftY = y
                self.width = w
                self.height = h

        def mouseButtonOverlap(self):
                mouse = pygame.mouse.get_pos()
                if self.upperLeftX + self.width > mouse[0] > self.upperLeftX and self.upperLeftY + self.height > mouse[1] > self.upperLeftY:
                        self.hovering = True
                        #print(self.hovering)
                else:
                        self.hovering = False
                        #print(self.hovering)

        def renderButton(self, screen):
                if self.hovering:
                        pygame.draw.rect(screen, self.buttonColor2, (self.upperLeftX, self.upperLeftY, self.width, self.height), 0)
                else:
                        pygame.draw.rect(screen, self.buttonColor, (self.upperLeftX, self.upperLeftY, self.width, self.height), 0)
                        
