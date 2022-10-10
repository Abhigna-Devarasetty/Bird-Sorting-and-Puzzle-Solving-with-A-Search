#!/usr/local/bin/python3
# route.py : Find routes through maps
#
# Code by: name IU ID
#
# Based on skeleton code by V. Mathur and D. Crandall, Fall 2022
#


# !/usr/bin/env python3
from calendar import c
import sys
import numpy as np

def perform_data_cleansing():
    data_dict = {}
    city_list = []
    segment_list = []

    # reading the city-gps file and filling up the city list
    with open("city-gps.txt", 'r') as f:
        city_info = f.read()
        city_list = city_info.split("\n")

    # updating the data dict with latitude and longitude
    for city in city_list:
        try:
            city_details = city.split(" ")
            data_dict[city_details[0]] = {"latitude" : city_details[1], "longitude" : city_details[2], "successor_cities" : []}
        except:
            data_dict[city_details[0]] = {"latitude" : "NA", "longitude" : "NA", "successor_cities" : []}
        

    # reading the road-segments.txt file and filling the segments list
    with open("road-segments.txt", "r") as f:
        segment_info = f.read()
        segment_list = segment_info.split("\n")
    
    # search the current city in segment list and update the successor value of the data dict
    

    # segment_list = np.array(segment_list)
    for segment in segment_list:
        for city in data_dict.keys():
            result = segment.find(city)
            if result != -1:
                try:
                    segment_details = segment.split(" ")
                    successor_dict = {}
                    
                    if segment_details[0] == city:
                        successor_dict["city"] = segment_details[1]
                    elif segment_details[1] == city:
                        successor_dict["city"] = segment_details[0]
                    
                    successor_dict["distance"] = segment_details[2]
                    successor_dict["speedlimit"] = segment_details[3]
                    successor_dict["route_details"] = segment_details[4]

                    data_dict[city]["successor_cities"].append(successor_dict)
                except:
                    pass
    return data_dict

    
def get_route(start, end, cost):
    
    """
    Find shortest driving route between start city and end city
    based on a cost function.

    1. Your function should return a dictionary having the following keys:
        -"route-taken" : a list of pairs of the form (next-stop, segment-info), where
           next-stop is a string giving the next stop in the route, and segment-info is a free-form
           string containing information about the segment that will be displayed to the user.
           (segment-info is not inspected by the automatic testing program).
        -"total-segments": an integer indicating number of segments in the route-taken
        -"total-miles": a float indicating total number of miles in the route-taken
        -"total-hours": a float indicating total amount of time in the route-taken
        -"total-delivery-hours": a float indicating the expected (average) time 
                                   it will take a delivery driver who may need to return to get a new package
    2. Do not add any extra parameters to the get_route() function, or it will break our grading and testing code.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """


    data_dict = perform_data_cleansing()
    print(data_dict)
    print("WAS UNABLE TO IMPLEMENT DUE TO TIME CONSTRAINTS. IF GIVEN MORE TIME CAN DEFINATELY IMPLEMENT IT")

    # route_taken = [("Martinsville,_Indiana","IN_37 for 19 miles"),
    #                ("Jct_I-465_&_IN_37_S,_Indiana","IN_37 for 25 miles"),
    #                ("Indianapolis,_Indiana","IN_37 for 7 miles")]
    
    # return {"total-segments" : len(route_taken), 
    #         "total-miles" : 51., 
    #         "total-hours" : 1.07949, 
    #         "total-delivery-hours" : 1.1364, 
    #         "route-taken" : route_taken}


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise(Exception("Error: expected 3 arguments"))

    (_, start_city, end_city, cost_function) = sys.argv
    if cost_function not in ("segments", "distance", "time", "delivery"):
        raise(Exception("Error: invalid cost function"))

    result = get_route(start_city, end_city, cost_function)

    # Pretty print the route
    print("Start in %s" % start_city)
    for step in result["route-taken"]:
        print("   Then go to %s via %s" % step)

    print("\n          Total segments: %4d" % result["total-segments"])
    print("             Total miles: %8.3f" % result["total-miles"])
    print("             Total hours: %8.3f" % result["total-hours"])
    print("Total hours for delivery: %8.3f" % result["total-delivery-hours"])


