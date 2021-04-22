import pygame
import camera
import cv2
import comms


class GUI:
    def __init__(self, screen_dim, cam, comm, exit_prog, POWER):
        pygame.init()
        self.h = h
        self.w = w
        self.screen = pygame.display.set_mode(screen_dim, pygame.RESIZABLE)
        self.cam = cam
        self.comm = comm
        self.exit_program = exit_prog
        self.POWER_BYTE = chr(POWER)
        self.REST_BYTE = chr(0)
        self.TERMINAL_BYTE = chr(255)
        
       

    def on_trigger(self, keys):
        #self.comm.encode_and_send(keys)
        print("sent")

    def create(self):

        pygame.init()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        cmd_byte = chr(0)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE # moveForward
                        self.on_trigger(packet)
                    if (event.key == pygame.K_s):
                        cmd_byte = chr(1)
                        packet = cmd_byte + self.POWER_BYTE+ self.TERMINAL_BYTE # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_DOWN):
                        cmd_byte = chr(2)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE # moveUp
                        self.on_trigger(packet)
                    if (event.key == pygame.K_UP):
                        cmd_byte = chr(3)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_a):
                        cmd_byte = chr(4)
                        packet = cmd_byte +  self.POWER_BYTE + self.TERMINAL_BYTE # moveLeft
                        self.on_trigger(packet)
                    if (event.key == pygame.K_d):
                        cmd_byte = chr(5)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE # moveRight
                        self.on_trigger(packet)
                    if (event.key == pygame.K_RIGHT):
                        cmd_byte = chr(6)
                        packet = cmd_byte + self.POWER_BYTE+ self.TERMINAL_BYTE #Turn Right
                        self.on_trigger(packet)
                    if (event.key == pygame.K_LEFT):
                        cmd_byte = chr(7)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE #TurnLeft
                        self.on_trigger(packet)
                    if (event.key == pygame.K_x):
                        self.cam.convert_to_img("moment", ".jpg")
                    if (event.key == pygame.K_SPACE):
                        cmd_byte = chr(8)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE #MoveClaw
                        self.on_trigger(packet)
                    if (event.key == pygame.K_ESCAPE):
                        running = False
                    
                        
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        cmd_byte = chr(0)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE # moveForward
                        self.on_trigger(packet)
                    if (event.key == pygame.K_s):
                        cmd_byte = chr(1)
                        packet = cmd_byte + self.REST_BYTE+ self.TERMINAL_BYTE # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_DOWN):
                        cmd_byte = chr(2)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE # moveUp
                        self.on_trigger(packet)
                    if (event.key == pygame.K_UP):
                        cmd_byte = chr(3)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_a):
                        cmd_byte = chr(4)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE # moveLeft
                        self.on_trigger(packet)
                    if (event.key == pygame.K_d):
                        cmd_byte = chr(5)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE # moveRight
                        self.on_trigger(packet)
                    if (event.key == pygame.K_RIGHT):
                        cmd_byte = chr(6)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE #Turn Right
                        self.on_trigger(packet)
                    if (event.key == pygame.K_LEFT):
                        cmd_byte = chr(7)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE #TurnLeft
                        self.on_trigger(packet)


                    

            
            frame = self.cam.capture()
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0,0))
            
            pygame.display.update()

        
        




def testing():
    gui = GUI(1280, 720, camera.Camera(0), None, None, 200)
    gui.create()


#testing()
    



height = 4 #Input later
width = 5 #Input later
INFO_X = 0 #Input later
INFO_Y = 0 #Input later




