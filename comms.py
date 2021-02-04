#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:39:22 2021

@author: ayambabu
"""

import serial
import pygame
import convert_to_packet.py
import gui.py
import camera.py

USB = ""
PACKET = ""
NUM_BYTES = 3
ser = None
cam = None

class Communications:
    def __init__(usb, camera_id1, camera_id2, SCREEN_DIMENSIONS, FPS, CAM_ID):
        USB = usb
        cam = (camera.Camera(camera_id1), camera.Camera(camera_id2))
        ser = serial.Serial(str(USB), 230400)
        gui.GUI(cam, SCREEN_DIMENSIONS, FPS, CAM_ID) ###
    
    def kill_op(self):
        self.encode_and_send('9' + chr(254) + chr(255))
    
    def receive(keys):
        convert_to_packet.CONVERT_TO_PACKET(keys)
        
    def encode_and_send(packets):
        for c in packets:
            ser.write(c.encode("latin"))
    
    def receive_packets(self, packets):
        line = ""
        if(packets[0] == '8'):
            if(packets[1] == chr(12)):
                cam[0].collect_screenshot() ###
                cam[1].collect_screenshot()
            else:
                self.encode_and_send(packets) ###
                line = ser.read(NUM_BYTES)
                
        elif(packets[0] == '9'):
            self.kill_op()
                
        return line
        
    def run(self):
        while True:
            return 0