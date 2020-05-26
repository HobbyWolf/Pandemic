from random import random, randint
from Space import update_coords
from Infections import update_infection
from Randomizer import get_angle
from numpy.random import randint as rint
import sys


class People:
    def __init__(self):
        self.x = random()
        self.y = random()
        self.ang = get_angle()
        self.cen_loc = randint(0, 1)
        self.symp = 0
        self.incub = randint(1, 14)
        self.deadrec = randint(14, 60)
        self.reinfec = 0
        self.quar = randint(1, 7)


def init_loc(pop_num, infec_pop):
    infected = rint(0, pop_num-1, infec_pop)
    pops = []
    for peeps in range(pop_num):
        pops.append(People())
    for infec in infected:
        pops[infec].symp = randint(1, 2)
        pops[infec].reinfec = 1
    return pops


def new_pops(pops, step_rat, dis_par):
    pops = update_coords(pops, step_rat)
    return update_infection(pops, dis_par)
