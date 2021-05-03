import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def distance(self, songt):
    songt_pt = np.array((songt['nrgy'], songt['dnce'], songt['acous'], songt['val']))

    dist = np.linalg.norm(self.song_pt - songt_pt)

    #print(dist)
    return dist

class recommender:
    def __init__(self):
        self.data = None
        self.song = None
        self.song_pt = None

    def recommend(self, data, song):
        self.song = song #set song
        self.data = data #set data
        #get rid of current song from our data
        self.data = data[data.title != song.title].reset_index().drop_duplicates(subset='title', keep="last")

        #generate datapoint for song to make recommendations off of
        self.song_pt = np.array((song['nrgy'], song['dnce'], song['acous'], song['val']))

        #generate similarity scores
        simi = self.data
        simi['similarity'] = self.data.apply(lambda row: distance(self, row), axis=1)

        #sort by smallest similarity
        sort = simi.sort_values('similarity', ascending=True)

        return sort.head(10)
