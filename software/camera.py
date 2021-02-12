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
        
    def capture(self):
        video = cv2.VideoCapture(CAMERA_ID)
        ret, img = video.read()
        return pyimg.frombuffer(img.tostring(), img.shape[1::-1], "RGB")
    
    def convert_to_img(self, name, imgformat):
        cv2.imwrite(os.path.join(PATH, name+imgformat), img)
        
    def destroy(self):
        video.release()
        cv2.DestroyAllWindows()
