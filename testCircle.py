# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:06:49 2021

@author: SANDHYA
"""

import unittest
import Circle
import Point

class TestCircle(unittest.TestCase):
    
    def test_getcenterpoint(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        result = (test_circle.getcenterpoint().getX(),test_circle.getcenterpoint().getY())
        self.assertTupleEqual((1,2), result)
        
    def test_getradius(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        self.assertEqual(4, test_circle.getradius())
        
    def test_setcenterpoint(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.setcenterpoint(Point.Point(2,1))
        result = (test_circle.getcenterpoint().getX(),test_circle.getcenterpoint().getY())
        self.assertTupleEqual((2,1), result)
        
    def test_setradius(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.setradius(2)
        self.assertEqual(2, test_circle.getradius())
        
    def test_area(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        result = test_circle.area()
        self.assertAlmostEqual(50.265, result, 3)
        
    def test_perimeter(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        result = test_circle.perimeter()
        self.assertAlmostEqual(25.133, result, 3)
        
    def test_contains(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        result = test_circle.contains(Point.Point(2,2))
        self.assertTrue(result)
        
    def test_toString(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        self.assertEqual("centerpoint = Point (1.0,2.0) radius = 4", test_circle.toString())
    
    def test_getstrokewidth(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.init_shape(10, "yellow", "pink")
        self.assertEqual(10, test_circle.getstrokeWidth())
    
    def test_getstrokecolor(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.init_shape(10, "yellow", "pink")
        self.assertEqual("yellow", test_circle.getstrokeColor())
    
    def test_getfillcolor(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.init_shape(10, "yellow", "pink")
        self.assertEqual("pink", test_circle.getfillColor())
    
    def test_setstrokwidth(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.setstrokeWidth(11)
        self.assertNotEqual(10, test_circle.getstrokeWidth())
    
    def test_setstrokecolor(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.setstrokeColor("yellow")
        self.assertEqual("yellow", test_circle.getstrokeColor())
    
    def test_setfillcolor(self):
        test_circle = Circle.Circle(Point.Point(1,2), 4)
        test_circle.setfillColor("yellow")
        self.assertEqual("yellow", test_circle.getfillColor())
        
if __name__ == '__main__': 
     unittest.main()