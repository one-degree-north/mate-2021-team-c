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
SPEED = 100
comm = None
exit_prog = None

def start():
    #create single instances of each class in the main class
    
    comm = comms.Communications(USB, SCREEN_DIMENSIONS, FPS, CAM_IDS)
    exit_prog = exit_program.Exit_Program(comm)
    controls = control.Control(comm, exit_prog, SPEED)

    #comms_thread = threading.Thread(target=comm.run)
    control_thread = threading.Thread(target=controls.run)
    
    #comms_thread.start()
    control_thread.start()
    #gui.GUI(SCREEN_DIMENSIONS, FPS, CAM_IDS)

def end():
    exit_prog.Exit()
    
start()
