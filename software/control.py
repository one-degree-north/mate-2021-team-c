#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:11 2021
@author: ayambabu
"""

import pygame
import keyboard

KEYS = ['w', 's', 'up', 'down', 'a', 'd', 'right', 'left', 'spacebar', 'command+w', 'esc']

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
        c = True
        while c:        
            if(keyboard.is_pressed('w')):
            	self.on_trigger('w')
             
            if(keyboard.is_pressed('s')):
            	self.on_trigger('s')
             
            if(keyboard.is_pressed('up')):
            	self.on_trigger('up')
             
            if(keyboard.is_pressed('down')):
            	self.on_trigger('down')
             
            if(keyboard.is_pressed('a')):
            	self.on_trigger('a')
             
            if(keyboard.is_pressed('d')):
            	self.on_trigger('d')
             
            if(keyboard.is_pressed('right')):
            	self.on_trigger('right')
             
            if(keyboard.is_pressed('left')):
            	self.on_trigger('left')
             
            if(keyboard.is_pressed('spacebar')):
            	self.on_trigger('spacebar')
             
            if(keyboard.is_pressed('command+w')):
            	self.on_trigger('command+w')
                
            if(keyboard.is_pressed('esc')):
                self.exit_program.Exit()
                
            self.events = pygame.event.get()
            
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.exit_program.Exit()
                    
                    