import copy
import math


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_axis(self):
        print((self.x, self.y))

    def __str__(self):
        return '%.d %.d' % (self.x, self.y)

    def __add__(self, other):
        x_axis = self.x + other.x
        y_axis = self.y + other.y
        return x_axis, y_axis


# start = Time()
# start.hour = 1
# start.minute = 30
# start.second = 45
# end = start.increment(15)
#
# time = Time(9, 10, 13)
#
# axis = Point(3, 4)
# print(axis)

# start = Time(9, 45)
# duration = Time(2, 35)
# print(start + duration)

# axis = Point(3, 4)
# add_axis = Point(3,2)
# print(axis + add_axis)
start = Time(3, 4)
print(start + 1335)