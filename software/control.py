#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021
@author: ayambabu
"""

import pygame
import keyboard
import comms

#KEYS = ['w', 's', 'up', 'down', 'a', 'd', 'right', 'left', 'spacebar', 'command+w', 'esc']

class Control:
    def __init__(self, comm, exit_prog, speed):
        #key_input = pygame.key.get_pressed()
        self.comms = comm
        self.exit_program = exit_prog
        self.events = None
        self.key_input = None
        pygame.init()
        self.screen = pygame.display.set_mode([500,500])
        self.screen.fill((255, 255, 255))
        self.arg_byte = speed
        
        
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
                        ind = chr(0)+ chr(self.arg_byte)+ chr(255) # moveForward
                        self.on_trigger(ind)
                    if (event.key == pygame.K_s):
                        ind = chr(1) + chr(self.arg_byte)+ chr(255) # moveBack
                        self.on_trigger(ind)
                    if (event.key == pygame.K_UP):
                        ind = chr(2) + chr(self.arg_byte)+ chr(255) # moveUp
                        self.on_trigger(ind)
                    if (event.key == pygame.K_DOWN):
                        ind = chr(3) + chr(self.arg_byte)+ chr(255) # moveBack
                        self.on_trigger(ind)
                    if (event.key == pygame.K_a):
                        ind = chr(4) +  chr(self.arg_byte)+ chr(255) # moveLeft
                        self.on_trigger(ind)
                    if (event.key == pygame.K_d):
                        ind = chr(5) + chr(self.arg_byte)+ chr(255) # moveRight
                        self.on_trigger(ind)
                    if (event.key == pygame.K_RIGHT):
                        ind = chr(6) + chr(self.arg_byte)+ chr(255) #Turn Right
                        self.on_trigger(ind)
                    if (event.key == pygame.K_LEFT):
                        ind = chr(7) + chr(self.arg_byte) + chr(255) #TurnLeft
                        self.on_trigger(ind)
                    if (event.key == pygame.K_SPACE):
                        ind = chr(8) + '0' + chr(255) #Take screenshot
                        self.on_trigger(ind)
                    if (event.key == pygame.K_ESCAPE):
                        self.comms.kill_op()
                    #print(self.ind)


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ind = chr(0) + chr(0) + chr(255) # moveForward
                        self.on_trigger(ind)
                        #print('w')
                    if (event.key == pygame.K_s):
                        ind = chr(1) + chr(0)+ chr(255) # moveBack
                        self.on_trigger(ind)
                        #print('s')
                    if (event.key == pygame.K_UP):
                        ind = chr(2) + chr(0)+ chr(255) # moveUp
                        self.on_trigger(ind)
                        #print('up')
                    if (event.key == pygame.K_DOWN):
                        ind = chr(3) + chr(0)+ chr(255) # moveBack
                        self.on_trigger(ind)
                        #print('down')
                    if (event.key == pygame.K_a):
                        ind = chr(4) +  chr(0)+ chr(255) # moveLeft
                        self.on_trigger(ind)
                        #print('a')
                    if (event.key == pygame.K_d):
                        ind = chr(5) + chr(0)+ chr(255) # moveRight
                        self.on_trigger(ind)
                        #print('d')
                    if (event.key == pygame.K_RIGHT):
                        ind = chr(6) + chr(0)+ chr(255) #Turn Right
                        self.on_trigger(ind)
                        #print('right')
                    if (event.key == pygame.K_LEFT):
                        ind = chr(7) + chr(0) + chr(255) #TurnLeft
                        self.on_trigger(ind)
                        #print('left')
                    #elif (event.key == pygame.K_SPACE):
                        #self.ind = '8' + '0' + chr(255) #Take screenshot
            pygame.display.flip()
