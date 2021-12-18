# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:53:04 2021

@author: SANDHYA
"""
import math
from Shape import Shape
class Point(Shape):
    def __init__(self, X, Y):
        self.X = float(X)
        self.Y = float(Y)
        
    def init_shape(self, strokeWidth, strokeColor, fillColor):
        super().__init__(strokeWidth, strokeColor, fillColor)
        
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    
    def setX(self, X):
        self.X = X
    def setY(self, Y):
        self.Y = Y
        
    def setPosition(self,X,Y):
        self.X = X
        self.Y = Y
        
    def distance(self, X, Y):
        xpt = (self.X - X) ** 2
        ypt = (self.Y - Y) ** 2
        dist = math.sqrt(xpt + ypt)
        return dist
    
    def toString(self):
        ptstr = "Point ("+ str(self.X) + "," + str(self.Y) + ")"
        return ptstr


        

        
        