#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021

@author: ayambabu
"""

import pygame
import keyboard
import exit_program

pygame.init()

key_input = None
events = None
comms = None
KEYS = []

class control:
    def __init__(comm):
        #key_input = pygame.key.get_pressed()
        comms = comm
        
    def on_trigger(keys):
        comms.q.put(keys)
        
    def run(self):
        for KEY in KEYS:
            keyboard.add_hotkey(KEY, self.on_trigger(KEY))
            
        while True:
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    exit_program.Exit()