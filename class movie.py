class movie:
    def __init__(self, movie_title , director , rating):
        self.movie_title=movie_title
        self.director=director
        self.rating=rating

    def display(self):
        print("the movie title is",self.movie_title)
        print("the director of movie is",self.director)
        print("the ratings of movie is",self.rating)

    def check(self):
        if self.rating>8.0:
            print("the movie is blockbaster")
        else:
            print("the movie is flop")

obj1=movie("siddat","kunal_deshmukh",7.6)
obj1.display()
obj1.check()
