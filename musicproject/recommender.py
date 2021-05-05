import numpy as np
import pandas as pd
import difflib as dl
pd.options.mode.chained_assignment = None  # default='warn'

def closest_title(uinp, title):  # find index of title in the titles array closest to user input
    stri = dl.get_close_matches(uinp, title, n=1)  # get closest matched word to input
    ind = 0
    for s in title:  # figure out index of this based on if the word is in the title
        if s in stri:
            return ind
        ind += 1
    return None

def distance(self, songt): #find distance between song points with 4 axis
    songt_pt = np.array((songt['nrgy'], songt['dnce'], songt['acous'], songt['val']))

    dist = np.linalg.norm(self.song_pt - songt_pt) #euclidian distance between points

    #print(dist)
    return dist

class recommender: #recommender class to be instantiated in main function(I did it this way to try OOP in Python since I haven't really done anything this way yet)
    def __init__(self):
        self.data = None
        self.song = None
        self.song_pt = None

    def recommend(self, data, song): #recommend songs based on data and song passed
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

        return sort.head(10) #returns best 10 matches
