#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021

@author: ayambabu
"""

import pygame
import keyboard
import communications.py
import exit_program.py

pygame.init()

key_input = None
events = None
comms = None
KEYS = []

class control:
    def __init__():
        key_input = pygame.key.get_pressed()
        comms = communications.Communications()
        
    def on_trigger(keys):
        comms.receive(keys)
        
    def run(self):
        for KEY in KEYS:
            keyboard.add_hotkey(KEY, self.on_trigger(KEY))
            
        while True:
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    exit_program.Exit()