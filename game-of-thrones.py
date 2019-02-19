from characters import characters
import matplotlib.pyplot as plt

jon_snow = {
    "url": "https://anapioficeandfire.com/api/characters/583",
    "name": "Jon Snow",
    "gender": "Male",
    "culture": "Northmen",
    "born": "In 283 AC",
    "died": "",
    "titles": ["Lord Commander of the Night's Watch"],
    "aliases": [
        "Lord Snow",
        "Ned Stark's Bastard",
        "The Snow of Winterfell",
        "The Crow-Come-Over",
        "The 998th Lord Commander of the Night's Watch",
        "The Bastard of Winterfell",
        "The Black Bastard of the Wall",
        "Lord Crow"
    ],
    "father": "",
    "mother": "",
    "spouse": "",
    "allegiances": ["https://anapioficeandfire.com/api/houses/362"],
    "books": ["https://anapioficeandfire.com/api/books/5"],
    "povBooks": [
        "https://anapioficeandfire.com/api/books/1",
        "https://anapioficeandfire.com/api/books/2",
        "https://anapioficeandfire.com/api/books/3",
        "https://anapioficeandfire.com/api/books/8"
    ],
    "tvSeries": [
        "Season 1",
        "Season 2",
        "Season 3",
        "Season 4",
        "Season 5",
        "Season 6"
    ],
    "playedBy": ["Kit Harington"]
}

# for character in characters:
#     if (character["name"][0] == "A") and (character["name"] != ""):
#             counter +=1
# print (counter)
# for character in characters:
#     if len(character["died"]) >= 1:
#         counter +=1
#         # print (character["name"])
# print(counter)

# for character in characters:
#     for titles in character["titles"]:
#         print (max(len(titles)))

# for character in characters:
#     if character["culture"] == "Valyrian":
#         counter +=1

# print (counter)

#lets assume that we have seen no titles yet

most_titles = 0

# visit each character and see if they have more than `most_titles`

for person in characters:
    num_titles = len(person['titles'])
    if num_titles > most_titles:
        most_titles = num_titles
    # person_with_most_titles = person['name']

for person in characters:
    num_titles = len(person['titles'])
    if num_titles == most_titles:
       print ("%s has %d titles" % (person["name"], most_titles))

print("nope that's it")

# print ("%s has %d titles" % (person_with_most_titles, most_titles))



def find_hot_pie():
    for character in characters:
        if character["name"] == "Hot Pie":
            return character["playedBy"][0]
print(find_hot_pie(), "is Hot Pie")

def find_book_only_characters():
    counter = 0
    for character in characters:
        if len(character["tvSeries"]) == 1:
            counter += 1
    return counter

print('There are %s characters that are only in the books' %
      find_book_only_characters())
# 2008 characters not in TV series

# iterate through characters
# find their names
# find their last name
# make sure their last name is targaryen
# add to count if so
def find_targ():
    counter = 0
    for character in characters:
        name_array = character["name"].split()
        if name_array[-1] == "Targaryen":
            counter += 1
    return counter

print("The number of Targaryens is", find_targ())

# create a histogram of the houses
# find each characters allegiance number
# count the total number of allegiances for each house
def hist():
    house_tracker = {
        "Targaryen": 0,
        "Frey": 0,
        "Clegane": 0,
        "Winterfell": 0,
        "Tully": 0,
        "Martell": 0,
        "Greyjoy": 0,
        "Tyrell": 0,
        "Other": 0,
    }
    for character in characters:
        if len(character["allegiances"]) < 1:
            continue
        # handle unallegianced characters
        else:
            url_parts = character["allegiances"][0].split('/')
            house_number = url_parts[-1]
            if house_number == "378":
                house_tracker["Targaryen"] += 1
            elif house_number == "143":
                house_tracker["Frey"] += 1
            elif house_number == "72":
                house_tracker["Clegane"] += 1
            elif house_number == "362":
                house_tracker["Winterfell"] += 1
            elif house_number == "395":
                house_tracker["Tully"] += 1
            elif house_number == "285":
                house_tracker["Martell"] += 1
            elif house_number == "169":
                house_tracker["Greyjoy"] += 1
            elif house_number == "398":
                house_tracker["Tyrell"] += 1
            else:
                # everyone else
                # house_tracker["Other"] += 1
                continue

    plt.bar(list(house_tracker.keys()), house_tracker.values(), color='g')
    plt.show()

# hist()

# for character in characters:
#     for character["titles"] in character:
#         for title in character["titles"]:

# # print out the key names individually
# for k in jon_snow:
#     print(k)

# # print out just the values
# for k in jon_snow:
#     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))