#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:15:26 2021
@author: ayambabu
"""

import cv2
import pygame.image as pyimg
import os

CAMERA_ID = 0
img = None
video = None
PATH = ""

class Camera:
    def __init__(self, camera_id):
        self.CAMERA_ID = camera_id
        self.video = cv2.VideoCapture(self.CAMERA_ID)
        
    def capture(self):
        ret, img = self.video.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.swapaxes(0, 1)
        return img
    
    def convert_to_img(self, name, imgformat):
        cv2.imwrite(os.path.join(PATH, name+imgformat), img)
        
    def destroy(self):
        video.release()
        cv2.DestroyAllWindows()
