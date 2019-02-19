#!/usr/bin/env python3
"""
This module takes a time value as an argument,
suspends the machine, wakes up at the  given timepoint
and starts playing some music.
"""

import os
import math
import sys
import datetime
import time
import subprocess

def check_uid():
    """Check if user has root permission, else abort"""
    if os.geteuid() != 0:
        print("This program requires running as root or \n"
              "elevated privileges, please rerun with 'sudo !!'")
        sys.exit()

check_uid()

def get_wakeuptime():
    """ Define Time (HH:MM where the device should wake up) """
    try:
        wakeup = sys.argv[1]
    except IndexError:
        wakeup = input("Please define a wakeuptime HH:MM" + '\n')
    return wakeup

def calc_wakeupdate(wakeuptime): #pylint: disable-msg=R0914
    """ Calculate the timedelta between wakeuptime and current time"""

    current_epoch = time.time()
    current_year = time.localtime()[0]
    current_month = time.localtime()[1]
    current_day = time.localtime()[2]
    current_hour = time.localtime()[3]
    current_minutes = time.localtime()[4]
    current_seconds = time.localtime()[5]

    current_date = (
        current_year,
        current_month,
        current_day,
        current_hour,
        current_minutes,
        current_seconds
        )

    wakeup_epoch = time.time() + 24 * 3600
    wakeuptime_split = wakeuptime.split(':')

    #Assume same day wakeup"
    wakeup_year = time.localtime()[0]
    wakeup_month = time.localtime()[1]
    wakeup_day = time.localtime()[2]
    wakeup_hour = int(wakeuptime_split[0])
    wakeup_minutes = int(wakeuptime_split[1])
    wakeup_seconds = 0

    wakeup_epoch = datetime.datetime(
        wakeup_year,
        wakeup_month,
        wakeup_day,
        wakeup_hour,
        wakeup_minutes
        ).strftime('%s')

#    If wakeup time is in the past add 1 day
    if float(wakeup_epoch) <= float(current_epoch):
        wakeup_epoch = float(wakeup_epoch) + 24 * 3600
    print("Final wakeup_epoch: " + str(wakeup_epoch))

    #Generate date form epoch
    wakeup_year = time.localtime(int(wakeup_epoch))[0]
    wakeup_month = time.localtime(int(wakeup_epoch))[1]
    wakeup_day = time.localtime(int(wakeup_epoch))[2]
    wakeup_hour = int(wakeuptime_split[0])
    wakeup_minutes = int(wakeuptime_split[1])
    wakeup_seconds = time.localtime(int(wakeup_epoch))[5]

    wakeup_date = (
        wakeup_year,
        wakeup_month,
        wakeup_day,
        wakeup_hour,
        wakeup_minutes,
        wakeup_seconds
        )

    deltatime = float(wakeup_epoch) - float(current_epoch)

    if deltatime > (24 * 3600):
        deltatime = deltatime - (24 * 3600)

    deltahours = math.floor(deltatime / 3600)
    deltatime = deltatime - deltahours * 3600
    deltaminutes = math.floor(deltatime / 60)
    print("Current Date: " + str(current_date))
    print("Wakeup Date:  " + str(wakeup_date))
    print()
    print("Time till wakeup: " + str(deltahours) + ":" + str(deltaminutes))

    return wakeup_date

def bash(command):
    """Run a standard bash command"""
    subprocess.Popen(['/bin/bash', '-c', command])

def rtcwake(wakeup_date):
    """Hibernate and wake up the device, then start playing music"""
    date = str(wakeup_date[0]).zfill(4)+str(wakeup_date[1]).zfill(2)+str(wakeup_date[2]).zfill(2)
    clock = str(wakeup_date[3]).zfill(2)+str(wakeup_date[4]).zfill(2)+str(wakeup_date[5]).zfill(2)
    print(date + clock)
    bash('sudo rtcwake -v -m mem --date ' + date + clock)
    bash('mpc play')

rtcwake(calc_wakeupdate(get_wakeuptime()))
