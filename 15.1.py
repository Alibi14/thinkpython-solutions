import copy
import math


class Point:
    """just point
    """


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


class Circle:
    """
        Represent a circle
        attributes: center(x,y), radius.

    """


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


class Rectangle():
    """Represent a circle
        attributes: width, height, corner.
"""


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 50.0

circle = Circle()
circle.center = Point()
circle.center.x = 150
circle.center.y = 100
circle.radius = 75


def distance_between_points(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    print(dist)
    return dist


def point_in_circle(circle1, point):
    d = distance_between_points(circle1, point)
    return d <= circle.radius


print(point_in_circle(box.corner, circle.center))


def rect_circle_overlap(rect, circle):
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False




