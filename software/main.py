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
import threading

USB = ""
SCREEN_DIMENSIONS = () # width, height
FPS = 30
CAM_IDS = [1]
SPEED = 100
comm = None
exit_prog = None

def start():
    comm = comms.Communications(USB, SCREEN_DIMENSIONS, FPS, CAM_IDS)
    exit_prog = exit_program.Exit_Program(comm)
    controls = control.Control(comm, exit_prog, SPEED)
    control_thread = threading.Thread(target=controls.run)
    control_thread.start()

def end():
    exit_prog.Exit()
    
start()
