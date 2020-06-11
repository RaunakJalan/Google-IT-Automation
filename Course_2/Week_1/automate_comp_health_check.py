#!/usr/bin/env python3

import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage("/")
    free = du.free/du.total * 100

    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)

    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")

else:
    print("Everything is OK!")

#disk usage
du = shutil.disk_usage("/")
print("Disk Usage: ",du)
disk_free_space = du.free/du.total * 100
print("Free Disk Space % : ",disk_free_space)
##
#cpu usage
cpu_usage = psutil.cpu_percent(0.5) #0.1 is interval
print("CPU Usage: ",cpu_usage)


