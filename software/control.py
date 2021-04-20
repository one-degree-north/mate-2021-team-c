#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021
@author: ayambabu
"""

import pygame
import comms
import gui
import camera

class Control:
    def __init__(self, gui, comm, exit_prog, POWER, SCREEN_DIMS):
        self.comms = comm
        self.gui = gui
        self.exit_program = exit_prog
        pygame.init()
        self.SCREEN_DIMS = SCREEN_DIMS
        self.SCREEN_COLOR = (255, 255, 255)
        #self.screen = pygame.display.set_mode(self.SCREEN_DIMS)
        #self.screen.fill(self.SCREEN_COLOR)
        self.POWER_BYTE = chr(POWER)
        self.REST_BYTE = chr(0)
        self.TERMINAL_BYTE = chr(255)
        
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
                        cmd_byte = chr(0)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE # moveForward
                        self.on_trigger(packet)
                    if (event.key == pygame.K_s):
                        cmd_byte = chr(1)
                        packet = cmd_byte + self.POWER_BYTE+ self.TERMINAL_BYTE # moveBack
                        self.on_trigger(packet)
                    if (event.key == pygame.K_UP):
                        cmd_byte = chr(2)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE # moveUp
                        self.on_trigger(packet)
                    if (event.key == pygame.K_DOWN):
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
                        self.on_trigger(paclet)
                    if (event.key == pygame.K_RIGHT):
                        cmd_byte = chr(6)
                        packet = cmd_byte + self.POWER_BYTE+ self.TERMINAL_BYTE #Turn Right
                        self.on_trigger(packet)
                    if (event.key == pygame.K_LEFT):
                        cmd_byte = chr(7)
                        packet = cmd_byte + self.POWER_BYTE + self.TERMINAL_BYTE #TurnLeft
                        self.on_trigger(packet)
                    if (event.key == pygame.K_SPACE):
                        self.cam.convert_to_img("moment", ".jpg")
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
                    if (event.key == pygame.K_UP):
                        cmd_byte = chr(2)
                        packet = cmd_byte + self.REST_BYTE + self.TERMINAL_BYTE # moveUp
                        self.on_trigger(packet)
                    if (event.key == pygame.K_DOWN):
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

            self.gui.create()
            pygame.display.flip()

        self.exit_program.Exit()   
