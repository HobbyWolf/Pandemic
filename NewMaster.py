from Population import init_loc
from Plotter import *


def Master(pop_num, dist_pop, infected_people, nod, infec_prob, social_distancing):
    # Population parameters
    pop_num = int(pop_num)
    dist_pop = float(dist_pop)
    step_rat = 0.01     # 10 m per step
    iter_per_day = int(dist_pop/step_rat)
    iter_per_day = 10
    infected_people = int(infected_people)

    # No.of days
    nod = int(nod)

    # Disease parameters
    thresh = float(4)
    thresh = thresh/1000.
    infec_prob = float(infec_prob)
    infec_prob = infec_prob/100.0
    social_distancing = float(social_distancing)
    thresh = thresh - thresh*social_distancing/100
    mortality_rate = float(4.)
    mortality_rate = mortality_rate/100.

    # Health-care
    med_care = float(20.)
    med_care = med_care/100.0 * pop_num
    isolation = True

    dis_par = [thresh, infec_prob, mortality_rate, med_care, infected_people]

    # Initialize the population with random values
    master_pop = init_loc(pop_num, infected_people)

    pop_data(nod, master_pop, step_rat, iter_per_day, dis_par)

    plt.show()
