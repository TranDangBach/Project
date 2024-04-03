class LibraryItem:  # This line defines a class named LibraryItem
    def __init__(self, name, director, rating=0):   # This is the constructor method for the LibraryItem class
        # These lines initialize the instance variables 'name', 'director', 'rating', and 'play_count'
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.image = f"{name}.jpg"

    def info(self):     # This method returns the name, director, and rating of the LibraryItem as a string
        return f"{self.name} - {self.director} {self.stars()}\n"

    def stars(self):    # This method generates a string of '*' based on the rating of the LibraryItem
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
