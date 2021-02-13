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
    def __init__(self, usb, camera_id1, camera_id2, SCREEN_DIMENSIONS, FPS):
        self.USB = usb
        self.cam = (camera.Camera(camera_id1), camera.Camera(camera_id2))
        self.ser = serial.Serial(str(self.USB), 230400)
        self.ctp = convert_to_packet.Convert_To_Packet()
        #gui.GUI(self.cam, SCREEN_DIMENSIONS, FPS, CAM_ID) ###
        self.q = Queue()
        self.PACKET = ""
    
    def kill_op(self):
        self.encode_and_send('9' + chr(254) + chr(255))
    
    def receive(self, keys):
        return self.receive_packets(self.ctp.pack(keys))
        
    def encode_and_send(self, packets):
        for c in packets:
            self.ser.write(c.encode("latin"))
    
    def receive_packets(self, packets):
        line = ""
        if(packets[0] == '8'):
            if(packets[1] == chr(12)):
                self.cam[0].collect_screenshot() ###
                self.cam[1].collect_screenshot()
            else:
                self.encode_and_send(packets) ###
                line = self.ser.read(NUM_BYTES)
                
        elif(packets[0] == '9'):
            self.kill_op()
        else:
            self.encode_and_send(packets)
                
        return line
        
    def run(self):
        while True:
            for i in range(int('1'), int('9')):
                self.receive_packets('8' + chr(i) + chr(255))
                
            self.receive_packets('8' + chr(10) + chr(255))
            self.receive_packets('8' + chr(11) + chr(255))
            
            while not self.q.empty():
                self.receive(self.q.get())
            
            # Take camera pic for GUI
