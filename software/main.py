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
import camera
import gui

USB = ""
SCREEN_DIMENSIONS = (500,500) # width, height
CAM_IDS = 0
SPEED = 100
BAUD_RATE = 115200

def start():
    comm = comms.Communications(USB, CAM_IDS, BAUD_RATE)
    exit_prog = exit_program.Exit_Program(comm)
    cam = camera.Camera(CAM_IDS)
    display = gui.GUI(1280,720,cam)
    controls = control.Control(comm, exit_prog, SPEED, SCREEN_DIMENSIONS)
    gui_thread = threading.Thread(target=display.run)
    control_thread = threading.Thread(target=controls.run)
    gui_thread.start()
    control_thread.start()
    gui_thread.join()
    control_thread.join()
    
    

def end():
    exit_prog.Exit()
    
start()
