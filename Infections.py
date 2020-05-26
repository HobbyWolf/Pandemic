from random import random, randint
from Space import peep_dist


def update_infection(pops, dis_par):
    dead = 0
    patients = 0
    recov = 0
    dead_list = []
    quarantine = []
    thresh = dis_par[0]
    infec_prob = dis_par[1]
    mort_rate = dis_par[2]
    med_care = dis_par[3]
    int_per_day = dis_par[4]
    limit = 1

    for peeps in pops:
        if 0 < peeps.symp < 3:
            x1 = peeps.x
            y1 = peeps.y
            if peeps.symp == 1:
                peeps.incub = peeps.incub - 1/int_per_day
                if peeps.incub <= 0:
                    peeps.symp = 2
            else:
                peeps.deadrec = peeps.deadrec - 1/int_per_day
                peeps.quar = peeps.quar - 1/int_per_day
                if peeps.quar <= 0:
                    quarantine.append(peeps)
                if peeps.deadrec <= 0:
                    if random() < mort_rate * limit:
                        dead_list.append(peeps)
                        dead = dead + 1
                    else:
                        peeps.symp = 0
                        recov = recov + 1
            # # Changing mortality rate according to medical care load
            # if patients > med_care:
            #     limit = 4
            # else:
            #     limit = 1
            for peep2 in pops:
                if peep2.symp == 0 and peep2.reinfec == 0:
                    x2 = peep2.x
                    y2 = peep2.y
                    if peep_dist(x1, y1, x2, y2) < thresh:
                        patients = patients + 1
                        peep2.symp = randint(1, 2)
                        peep2.reinfec = 1
        if peeps.symp == 3:
            peeps.deadrec = peeps.deadrec - 1/int_per_day
            if peeps.deadrec <= 0:
                if random() < mort_rate * limit:
                    dead_list.append(peeps)
                    dead = dead + 1
                else:
                    peeps.symp = 0
                    recov = recov + 1

    # Dead
    for index in dead_list:
        pops.remove(index)
    #
    # # Quarantine
    # for index in quarantine:
    #     pops[index][2] = 3

    daily_data = [patients, recov, dead]
    return pops, daily_data
