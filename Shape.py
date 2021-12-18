# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:35:24 2021

@author: SANDHYA
"""

class Shape:
    def __init__(self, strokeWidth, strokeColor, fillColor):
        self.strokeWidth = strokeWidth
        self.strokeColor = strokeColor
        self.fillColor = fillColor
    
    def getstrokeWidth(self):
        return self.strokeWidth
    
    def getstrokeColor(self):
        return self.strokeColor
    
    def getfillColor(self):
        return self.fillColor
    
    def setstrokeWidth(self, strokeWidth):
        self.strokeWidth = strokeWidth
        
    def setstrokeColor(self, strokeColor):
        self.strokeColor = strokeColor
        
    def setfillColor(self, fillColor):
        self.fillColor = fillColor
    
    