from Population import new_pops
import os


def data_store(life, master_pop, step_rat, iter_per_day, dis_par):
    if not os.path.isdir('TLol'):
        os.mkdir('TLol')

    total = [dis_par[4]]
    active = [dis_par[4]]
    recovered = [0]
    ddead = [0]
    f_daily = open("TLol/DailyData.txt", "w")
    f_daily.write("------------------Run parameters--------------------\n")
    f_daily.write("Index\tTotal\tActive\tRecovered\tDead\n")
    for i in range(1, life*iter_per_day):
        f_daily.write(str(i/iter_per_day)+"\t"+str(total[-1])+"\t"+str(active[-1])+"\t"+str(recovered[-1])+"\t"+str(ddead[-1])+"\n")
        pops, daily_data = new_pops(master_pop, step_rat, dis_par)

        total, active = daily_curves(daily_data, total, active)
        recovered.append(recovered[-1] + daily_data[1])
        ddead.append(ddead[-1] + daily_data[2])
        if active[-1] == 0:
            break


def daily_curves(daily_data, total, active):
    total.append(total[-1] + daily_data[0])
    active.append(active[-1] + daily_data[0] - daily_data[1] - daily_data[2])
    return total, active
