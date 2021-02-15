#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:08:59 2021

@author: ayambabu
"""

import sys

class Exit_Program:
    def __init__(self, comm):
        self.comms = comm
        
    def Exit(self):
        self.comms.kill_op()
        #time to look at the message
        sys.exit()
