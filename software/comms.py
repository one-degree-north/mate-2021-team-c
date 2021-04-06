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
    def __init__(self, usb, SCREEN_DIMENSIONS, FPS, cam_ids, baud_rate):
        self.USB = usb
        self.cams = []
        for cam_id in cam_ids:
            self.cams.append(camera.Camera(cam_id))
        self.ser = serial.Serial(self.USB, baud_rate)
        self.ser.close()
        self.ser.open()
        
        self.PACKET = ""
    
    def kill_op(self):
        sys.exit()
        end_packet = chr(9) + chr(254) + chr(255)
        self.encode_and_send(end_packet)
        
    def encode_and_send(self, packets):
        self.ser.write(packets.encode("latin"))
        print("sent")
 
    def receive(self, packets):
        line = ""
        cams_cmd_byte = chr(8)
        sshot_byte = chr(12)
        cmd_byte_received = packets[0]
        arg_byte_received = packets[1]
        
        if(cmd_byte_received == cams_cmd_byte):
            if(arg_byte_received == sshot_byte):
                for cam in self.cams:
                    cam.collect_screenshot()
            else:
                self.encode_and_send(packets) ###
                line = self.ser.read(NUM_BYTES)
                
        else:
            self.encode_and_send(packets)
                
        return line
        
    """def run(self):
        while True:
            for i in range(int('0'), int('9')+1):
                self.receive_packets('8' + chr(i) + chr(255))
                
            self.receive_packets('8' + chr(10) + chr(255))
            self.receive_packets('8' + chr(11) + chr(255))
            
            while not self.q.empty():
                self.receive(self.q.get())
            
            # Take camera pic for GUI
    """
