from ..database import database
from ..database import queries

#A new Predictor object is instantiated for each user
class Predictor:

    #store id's for liked and disliked songs
    likes = []
    #dislikes = []

    def suggest_song(self):
           