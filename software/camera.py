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
video = None
PATH = ""

class Camera:
    def __init__(self, camera_id):
        self.CAMERA_ID = camera_id
        self.video = cv2.VideoCapture(self.CAMERA_ID)
        self.cnt = 0
        self.img = None
        
    def capture(self):
        ret, self.img = self.video.read()
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img = self.img.swapaxes(0, 1)
        return self.img
    
    def convert_to_img(self, name, imgformat):
        cv2.imwrite(os.path.join(PATH, name+str(cnt)+imgformat), self.img)
        self.cnt = self.cnt + 1
        
    def destroy(self):
        video.release()
        cv2.DestroyAllWindows()
