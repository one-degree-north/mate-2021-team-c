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
        self.comms.receive(keys)
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ind = '0'+ chr(50)+ chr(255) # moveForward
                        on_trigger(ind)
                    if (event.key == pygame.K_s):
                        ind = '1' + chr(50)+ chr(255) # moveBack
                        on_trigger(ind)
                    if (event.key == pygame.K_UP):
                        ind = '2' + chr(50)+ chr(255) # moveUp
                        on_trigger(ind)
                    if (event.key == pygame.K_DOWN):
                        ind = '3' + chr(50)+ chr(255) # moveBack
                        on_trigger(ind)
                    if (event.key == pygame.K_a):
                        ind = '4' +  chr(50)+ chr(255) # moveLeft
                        on_trigger(ind)
                    if (event.key == pygame.K_d):
                        ind = '5' + chr(50)+ chr(255) # moveRight
                        on_trigger(ind)
                    if (event.key == pygame.K_RIGHT):
                        ind = '6' + chr(50)+ chr(255) #Turn Right
                        on_trigger(ind)
                    if (event.key == pygame.K_LEFT):
                        ind = '7' + chr(50) + chr(255) #TurnLeft
                        on_trigger(ind)
                    if (event.key == pygame.K_SPACE):
                        ind = '8' + '0' + chr(255) #Take screenshot
                        on_trigger(ind)
                    #print(self.ind)


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ind = chr(0) + chr(0) + chr(255) # moveForward
                        on_trigger(ind)
                        #print('w')
                    if (event.key == pygame.K_s):
                        ind = chr(1) + chr(0)+ chr(255) # moveBack
                        on_trigger(ind)
                        #print('s')
                    if (event.key == pygame.K_UP):
                        ind = chr(2) + chr(0)+ chr(255) # moveUp
                        on_trigger(ind)
                        #print('up')
                    if (event.key == pygame.K_DOWN):
                        ind = chr(3) + chr(0)+ chr(255) # moveBack
                        on_trigger(ind)
                        #print('down')
                    if (event.key == pygame.K_a):
                        ind = chr(4) +  chr(0)+ chr(255) # moveLeft
                        on_trigger(ind)
                        #print('a')
                    if (event.key == pygame.K_d):
                        ind = chr(5) + chr(0)+ chr(255) # moveRight
                        on_trigger(ind)
                        #print('d')
                    if (event.key == pygame.K_RIGHT):
                        ind = chr(6) + chr(0)+ chr(255) #Turn Right
                        on_trigger(ind)
                        #print('right')
                    if (event.key == pygame.K_LEFT):
                        ind = chr(7) + chr(0) + chr(255) #TurnLeft
                        on_trigger(ind)
                        #print('left')
                    #elif (event.key == pygame.K_SPACE):
                        #self.ind = '8' + '0' + chr(255) #Take screenshot
