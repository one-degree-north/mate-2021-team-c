#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:08:59 2021

@author: ayambabu
"""

import sys
import comms.py

class exit_program:
    def Exit():
        comms.kill_op()
        #time to look at the message
        sys.exit()