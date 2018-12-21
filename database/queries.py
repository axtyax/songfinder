#essentially just query templates specific to this database architecture 

import database

def get_song_likes(songid):
    database.db_query("SELECT * IN songs")