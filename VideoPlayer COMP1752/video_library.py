from library_item import LibraryItem    # Import the LibraryItem class from the library_item module.


library = {}    # This is a dictionary that stores LibraryItem objects, with the key being a string representation of the item's ID.
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)  # Add a new LibraryItem to the dictionary with the ID "01", name "Tom and Jerry", director "Fred Quimby", and rating 4.
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)   # Add a new LibraryItem to the dictionary with the ID "02", name "Breakfast at Tiffany's", director "Blake Edwards", and rating 5.
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)  # Add a new LibraryItem to the dictionary with the ID "03", name "Casablanca", director "Michael Curtiz", and rating 2.
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1) # Add a new LibraryItem to the dictionary with the ID "04", name "The Sound of Music", director "Robert Wise", and rating 1.
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)  # Add a new LibraryItem to the dictionary with the ID "05", name "Gone with the Wind", director "Victor Fleming", and rating 3.


def list_all():     # This function returns a string containing the video number and information about all LibraryItems in the library dictionary.
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}"
    return output


def get_name(key):  # This function returns the name of the LibraryItem associated with the given key in the library dictionary
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):  # This function returns the director of the LibraryItem associated with the given key in the library dictionary
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):    # This function returns the rating of the LibraryItem associated with the given key in the library dictionary
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):    # This function sets the rating of the LibraryItem associated with the given key in the library dictionary to the given rating
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):    # This function returns the number of times the LibraryItem associated with the given key in the library dictionary has been played
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def get_image(key):
    try:
        item = library[key]
        return item.image
    except KeyError:
        return None

def increment_play_count(key):  # This function increments the number of times the LibraryItem associated with the given key in the library dictionary has been played by 1
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return


