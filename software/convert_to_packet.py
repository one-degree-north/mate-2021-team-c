import pygame

key = 'w' #imported from control subsystem
secKey = 'q'#imported from control subsystem
ind = ''
allKeys= ['w', 'a', 'up', 'down', 'd', 'right', 'left', 'spacebar']


class Convert_To_Packet:
    
    def __init__(self):
        self.key = 'w'
        
        

    def pack(self):
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.ind = '0'+ chr(50)+ chr(255) # moveForward
                    if (event.key == pygame.K_s):
                        self.ind = '1' + chr(50)+ chr(255) # moveBack
                    if (event.key == pygame.K_UP):
                        self.ind = '2' + chr(50)+ chr(255) # moveUp
                    if (event.key == pygame.K_DOWN):
                        self.ind = '3' + chr(50)+ chr(255) # moveBack
                    if (event.key == pygame.K_a):
                        self.ind = '4' +  chr(50)+ chr(255) # moveLeft
                    if (event.key == pygame.K_d):
                        self.ind = '5' + chr(50)+ chr(255) # moveRight
                    if (event.key == pygame.K_RIGHT):
                        self.ind = '6' + chr(50)+ chr(255) #Turn Right
                    if (event.key == pygame.K_LEFT):
                        self.ind = '7' + chr(50) + chr(255) #TurnLeft
                    if (event.key == pygame.K_SPACE):
                        self.ind = '8' + '0' + chr(255) #Take screenshot
                    #print(self.ind)


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.ind = chr(0) + chr(0) + chr(255) # moveForward
                        #print('w')
                    if (event.key == pygame.K_s):
                        self.ind = chr(1) + chr(0)+ chr(255) # moveBack
                        #print('s')
                    if (event.key == pygame.K_UP):
                        self.ind = chr(2) + chr(0)+ chr(255) # moveUp
                        #print('up')
                    if (event.key == pygame.K_DOWN):
                        self.ind = chr(3) + chr(0)+ chr(255) # moveBack
                        #print('down')
                    if (event.key == pygame.K_a):
                        self.ind = chr(4) +  chr(0)+ chr(255) # moveLeft
                        #print('a')
                    if (event.key == pygame.K_d):
                        self.ind = chr(5) + chr(0)+ chr(255) # moveRight
                        #print('d')
                    if (event.key == pygame.K_RIGHT):
                        self.ind = chr(6) + chr(0)+ chr(255) #Turn Right
                        #print('right')
                    if (event.key == pygame.K_LEFT):
                        self.ind = chr(7) + chr(0) + chr(255) #TurnLeft
                        #print('left')
                    #elif (event.key == pygame.K_SPACE):
                        #self.ind = '8' + '0' + chr(255) #Take screenshot
                    

                    

    
