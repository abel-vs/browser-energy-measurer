import pandas as pd
import numpy as np
import os

relative_path = '../30 runs/'

files = [f for f in os.listdir(relative_path)]


def is_browser(filename, browser):
    if browser in filename and "run_0" not in filename:
        return True
    return False


def extract_number(reader):
    lst = reader.to_numpy()[0][0]
    return float([i for i in lst.split()][-1])


def get_stats(lst):
    avg = np.mean(lst)
    var = np.var(lst)
    std = np.std(lst)
    p95 = np.percentile(lst, 95)
    p99 = np.percentile(lst, 99)
    p100 = np.percentile(lst, 100)
    stats = f'Mean: {avg} | Variance: {var} | Standard deviation: {std} | p95: {p95} | p99: {p99} | p100: {p100}\n'
    return stats


chrome_files = list(filter(lambda x: is_browser(x, "chrome"), files))
firefox_files = list(filter(lambda x: is_browser(x, "firefox"), files))
edge_files = list(filter(lambda x: is_browser(x, "edge"), files))

# get statistics for chrome
chrome_cum_energy = []
chrome_avg_power = []

for f in chrome_files:
    read = pd.read_csv(os.path.join(relative_path, f))

    cum_energy = extract_number(read[-12:-11])
    avg_power = extract_number(read[-10:-9])

    chrome_cum_energy.append(cum_energy)
    chrome_avg_power.append(avg_power)

# get statistics for firefox
firefox_cum_energy = []
firefox_avg_power = []

for f in firefox_files:
    read = pd.read_csv(os.path.join(relative_path, f))

    cum_energy = extract_number(read[-12:-11])
    avg_power = extract_number(read[-10:-9])

    firefox_cum_energy.append(cum_energy)
    firefox_avg_power.append(avg_power)

# get statistics for Edge
edge_cum_energy = []
edge_avg_power = []

for f in edge_files:
    read = pd.read_csv(os.path.join(relative_path, f))

    cum_energy = extract_number(read[-12:-11])
    avg_power = extract_number(read[-10:-9])

    edge_cum_energy.append(cum_energy)
    edge_avg_power.append(avg_power)


with open("outputs.txt", "w") as w:
    w.write("\nChrome stats for 30 runs:\n")
    w.write("Cumulative energy (Joules)\n")
    w.write(get_stats(chrome_cum_energy))
    w.write("Avg processor power (Watt)\n")
    w.write(get_stats(chrome_avg_power))

    w.write("\nFirefox stats for 30 runs:\n")
    w.write("Cumulative energy (Joules)\n")
    w.write(get_stats(firefox_cum_energy))
    w.write("Avg processor power (Watt)\n")
    w.write(get_stats(firefox_avg_power))

    w.write("\nEdge stats for 30 runs:\n")
    w.write("Cumulative energy (Joules)\n")
    w.write(get_stats(edge_cum_energy))
    w.write("Avg processor power (Watt)\n")
    w.write(get_stats(edge_avg_power))

w.close()
