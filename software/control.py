#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021
@author: ayambabu
"""

import pygame
import comms

class Control:
    def __init__(self, comm, exit_prog, POWER):
        self.comms = comm
        self.exit_program = exit_prog
        pygame.init()
        self.SCREEN_DIMS = [500,500]
        self.SCREEN_COLOR = (255, 255, 255)
        self.screen = pygame.display.set_mode(self.SCREEN_DIMS)
        self.screen.fill(self.SCREEN_COLOR)
        self.POWER = POWER
        
        
    def on_trigger(self, keys):
        self.comms.encode_and_send(keys)
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        packet = chr(0)+ chr(self.POWER)+ chr(255) # moveForward
                        self.on_trigger(packet)
                    if (event.key == pygame.K_s):
                        packet = chr(1) + chr(self.POWER)+ chr(255) # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_UP):
                        packet = chr(2) + chr(self.POWER)+ chr(255) # moveUp
                        self.on_trigger(packet)
                    if (event.key == pygame.K_DOWN):
                        packet = chr(3) + chr(self.POWER)+ chr(255) # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_a):
                        packet = chr(4) +  chr(self.POWER)+ chr(255) # moveLeft
                        self.on_trigger(packet)
                    if (event.key == pygame.K_d):
                        packet = chr(5) + chr(self.POWER)+ chr(255) # moveRight
                        self.on_trigger(paclet)
                    if (event.key == pygame.K_RIGHT):
                        packet = chr(6) + chr(self.POWER)+ chr(255) #Turn Right
                        self.on_trigger(packet)
                    if (event.key == pygame.K_LEFT):
                        packet = chr(7) + chr(self.POWER) + chr(255) #TurnLeft
                        self.on_trigger(packet)
                    if (event.key == pygame.K_SPACE):
                        packet = chr(8) + '0' + chr(255) #Take screenshot
                        self.on_trigger(packet)
                    if (event.key == pygame.K_ESCAPE):
                        running = False
                    #print(self.packet)


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        packet = chr(0) + chr(0) + chr(255) # moveForward
                        self.on_trigger(packet)
                        #print('w')
                    if (event.key == pygame.K_s):
                        packet = chr(1) + chr(0)+ chr(255) # moveBack
                        self.on_trigger(packet)
                        #print('s')
                    if (event.key == pygame.K_UP):
                        packet = chr(2) + chr(0)+ chr(255) # moveUp
                        self.on_trigger(packet)
                        #print('up')
                    if (event.key == pygame.K_DOWN):
                        packet = chr(3) + chr(0)+ chr(255) # moveBack
                        self.on_trigger(packet)
                        #print('down')
                    if (event.key == pygame.K_a):
                        packet = chr(4) +  chr(0)+ chr(255) # moveLeft
                        self.on_trigger(packet)
                        #print('a')
                    if (event.key == pygame.K_d):
                        packet = chr(5) + chr(0)+ chr(255) # moveRight
                        self.on_trigger(packet)
                        #print('d')
                    if (event.key == pygame.K_RIGHT):
                        packet = chr(6) + chr(0)+ chr(255) #Turn Right
                        self.on_trigger(packet)
                        #print('right')
                    if (event.key == pygame.K_LEFT):
                        packet = chr(7) + chr(0) + chr(255) #TurnLeft
                        self.on_trigger(packet)
                        #print('left')
                    #elif (event.key == pygame.K_SPACE):
                        #self.packet = '8' + '0' + chr(255) #Take screenshot
            pygame.display.flip()
        self.exit_program.Exit()   
