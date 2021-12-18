# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:15:34 2021

@author: SANDHYA
"""

import unittest
import Point


class TestPoint(unittest.TestCase):


    def test_get_X(self):
        test_point  =  Point.Point(15, 35)
        self.assertEqual(15, test_point.getX())
        
    def test_get_Y(self):
        test_point  =  Point.Point(15, 35)
        self.assertEqual(35, test_point.getY())
        
    def test_set_X(self):
        test_point = Point.Point(7,22)
        test_point.setX(10)
        self.assertEqual(10, test_point.getX())
        
    def test_set_Y(self):
        test_point = Point.Point(7,22)
        test_point.setY(7)
        self.assertEqual(7, test_point.getY())
        
    def test_setPosition(self):
        test_point = Point.Point(22,7)        
        test_point.setPosition(11,22)
        position = (test_point.getX(),test_point.getY())
        self.assertTupleEqual((11,22), position)
        
    def test_distance(self):
        test_point = Point.Point(5,5)
        self.assertEqual(1, test_point.distance(6,5))
        
    def test_toString(self):
        test_point = Point.Point(12,15)
        self.assertEqual("Point (12.0,15.0)", test_point.toString())
    
    def test_getstrokewidth(self):
        test_point = Point.Point(12,15)
        test_point.init_shape(10, "yellow", "pink")
        self.assertEqual(10, test_point.getstrokeWidth())
    
    def test_getstrokecolor(self):
        test_point = Point.Point(12,15)
        test_point.init_shape(10, "yellow", "pink")
        self.assertEqual("yellow", test_point.getstrokeColor())
    
    def test_getfillcolor(self):
        test_point = Point.Point(12,15)
        test_point.init_shape(10, "yellow", "pink")
        self.assertEqual("pink", test_point.getfillColor())
    
    def test_setstrokwidth(self):
        test_point = Point.Point(12,15)
        test_point.setstrokeWidth(11)
        self.assertNotEqual(10, test_point.getstrokeWidth())
    
    def test_setstrokecolor(self):
        test_point = Point.Point(12,15)
        test_point.setstrokeColor("yellow")
        self.assertEqual("yellow", test_point.getstrokeColor())
    
    def test_setfillcolor(self):
        test_point = Point.Point(12,15)
        test_point.setfillColor("yellow")
        self.assertEqual("yellow", test_point.getfillColor())
    
if __name__ == '__main__': 
     unittest.main()