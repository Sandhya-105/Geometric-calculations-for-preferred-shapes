# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:23:46 2021

@author: SANDHYA
"""

import unittest
import Rectangle
import Point


class TestRect(unittest.TestCase):
    
    def test_gettopleftpoint(self):
        test_rect = Rectangle.Rectangle(Point.Point(11,22), 6, 7)
        rect = (test_rect.gettopleftpoint().getX(), test_rect.gettopleftpoint().getY())
        self.assertTupleEqual((11,22), rect)
        
    def test_getwidth(self):
        test_rect = Rectangle.Rectangle(Point.Point(11,22), 6, 7)
        self.assertEqual(6, test_rect.getwidth())
        
    def test_getheight(self):
        test_rect = Rectangle.Rectangle(Point.Point(11,22), 6, 7)
        self.assertEqual(7, test_rect.getheight())
        
    def test_settopleftpoint(self):
        test_rect = Rectangle.Rectangle(Point.Point(11,22), 6, 7)
        test_rect.settopleftpoint(Point.Point(19,18))
        rect = (test_rect.gettopleftpoint().getX(), test_rect.gettopleftpoint().getY())
        self.assertTupleEqual((19,18), rect)
        
    def test_setwidth(self):
        test_rect = Rectangle.Rectangle(Point.Point(11,22), 6, 7)
        test_rect.setwidth(10)
        self.assertEqual(10, test_rect.getwidth())
        
    def test_setheight(self):
        test_rect = Rectangle.Rectangle(Point.Point(11,22), 6, 7)
        test_rect.setheight(1)
        self.assertEqual(1, test_rect.getheight())
        
    def test_area(self):
        test_rect = Rectangle.Rectangle(Point.Point(10,22), 6, 7)
        Area = test_rect.area()
        self.assertEqual(42, Area)
        
    def test_perimeter(self):
        test_rect = Rectangle.Rectangle(Point.Point(10,22), 6, 7)
        Perimeter = test_rect.perimeter()
        self.assertEqual(26, Perimeter)
        
    def test_contains(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        result = test_rect.contains(Point.Point(6,7))
        self.assertTrue(result)
        
    def test_centroid(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        result = (test_rect.centroid().getX(), test_rect.centroid().getY())
        self.assertTupleEqual((8.5,10.5), result)
        
    def test_tostring(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        self.assertEqual("topleftpoint = Point (5.0,6.0) width = 7 height = 9", test_rect.toString())
        
    def test_getstrokewidth(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        test_rect.init_shape(10, "yellow", "pink")
        self.assertEqual(10, test_rect.getstrokeWidth())
    
    def test_getstrokecolor(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        test_rect.init_shape(10, "yellow", "pink")
        self.assertEqual("yellow", test_rect.getstrokeColor())
    
    def test_getfillcolor(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        test_rect.init_shape(10, "yellow", "pink")
        self.assertEqual("pink", test_rect.getfillColor())
    
    def test_setstrokwidth(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        test_rect.setstrokeWidth(11)
        self.assertNotEqual(10, test_rect.getstrokeWidth())
    
    def test_setstrokecolor(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        test_rect.setstrokeColor("yellow")
        self.assertEqual("yellow", test_rect.getstrokeColor())
    
    def test_setfillcolor(self):
        test_rect = Rectangle.Rectangle(Point.Point(5,6), 7, 9)
        test_rect.setfillColor("yellow")
        self.assertEqual("yellow", test_rect.getfillColor())
        
if __name__ == '__main__': 
     unittest.main()