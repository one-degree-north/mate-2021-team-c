#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:39:22 2021
@author: ayambabu
"""

import serial
import pygame
import convert_to_packet
import camera
import sys

NUM_BYTES = 3

class Communications:
    def __init__(self, usb, SCREEN_DIMENSIONS, cam_ids, BAUD_RATE):
        self.USB = usb
        self.cams = []
        for cam_id in cam_ids:
            self.cams.append(camera.Camera(cam_id))
        self.ser = serial.Serial(self.USB, BAUD_RATE)
        self.ser.close()
        self.ser.open()
    
    def kill_op(self):
        sys.exit()
        end_packet = chr(9) + chr(254) + chr(255)
        self.encode_and_send(end_packet)
        
    def encode_and_send(self, packets):
        self.ser.write(packets.encode("latin"))
        print("sent")
