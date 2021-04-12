import pygame
import pygame_gui
import camera

class ShowX:
    def __init__(self,h, w, camID):
        pygame.init()
        self.h = h
        self.w = w
        self.screen = pygame.display.set_mode([h,w], pygame.RESIZABLE)
        self.cam = camera.Camera(camID)

    def create(self):

        pygame.init()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255,255,255))
            '''
            pygame.draw.rect(self.screen, (0, 0, 0), (0,0,((self.h/1.5)), (self.w/2)), 1)
            pygame.draw.rect(self.screen, (0, 0, 0), ((self.h/1.5),0,(self.h - (self.h/1.5)), (self.w/2)), 1)
            pygame.draw.rect(self.screen, (0, 0, 0), (0,(self.w/2),(self.h/1.5), (self.w/2)), 1)
            pygame.draw.rect(self.screen, (0, 0, 0), ((self.h/1.5),(self.w/2),(self.h-(self.h/1.5)), (self.w/2)), 1)
            '''

            rect = pygame.Rect(0, 0, self.h/2, self.w/2)
            #video = self.cam.capture()
            self.screen.blit(self.cam.capture(), (0,0), rect)
            pygame.display.flip()

        
        

    def ayamFunction(st, INFO_X):
        global width, height
        x = int(st)
        return (INFO_X + ((x % 3) * width / 3), INFO_Y + ((x // 3) * height / 12 ))

    
    



height = 4 #Input later
width = 5 #Input later
INFO_X = 0 #Input later
INFO_Y = 0 #Input later




