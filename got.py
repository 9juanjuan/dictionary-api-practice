import requests # makes API requests (this is a third-party module)
import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps
from characters import characters

def make_house_histogram(character_list):
    histogram = {}
    # loop through all the characters

    for person in character_list:
        # check allegiances for each person
        allegiances = person['allegiances']
        #allegiances is a list of urls
        for house in allegiances:
            if house in histogram:
                histogram[house] = histogram[house] + 1
            else:
                histogram[house] = 1
            #do something with that house
            #they look like this:
            #["https://www.anapioficeandfire.com/api/houses/143"]

    return histogram 

def pretty_print_histogram(histogram):
    for house in histogram:
        print("%s has %d members" % (house, histogram[house]))

def translate_address_to_house_name(URL):
    house_name = ''
    r = requests.get(URL)
    house_info= r.json()
    house_name = house_info['name']
    return house_name

def convert_to_nice_names(histogram):
    nice_histogram = {}

    for url in histogram:
        house_name = translate_address_to_house_name(url)
        nice_histogram[house_name] = histogram[url]
        time.sleep(0.1)

    #go through histogram keys and convert to actual house names
    return nice_histogram

ugly_histogram = make_house_histogram(characters)
pretty_histogram = convert_to_nice_names(ugly_histogram)
pretty_print_histogram(pretty_histogram)

# print(translate_address_to_house_name("https://www.anapioficeandfire.com/api/houses/143"))

# pretty_print_histogram(make_house_histogram(characters))
# print(make_house_histogram(characters))