#!/usr/bin/python3
import sys
from pathlib import Path
from clock_module import get_time
from clock_module import clock

directory = str(Path(__file__).parent)

match sys.argv[1]:
    case "--continent":
        try:
            continent = sys.argv[2]
            city = sys.argv[4]
            request_data = get_time(continent, city)
            with open(directory + "/time_zone", 'w') as store_time_zone:
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

    case "--clock":
        try:
            stored_time_zone = open(directory + "/time_zone", 'r').readlines()
            continent = stored_time_zone[0].split(":")[0]
            city = stored_time_zone[0].split(":")[1]
            current_time = get_time(continent, city)
            clock(continent, city, current_time)
        except IndexError:
            print("No Time Zone was stored.")
            print("Please run with arguments '--continent' and '--city' to store a requested time zone.")
            print("Ending.")

    case "--help":
        print("Help:")
        print("To display time: --continent (continent) --city (city)")
        print("example: --continent Europe --city London")
        print("To display available continents and cities: --continents")
        print("To run a clock in your terminal in the stored time zone: --clock")

    case _:
        print('Invalid Arguments. Use "--help" for help')
