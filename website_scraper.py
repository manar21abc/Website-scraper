import time

start_time = time.time()
from datetime import datetime

now0 = datetime.now()
import requests

import re

import winsound

import urllib3

urllib3.disable_warnings()

my_list = []
link_list = []
total_response_time = 0
response_count = 0
limit = 0
vip_count = 0
date_list = []
viplist = []

while True:
    try:
        try:
            url = "https://appointment.visafg.com/calendar/3?month=2022-02"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=5, verify=False)
            response_time = response.elapsed.total_seconds()
            total_response_time = total_response_time + response_time
            response_count = response_count + 1
        except Exception as error_1:
            print("URL Error:", error_1)
            print()
            winsound.Beep(300, 2000)
            continue
        count_list = re.findall("'fa fa-user'></i> ([0-9]+)", response.text)

        date_list1 = re.findall('color:;"><strong>([0-9]+)</strong>', response.text)
        date_list2 = re.findall('success;"><strong>([0-9]+)</strong>', response.text)
        if len(date_list1) != 0:
            for element1 in date_list1:
                date_list.append(element1)
        if len(date_list2) != 0:
            for element2 in date_list2:
                date_list.append(element2)
        for date, count in zip(date_list, count_list):
            if count != "0":
                my_list.append(date)
                my_list.append(count)
        if len(my_list) == 0:
            now1 = datetime.now()
            if limit > 1:
                print("no of iteration while open: ", limit)
            if limit == 1 or limit == 2:
                vip_count = vip_count + 1
                limit = 0
            print("Nope", str(now1)[11:23], "V.3 Feb | VIP:", vip_count)
            continue
        else:
            now5 = datetime.now()
            print("OPEN NOW", str(now5)[11:23])
            print(my_list)
            if my_list[1] == "1":
                viplist.append(my_list[0])
            winsound.Beep(1500, 200)
            my_list = []
            date_list = []
            limit = limit + 1
            continue
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        winsound.Beep(1000, 500)
        break
finish_time = time.time()
total_time = finish_time - start_time


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


now4 = datetime.now()
average_response_time = total_response_time / response_count
average_cycle_time = total_time / response_count
average_processing_time = average_cycle_time - average_response_time
print()
print("                Start at:", str(now0)[11:23])
print("               Finish at:", str(now4)[11:23])
print("              Total time:", convert(total_time))
print()
print("   Total time in seconds:", total_time)
print("          response count:", response_count)
print()
print("   Average response time:", str(average_response_time)[0:5])
print(" Average processing time:", str(average_processing_time)[0:5])
print("      Average cycle time:", str(average_cycle_time)[0:5])
print()
print("no of iteration while open: ", limit)
print("vip dates", viplist)
print()
input()
