from characters import characters
import matplotlib.pyplot as plt

jon_snow = {
        "url":"https://anapioficeandfire.com/api/characters/583",
        "name":"Jon Snow",
        "gender":"Male",
        "culture":"Northmen",
        "born":"In 283 AC",
        "died":"",
        "titles":["Lord Commander of the Night's Watch"],
        "aliases":[
                "Lord Snow",
                "Ned Stark's Bastard",
                "The Snow of Winterfell",
                "The Crow-Come-Over",
                "The 998th Lord Commander of the Night's Watch",
                "The Bastard of Winterfell",
                "The Black Bastard of the Wall",
                "Lord Crow"
                ],
        "father":"",
        "mother":"",
        "spouse":"",
        "allegiances":["https://anapioficeandfire.com/api/houses/362"],
        "books":["https://anapioficeandfire.com/api/books/5"],
        "povBooks":[
                "https://anapioficeandfire.com/api/books/1",
                "https://anapioficeandfire.com/api/books/2",
                "https://anapioficeandfire.com/api/books/3",
                "https://anapioficeandfire.com/api/books/8"
                ],
        "tvSeries":[
                "Season 1",
                "Season 2",
                "Season 3",
                "Season 4",
                "Season 5",
                "Season 6"
                ],
        "playedBy":["Kit Harington"]
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

for character in characters:
    if character["name"]== "Hot Pie":
        print (character["playedBy"])

def find_book_only_characters ():
    counter = 0
    for character in characters:
        if len(character["tvSeries"]) == 1:
            counter += 1
    return counter

print('There are %s characters that are only in the books.' % find_book_only_characters())
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
            print (character["name"])
    return counter
print (find_targ())

# Create a histogram of the houses
# find each characters allegiance number
# count the total number of allegiances for each house

def hist():
    house_tracker = {}
    for character in characters:
        if len(character["allegiances"]) < 1:
            continue
        # handle unallegianced characters
        else:
            url_parts = character["allegiances"][0].split('/')
            house_number = url_parts[-1]
            print (house_number)
            if house_number in house_tracker.keys():
                house_tracker[house_number] += 1
            else:
                 house_tracker[house_number] = 1
    print (max(house_tracker.keys()))
    # print (house_tracker)

hist()






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