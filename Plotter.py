import numpy as np
import matplotlib.pyplot as plt
from Population import new_pops
from DataStore import init_store


def plt_space(pops, ax1):
    paths = []
    for peeps in pops:
        if peeps.symp == 0:
            clr = 'green'
        elif peeps.symp == 1:
            clr = 'yellow'
        elif peeps.symp == 2:
            clr = 'red'
        else:
            clr = 'white'

        paths.append(ax1.scatter(peeps.x, peeps.y, color=clr, s=1))
    ax1.set_xlim([0, 1])
    ax1.set_ylim([0, 1])
    ax1.plot(0.7, 0.7, 'bs', markersize='4')
    ax1.tick_params(
        axis='both',  # changes apply to the both-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False,
        left=False,  # ticks along the bottom edge are off
        right=False,  # ticks along the top edge are off
        labelleft=False)
    plt.pause(0.01)
    for path in paths:
        path.remove()


# Currently not implemented
def pop_animation(life, master_pop, step_rat, iter_per_day, dis_par):

    total = [dis_par[4]]
    active = [dis_par[4]]
    recovered = [0]
    ddead = [0]
    fig, ax = plt.subplots(2, 2)
    for i in range(1, life*iter_per_day):
        if len(plt.get_fignums()) == 0:
            break
        pops, daily_data = new_pops(master_pop, step_rat, dis_par)

        # plt.subplot(2, 2, 1)
        total, active = daily_curves(daily_data, total, active)
        recovered.append(recovered[-1] + daily_data[1])
        ddead.append(ddead[-1] + daily_data[2])

        # plt.subplot(2, 2, 2)
        ax[1][0].plot(np.linspace(0, i/iter_per_day, i+1), total, color='black')
        ax[1][0].set_title('Total Cases')

        # plt.subplot(2, 2, 3)
        ax[0][1].plot(np.linspace(0, i / iter_per_day, i + 1), active, color='black')
        ax[0][1].set_title('Active Cases')

        # plt.subplot(2, 2, 4)
        ax[1][1].plot(np.linspace(0, i / iter_per_day, i + 1), ddead, color='black')
        ax[1][1].set_title('Total Dead')

        if active[-1] == 0:
            break


def pop_data(life, master_pop, step_rat, iter_per_day, dis_par):
    total = [dis_par[4]]
    active = [dis_par[4]]
    recovered = [0]
    ddead = [0]
    fig, ax = plt.subplots(2, 2)
    file_h = init_store()
    for i in range(1, life * iter_per_day):
        if len(plt.get_fignums()) == 0:
            break
        pops, daily_data = new_pops(master_pop, step_rat, dis_par)
        total, active = daily_curves(daily_data, total, active)
        recovered.append(recovered[-1] + daily_data[1])
        ddead.append(ddead[-1] + daily_data[2])

        # Writing data to file
        file_h.write(str(i / iter_per_day) + "\t" + str(total[-1]) + "\t" + str(active[-1]) + "\t" + str(
            recovered[-1]) + "\t" + str(ddead[-1]) + "\n")

        ax[0][0].plot(np.linspace(0, i / iter_per_day, i + 1), total, color='Red')
        ax[0][0].set_title('Total Cases')

        ax[1][0].plot(np.linspace(0, i / iter_per_day, i + 1), active, color='Brown')
        ax[1][0].set_title('Active Cases')

        ax[0][1].plot(np.linspace(0, i / iter_per_day, i + 1), ddead, color='black')
        ax[0][1].set_title('Total Dead')

        ax[1][1].plot(np.linspace(0, i / iter_per_day, i + 1), recovered, color='Green')
        ax[1][1].set_title('Total Recovered')

        plt.pause(0.01)

        if active[-1] == 0:
            break


def daily_curves(daily_data, total, active):
    total.append(total[-1] + daily_data[0])
    active.append(active[-1] + daily_data[0] - daily_data[1] - daily_data[2])
    return total, active