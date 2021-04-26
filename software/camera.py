#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:15:26 2021
@author: ayambabu
"""

import cv2
import pygame.image as pyimg
import os

CAMERA_ID = -1
img = None
video = None
PATH = ""

class Camera:
    def __init__(self, camera_id):
        self.CAMERA_ID = camera_id
        video = cv2.VideoCapture(CAMERA_ID)
        
    def capture(self):
        ret, img = video.read()
        return img
    
    def convert_to_img(self, name, imgformat):
        os.chdir(PATH)
        cv2.imwrite(name+img_format, img)
        print("Screenshot Stored in: " + PATH)
        
    def destroy(self):
        video.release()
        cv2.DestroyAllWindows()
