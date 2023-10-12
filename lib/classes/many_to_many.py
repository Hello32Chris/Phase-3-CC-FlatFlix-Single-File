from statistics import mean

class Movie:

    all = []

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else: 
            raise Exception

    def reviews(self):
        return [review for review in Review.all if review.movie is self]

    def reviewers(self):
        return list({review.viewer for review in self.reviews()})

    def average_rating(self):
        ratings = [review.rating for review in self.reviews()]
        return round(mean(ratings), 1) if ratings else None
    
    # ^^^ it seems all we did here was pull out all of the ratings and round the mean of them all to the first decimal place

class Review:

    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.all.append(self)

    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else: 
            raise Exception

    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else: 
            raise Exception

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 0 < rating < 6 and not hasattr(self, 'rating'):
            self._rating = rating
        else: 
            raise Exception
        
class Viewer:

    all = []

    def __init__(self, username):
        self.username = username
        Viewer.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 5 < len(username) < 17:
            self._username = username
        else: 
            raise Exception

    def reviews(self):
        return [review for review in Review.all if review.viewer is self]

    def reviewed_movies(self):
        return list({review.movie for review in self.reviews()})

    def has_reviewed_movie(self, movie):
        if movie in self.reviewed_movies():
            return True
        else:
            return False

    def add_review(self, movie, rating):
        return Review(self, movie, rating)