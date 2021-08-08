#!/usr/bin/env python3
import psutil
from check_connectivity import *


def check_disk_usage(disk):
    du = psutil.disk_usage(disk)
    free_in_percent = du.free / du.total * 100
    return free_in_percent > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!!")
elif check_connectivity() and check_localhost():
    print("Everything is OK!")
else:
    print("Network connection error!!!")
