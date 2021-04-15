import pygame
import camera
import cv2


class ShowX:
    def __init__(self,h, w, camID):
        pygame.init()
        self.h = h
        self.w = w
        self.screen = pygame.display.set_mode([h,w], pygame.RESIZABLE)
        self.cam = cv2.VideoCapture(camID)

    def create(self):

        pygame.init()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            ret, frame = self.cam.read()
            
            #self.screen.fill([0, 0, 0])
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = frame.swapaxes(0, 1)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0,0))
            
            pygame.display.update()

        
        

    def ayamFunction(st, INFO_X):
        global width, height
        x = int(st)
        return (INFO_X + ((x % 3) * width / 3), INFO_Y + ((x // 3) * height / 12 ))

    
    



height = 4 #Input later
width = 5 #Input later
INFO_X = 0 #Input later
INFO_Y = 0 #Input later




