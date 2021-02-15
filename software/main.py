#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:34:28 2021

@author: ayambabu
"""

import sys
import exit_program
import control
import comms
# import gui
import threading

USB = ""
SCREEN_DIMENSIONS = () # width, height
FPS = 30
CAM_IDS = [1]
comm = None
exit_prog = None

def start():
    #create single instances of each class in the main class
    
    comm = comms.Communications(USB, SCREEN_DIMENSIONS, FPS, CAM_IDS)
    exit_prog = exit_program.Exit_Program(comm)
    controls = control.Control(self.comm, self.exit_program)
    
    control_thread = threading.Thread(target=self.controls.run())
    comms_thread = threading.Thread(target=self.comm.run())
    
    control_thread.start()
    comms_thread.start()
    #gui.GUI(SCREEN_DIMENSIONS, FPS, CAM_IDS)

def end():
    exit_prog.Exit()
    
start()
