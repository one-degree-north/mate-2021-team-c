#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021

@author: ayambabu
"""

import pygame
import keyboard
import exit_program


KEYS = []

class Control:
    def __init__(self, comm):
        #key_input = pygame.key.get_pressed()
        self.comms = comm
        self.events = None
        self.key_input = None
        pygame.init()
        
    def on_trigger(self, keys):
        self.comms.q.put(keys)
        
    def run(self):
        for KEY in KEYS:
            keyboard.add_hotkey(KEY, self.on_trigger(KEY))
            
        while True:
            self.events = pygame.event.get()
            
            for event in self.events:
                if event.type == pygame.QUIT:
                    exit_program.Exit()
