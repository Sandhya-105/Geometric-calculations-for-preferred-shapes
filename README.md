# Lab4 - ISP

## Purpose
* To generate a point, circle and rectangle of any given parameters using specified styling operations.
* To perform geometric calculations( Area, Perimeter, Centroid, Contains ) using the generated shape of choice

## Functionality
### Point class 
Here, this code can help you to create a point object, we can set and get the points(x,y).
We can calculate distances between 2 points and we can print a statement stating the point created.

### Rectangle class
The code is used to create rectangle by specifying a point, width and height parameters. 
It has methods to calculate area, perimeter and centroid of the custom rectangle. It has setters and getters method to create/ update the parameters.
We can also get to know if the given point are enclosed within the given rectangle using contains method.
Finally, we can print a statement stating the rectangle created using toString method.

### Circle class
The code is used to create circle by specifying a centerpoint and radius parameters. 
It has setters and getters method to create/ update the parameters.
It has methods to calculate area, perimeter of the given circle.
We can also get to know if the given point are enclosed within the given circle using contains method.
Finally, we can print a statement stating the circle created using toString method.

### Shape class
> Point, Circle and Rectangle class all inherit the Shape class

The shape class has three parameters : strokewidth, strokecolor and fillcolor
It has both setters and getters method for each parameter and can be used to style the generated user-defined shape.

Unittest- TestCase class has been used to test all the methods of the class point, circle, rectangle as well as inherited methods of class shape.

## Usage

``` python
import Point
# create a point object 
point = Point.Point(10,12)
# distance calculation
dist = point.distance(12,13)
# To print a statement of the created point
statement = point.toString()
```

``` python
import Rectangle
import Point
# create a rectangle object
rectangle = Rectangle.Rectangle(Point.Point(11, 9), 3, 7)
# area, perimeter and centroid calculation
perimeter = rectangle.perimeter()
area = rectangle.area()
rectangle.centroid()
# To check whether a given point is within the given rectangle
rectangle.contains(Point.Point(12, 10))
# To print a statement of the created rectangle
statement = rectangle.toString()
```

```python
import Circle
import Point
# create a circle object
circle = Circle.Circle(Point.Point(0,9), 2)
# area and perimeter calculation
area = circle.area()
perimeter = circle.perimeter()
# To check whether a given point is inside the given circle
circle.contains(Point.Point(1, 6))
# To print a statement of the created circle
statement = circle.toString()
# To set a fillcolor for the generated circle
circle.setfillcolor("blue")
# To get a fillcolor for the generated circle
circle.getfillcolor()
```
