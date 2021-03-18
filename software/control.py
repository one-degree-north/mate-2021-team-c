#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021
@author: ayambabu
"""

import pygame
import keyboard

#KEYS = ['w', 's', 'up', 'down', 'a', 'd', 'right', 'left', 'spacebar', 'command+w', 'esc']

class Control:
    def __init__(self, comm, exit_prog):
        #key_input = pygame.key.get_pressed()
        self.comms = comm
        self.exit_program = exit_prog
        self.events = None
        self.key_input = None
        pygame.init()
        
    def on_trigger(self, keys):
        self.comms.q.put(keys)
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.ind = '0'+ chr(50)+ chr(255) # moveForward
                        on_trigger(self.ind)
                    if (event.key == pygame.K_s):
                        self.ind = '1' + chr(50)+ chr(255) # moveBack
                        on_trigger(self.ind)
                    if (event.key == pygame.K_UP):
                        self.ind = '2' + chr(50)+ chr(255) # moveUp
                        on_trigger(self.ind)
                    if (event.key == pygame.K_DOWN):
                        self.ind = '3' + chr(50)+ chr(255) # moveBack
                        on_trigger(self.ind)
                    if (event.key == pygame.K_a):
                        self.ind = '4' +  chr(50)+ chr(255) # moveLeft
                        on_trigger(self.ind)
                    if (event.key == pygame.K_d):
                        self.ind = '5' + chr(50)+ chr(255) # moveRight
                        on_trigger(self.ind)
                    if (event.key == pygame.K_RIGHT):
                        self.ind = '6' + chr(50)+ chr(255) #Turn Right
                        on_trigger(self.ind)
                    if (event.key == pygame.K_LEFT):
                        self.ind = '7' + chr(50) + chr(255) #TurnLeft
                        on_trigger(self.ind)
                    if (event.key == pygame.K_SPACE):
                        self.ind = '8' + '0' + chr(255) #Take screenshot
                        on_trigger(self.ind)
                    #print(self.ind)


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.ind = chr(0) + chr(0) + chr(255) # moveForward
                        on_trigger(self.ind)
                        #print('w')
                    if (event.key == pygame.K_s):
                        self.ind = chr(1) + chr(0)+ chr(255) # moveBack
                        on_trigger(self.ind)
                        #print('s')
                    if (event.key == pygame.K_UP):
                        self.ind = chr(2) + chr(0)+ chr(255) # moveUp
                        on_trigger(self.ind)
                        #print('up')
                    if (event.key == pygame.K_DOWN):
                        self.ind = chr(3) + chr(0)+ chr(255) # moveBack
                        on_trigger(self.ind)
                        #print('down')
                    if (event.key == pygame.K_a):
                        self.ind = chr(4) +  chr(0)+ chr(255) # moveLeft
                        on_trigger(self.ind)
                        #print('a')
                    if (event.key == pygame.K_d):
                        self.ind = chr(5) + chr(0)+ chr(255) # moveRight
                        on_trigger(self.ind)
                        #print('d')
                    if (event.key == pygame.K_RIGHT):
                        self.ind = chr(6) + chr(0)+ chr(255) #Turn Right
                        on_trigger(self.ind)
                        #print('right')
                    if (event.key == pygame.K_LEFT):
                        self.ind = chr(7) + chr(0) + chr(255) #TurnLeft
                        on_trigger(self.ind)
                        #print('left')
                    #elif (event.key == pygame.K_SPACE):
                        #self.ind = '8' + '0' + chr(255) #Take screenshot
