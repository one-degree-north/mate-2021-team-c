#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:11:01 2021

@author: ayambabu, haardikchopra
"""

import sys
import keyboard
#import serial
import pygame

#ser = serial.Serial('/dev/tty.usbmodem1431', 230400)
screen = pygame.display.set_mode((400, 300))

black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
red = ( 255, 0, 0)

# Kind of like XBox Controller Color Scheme

#def encode_and_send(string):
 #   for c in string:
  #      ser.write(c.encode("latin"))
   # return 0

while True:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    if keyboard.is_pressed('w'):
        print("Moving 1 block forward")
        pygame.draw.rect(screen, yellow, pygame.Rect(100, 100, 200, 100))
        #encode_and_send('0'+'w')
    elif pygame.key.get_pressed()[pygame.K_a]:
        print("Moving 1 block left")
        pygame.draw.rect(screen, blue, pygame.Rect(100, 100, 200, 100))
        #encode_and_send('0'+'a')
    elif pygame.key.get_pressed()[pygame.K_d]:
        print("Moving 1 block right")
        pygame.draw.rect(screen, red, pygame.Rect(100, 100, 200, 100))
        #encode_and_send('0'+'d')
    elif pygame.key.get_pressed()[pygame.K_s]:
        print("Moving 1 block down")
        pygame.draw.rect(screen, green, pygame.Rect(100, 100, 200, 100))
        #encode_and_send('0'+'s')
        
    pygame.display.update()
    pygame.time.Clock().tick(30)
    pygame.display.flip()
