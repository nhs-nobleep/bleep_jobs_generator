import numpy as np
from random import randrange
from datetime import timedelta


def random_date_in_shift(shift):
    """
    :param shift: shift as a 2ple of datetime objects
    This function will return a random datetime in the shift.
    """
    start, end = shift[0], shift[1]
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_date_after_a_point(point, mu=10, sigma=2):
    """
    :param point: datetime object
    :param mu: datetime + point in minutes
    :param sigma: in minutes
    :return:
    """
    minutes = mu + sigma * np.random.randn(1)
    return point + timedelta(minutes=minutes[0])

