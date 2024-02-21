import requests
import time
import sys


def get_time(data_for_continent, data_for_city):
    time_request = requests.get(page + "/{}/{}".format(data_for_continent, data_for_city))
    time_zone = time_request.json()['datetime'].split("T")[1].split(".")[0]
    return time_zone


def clock(time_zone):
    hour = int(time_zone.split(":")[0])
    minute = int(time_zone.split(":")[1].split(":")[0])
    second = int(time_zone.split(":")[2])
    while True:
        time.sleep(1)
        print("\x1bc{}:{}:{}".format(hour, minute, second))
        if second < 59:
            second += 1
        elif second == 59:
            second = 0
            minute += 1
        elif second == 59 and minute == 59:
            second = 0
            minute = 0
            hour += 1


counter = 0
continents = {}
nations = {}
page = "https://worldtimeapi.org/api/timezone/"
endpoint = requests.get(page)

while counter < len(endpoint.json()):
    continents[endpoint.json()[counter].split("/")[0]] = 'None'
    counter += 1
continents = list(continents)
counter = 0
match sys.argv[1]:
    case "--continent":
        try:
            continent = sys.argv[2]
            city = sys.argv[4]
            request_data = get_time(continent, city)
            with open("time_zone", 'w') as store_time_zone:
                store_time_zone.write(continent + ":" + city)
            print("The current time in {}, {} is {}".format(continent, city, request_data))
            print("Current time zone was stored")
        except KeyError:
            print("Invalid arguments")
            print("That's not a valid continent/city, or the requested time-zones are not available")
            print('Use "--continents" to get a list of all available Time Zones')
        except IndexError:
            print("Invalid arguments")
            print("Enter values for both continent and city")
            print("i.e. --continent Europe --city London")
    case "--continents":
        print("Available Time Zones:\n")
        for i in endpoint.json():
            print(i)
    case "--clock":
        stored_time_zone = open("time_zone", 'r').readlines()
        current_time = get_time(stored_time_zone[0].split(":")[0], stored_time_zone[0].split(":")[1])
        clock(current_time)
    case "--help":
        print("Help:")
        print("To display time: --continent (continent) --city (city)")
        print("example: --continent Europe --city London")
        print("To display available continents and cities: --continents")
        print("To run a clock in your terminal in the stored time zone: --clock")
    case _:
        print('Invalid Arguments. Use "--help" for help')

