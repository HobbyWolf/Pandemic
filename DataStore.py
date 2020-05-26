import os


def init_store():
    if not os.path.isdir('Data'):
        os.mkdir('Data')
    f_daily = open("Data/DailyData.txt", "w")
    f_daily.write("------------------Run parameters--------------------\n")
    f_daily.write("Index\tTotal\tActive\tRecovered\tDead\n")
    return f_daily
