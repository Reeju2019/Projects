# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:09:03 2020

@author: reeju
"""
import random
from  config import Config

class Apple():
    def __init__(self):
        self.setNewLocation()
        
    def setNewLocation(self):
        self.x = random.randint(0, Config.CELLWIDTH - 1)
        self.y = random.randint(0, Config.CELLHEIGHT - 1)
        
        