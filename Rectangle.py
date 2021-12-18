# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 13:35:54 2021

@author: SANDHYA
"""
from Point import Point
from Shape import Shape
class Rectangle(Shape):
    def __init__(self, topleftpoint, width, height):
        self.width = width
        self.height = height
        self.topleftpoint = topleftpoint
    
    def init_shape(self, strokeWidth, strokeColor, fillColor):
        super().__init__(strokeWidth, strokeColor, fillColor)
        
    def gettopleftpoint(self):
        return self.topleftpoint
    
    def getwidth(self):
        return self.width
    
    def getheight(self):
        return self.height
    
    def settopleftpoint(self,topleftpoint):
        self.topleftpoint = topleftpoint
        
    def setwidth(self, width):
        self.width = width
        
    def setheight(self,height):
        self.height = height
        
    def area(self):
        area = self.width * self.height
        return float(area)
    
    def perimeter(self):
        perimeter = 2*(self.width + self.height)
        return float(perimeter)
    
    def contains(self, point):
        if(point.getX() > self.topleftpoint.getX() and point.getX() < self.topleftpoint.getX() + self.width and point.getY() > self.topleftpoint.getY() and point.getY() < self.topleftpoint.getY()+ self.height):
           return True
        else:
           return False
    
    def centroid(self):
        w = self.width/2
        h = self.height/2
        x = self.topleftpoint.getX() + w
        y = self.topleftpoint.getY() + h
        return Point(x,y)
    
    def toString(self):
       rectstr = "topleftpoint = " + self.topleftpoint.toString() + " width = " + str(self.width) + " height = " + str(self.height)
       return rectstr
        