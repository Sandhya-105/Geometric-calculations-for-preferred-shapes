# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:46:21 2021

@author: SANDHYA
"""
import math
from Shape import Shape

class Circle(Shape):
    def __init__(self, centerpoint, radius):
        self.centerpoint = centerpoint
        self.radius = radius
    
    def init_shape(self, strokeWidth, strokeColor, fillColor):
        super().__init__(strokeWidth, strokeColor, fillColor)
        
    def getcenterpoint(self):
        return self.centerpoint
    
    def getradius(self):
        return self.radius
    
    def setcenterpoint(self, centerpoint):
        self.centerpoint = centerpoint
    
    def setradius(self, radius):
        self.radius = radius
    
    def area(self):
        area = math.pi * self.radius * self.radius
        return area
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def contains(self, Point):
        d = self.centerpoint.distance(Point.getX(),Point.getY())
        if d < self.radius:
            return True
        else:
            return False
    
    def toString(self):
        cirstr = "centerpoint = " + self.centerpoint.toString() + " radius = " + str(self.radius)
        return cirstr