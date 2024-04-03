from library_item import LibraryItem    # import the LibraryItem class from the library_item module

def test_library_class():     # define a function to test the LibraryItem class
    lib_item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)   # create an instance of the LibraryItem class with parameters: name, director, rating
    # perform assertions to check if the instance attributes are equal to the expected values
    assert lib_item.name == "Tom and Jerry"
    assert lib_item.director == "Fred Quimby"
    assert lib_item.rating == 4
    assert lib_item.play_count == 0
    assert lib_item.image == "Tom and Jerry.jpg"
    # call the info(), stars() methods of the instance and check if the returned value is equal to the expected value
    assert lib_item.info() == "Tom and Jerry - Fred Quimby ****\n"
    assert lib_item.stars() == "****"
