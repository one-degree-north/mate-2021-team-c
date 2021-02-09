#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:34:28 2021

@author: ayambabu
"""

import sys
import exit_program.py
import control.py
import comms.py
import gui.py
import threading

USB = ""
SCREEN_DIMENSIONS = () # width, height
FPS = 30
CAM_ID = (1)

def start():
    #create single instances of each class in the main class
    controls = control.Control()
    comms.Comms(USB, SCREEN_DIMENSIONS, FPS, CAM_ID)
    
    control_thread = threading.Thread(target=controls.run())
    comms_thread = threading.Thread(target=comms.run())
    
    control_thread.start()
    comms_thread.start()
    #gui.GUI(SCREEN_DIMENSIONS, FPS, CAM_ID)

def end():
    exit_program.Exit()
    
start()