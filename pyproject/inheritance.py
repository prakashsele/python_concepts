# create to files Telugu_movie and International_movies
# International_movies can inherit Telugu_movie

from Telugu_movie import OnlyTeluguMovies
from International_movies import Allmovies

movies = OnlyTeluguMovies()
movies.Bahubhali()

alMoviesc = Allmovies()
alMoviesc.Magadheera()

