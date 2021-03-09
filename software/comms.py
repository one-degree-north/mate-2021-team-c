#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:39:22 2021
@author: ayambabu
"""

import serial
import pygame
import convert_to_packet
# import gui
import camera

from queue import Queue

NUM_BYTES = 3

class Communications:
    def __init__(self, usb, SCREEN_DIMENSIONS, FPS, cam_ids):
        self.USB = usb
        self.cams = []
        for cam_id in cam_ids:
            self.cams.append(camera.Camera(cam_id))
        self.ser = serial.Serial(self.USB, 230400)
        self.ctp = convert_to_packet.Convert_To_Packet()
        #gui.GUI(self.cam, SCREEN_DIMENSIONS, FPS, CAM_ID) ###
        self.q = Queue()
        self.PACKET = ""
    
    def kill_op(self):
        self.encode_and_send(chr(9) + chr(254) + chr(255))
    
    def receive(self, keys):
        return self.receive_packets(keys)
        
    def encode_and_send(self, packets):
        for c in packets:
            self.ser.write(c.encode("latin"))
    
    def receive_packets(self, packets):
        line = ""
        if(packets[0] == chr(8)):
            if(packets[1] == chr(12)):
                for cam in self.cams:
                    cam.collect_screenshot()
            else:
                self.encode_and_send(packets) ###
                line = self.ser.read(NUM_BYTES)
                
        elif(packets[0] == chr(9)):
            self.kill_op()
        else:
            self.encode_and_send(packets)
                
        return line
        
    def run(self):
        while True:
            """for i in range(int('0'), int('9')+1):
                self.receive_packets('8' + chr(i) + chr(255))
                
            self.receive_packets('8' + chr(10) + chr(255))
            self.receive_packets('8' + chr(11) + chr(255))"""
            
            while not self.q.empty():
                self.receive(self.q.get())
            
            # Take camera pic for GUI
