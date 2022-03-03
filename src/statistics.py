import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

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

# PRINT BOXPLOTS
energy_data = [chrome_cum_energy, firefox_cum_energy, edge_cum_energy]
energy_fig = plt.figure()
energy_ax = energy_fig.add_subplot(111)
energy_ax.set_title('Cumulative Energy per Browser')
energy_ax.set_ylabel('Cumulative Energy (Joules)')
energy_ax.set_xticklabels(["Chrome", "Firefox", "Edge"])
energy_bp = energy_ax.boxplot(energy_data)

power_data = [chrome_avg_power, firefox_avg_power, edge_avg_power]
power_fig = plt.figure()
power_ax = power_fig.add_subplot(111)
power_ax.set_title('Average Processor Power per Browser')
power_ax.set_ylabel('Average Processor Power (Watt)')
power_ax.set_xticklabels(["Chrome", "Firefox", "Edge"])
power_bp = power_ax.boxplot(power_data)

plt.show()
