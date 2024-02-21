import requests
import time

page = "https://worldtimeapi.org/api/timezone/"


def get_time(data_for_continent, data_for_city):
    time_request = requests.get(page + "/{}/{}".format(data_for_continent, data_for_city))
    time_zone = time_request.json()['datetime'].split("T")[1].split(".")[0]
    return time_zone


def clock(continent, city, time_zone):
    hour = int(time_zone.split(":")[0])
    minute = int(time_zone.split(":")[1])
    second = int(time_zone.split(":")[2])
    while True:
        if second < 59:
            second += 1
        elif second == 59 and minute != 59:
            second = 0
            minute += 1
        elif second == 59 and minute == 59:
            second = 0
            minute = 0
            hour += 1
        time.sleep(1)
        if second < 10:
            print("\x1bTime Zone: {}, {} - Current Time:\n{}:{}:{:02d}".format( continent, city, hour, minute, second))
        if second < 10 and minute < 10:
            print("\x1bcTime Zone: {}, {} - Current Time:\n{}:{:02d}:{:02d}".format( continent, city, hour, minute, second))
        else:
            print("\x1bcTime Zone: {}, {} - Current Time:\n{}:{:02d}:{:02d}".format( continent, city, hour, minute, second))
