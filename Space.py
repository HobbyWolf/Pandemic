import numpy as np
from Randomizer import get_xy, get_angle
from random import random
from math import atan
from numpy import pi


def update_coords(pops_1, step_rat):
    cent_x = 0.7
    cent_y = 0.7
    for peeps_1 in pops_1:
        x = peeps_1.x
        y = peeps_1.y
        if random() < 0 and peeps_1.cen_loc == 0:
            redir = get_supermarket_angle(x, y, cent_x, cent_y)
            ang = redir
            peeps_1.cen_loc = 1
        else:
            ang = peeps_1.ang
        dx, dy, angle, flag = check_boundary(x, y, ang, step_rat, 0)
        if flag == 1:
            peeps_1.den_loc = 0
        peeps_1.ang = angle
        peeps_1.x = peeps_1.x + dx
        peeps_1.y = peeps_1.y + dy
    return pops_1


def peep_dist(x1, y1, x2, y2):
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)


def check_boundary(x, y, ang, step_rat, flag):
    dx, dy = get_xy(ang, step_rat)
    tempx = x + dx
    tempy = y + dy
    if tempx < 0 or tempy < 0 or tempy > 1 or tempx > 1:
        ang = get_angle()
        return check_boundary(x, y, ang, step_rat, 1)
    else:
        return dx, dy, ang, flag


def get_supermarket_angle(x, y, cent_x, cent_y):
    frac = (cent_y - y)/(cent_x - x)
    redir = atan(frac)*180/pi
    if cent_x - x < 0:
        redir = (180 + redir)*pi/180
        return redir
    else:
        return redir*pi/180

