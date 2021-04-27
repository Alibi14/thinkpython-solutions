import copy
import math


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


class Time:
    """
        represent the time of day
        attributes, hour, minute, second
    """


time = Time()
time.hour = 61
time.minute = 59
time.second = 30


time2 = copy.copy(time)

time2.hour = 10
time2.minute = 59
time2.second = 30


def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


# pure functions


# def add_time(t1, t2):
#     sum = Time()
#     sum.hour = t1.hour + t2.hour
#     sum.minute = t1.minute + t2.minute
#     sum.second = t1.second + t2.second
#
#     if sum.second >= 60:
#         sum.second -= 60
#         sum.minute += 1
#     if sum.minute >= 60:
#         sum.minute -= 60
#         sum.hour += 1
#
#     return sum


start = Time()
start.hour = 21
start.minute = 22
start.second = 30

duration = Time()
duration.hour = 1
duration.minute = 30
duration.second = 0

# overall = add_time(start, duration)
# print_time(overall)


# def increment(time, seconds):   # modifier
#     time.second += seconds
#     minutes, time.second = divmod(seconds, 60)
#     time.hour, time.minute = divmod(minutes, 60)
#     return time
#
#
# def increment(seconds):    # implemented with pure function
#     new_time = Time()
#     new_time.second = seconds
#     minutes, new_time.second = divmod(seconds, 60)
#     new_time.hour, new_time.minute = divmod(minutes, 60)
#     return new_time


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# def add_time(t1, t2):
#     seconds = time_to_int(t1) + time_to_int(t2)
#     return int_to_time(seconds)


def increment(time, seconds):   # written using 2 functions
    seconds += time_to_int(time)
    return int_to_time(seconds)


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.hour >= 60 or time.minute >= 60:
        return False
    return True


def add_time(t1, t2):
    # if not valid_time(t1) or not valid_time(t2):
    #     raise ValueError('invalid Time object in add time')
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def mul_time(time, number):
    assert valid_time(time)
    seconds = time_to_int(time) * number
    return int_to_time(seconds)


def time_per_mile():
    race_time = Time
    race_time.hour = 1
    race_time.minute = 30
    race_time.second = 25
    distance = 14
    pace = mul_time(race_time, 1/distance)
    return pace


print_time(time_per_mile())






