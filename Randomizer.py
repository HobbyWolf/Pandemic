import numpy as np
from random import random


def get_angle():
    temp = random()
    ang = temp*np.pi*2
    return ang


def get_dist(step_rat):
    return random()*step_rat


def get_xy(angle, step_rat):
    dist = get_dist(step_rat)
    dx = dist*np.cos(angle)
    dy = dist*np.sin(angle)
    return dx, dy
