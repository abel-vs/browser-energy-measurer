import drivers
from scenarios import wikipedia, amazon, google, youtube, soundcloud
from mechanisms import open_new_tab

import time
import socket
import os

def start(identifier, pid):
    print('start', pid, identifier)
    UDP_IP, UDP_PORT = 'localhost', 2000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes('start ' + str(pid) + ' ' + identifier, encoding='utf-8'), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print(data, addr)
    sock.close()

def stop(identifier):
    print('stop', identifier)
    UDP_IP, UDP_PORT = 'localhost', 2000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes('stop ' + identifier, encoding='utf-8'), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print(data, addr)
    sock.close()

def report(path):
    print('report', path)
    UDP_IP, UDP_PORT = 'localhost', 2000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes('report ' + path, encoding='utf-8'), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print(data, addr)
    sock.close()

def run(driver_fun, name_driver, measure_sec=True):
    driver = driver_fun()
    scenarios = [
        lambda: soundcloud.visit(driver),
        lambda: wikipedia.visit(driver),
        lambda: amazon.visit(driver),
        lambda: youtube.visit(driver),
        # lambda: google.visit(driver),
    ]
    if measure_sec:
        start(name_driver, driver.service.process.pid)
    for scenario in scenarios:
        scenario()
        open_new_tab(driver)
    time.sleep(1)
    if measure_sec:
        stop(name_driver)
    driver.quit()

if __name__ == '__main__':

    time.sleep(10)
    
    driver_per_name = {
        'chrome': drivers.chrome_driver,
        'firefox': drivers.firefox_driver
    }

    # warm-up
    for name_driver in driver_per_name:
        run(driver_per_name[name_driver], name_driver, measure_sec=False)

    time.sleep(30)
        
    external_iteration = 10
    internal_iteration = 3

    for i in range(0, external_iteration):
        for name_driver in driver_per_name:
            for j in range(0, internal_iteration):
                run(driver_per_name[name_driver], '-'.join([name_driver, str(i), str(j)]))
            #cool down
            time.sleep(30)

    report('/'.join([os.getcwd(), 'report.json']))