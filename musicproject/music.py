import pandas as pd
import recommender as r
import random

def load_data(): #load the datafiles
    # load in CSV files
    top10 = pd.read_csv("top10s.csv", index_col=0)
    megas = pd.read_csv("spotify_mega.csv", index_col=0)

    #merge dataframes and reset the index
    alldf = pd.DataFrame(pd.concat([top10, megas]).reset_index(drop=True))

    #return this dataframe
    return alldf

def song_in(alldf): #take user input

    titles = alldf['title'].array #grab titles of the dataframe
    uinput = input("Enter the name of a song as best as you can:\nIf you would like recommendations from a random song, just press enter.\n")
    songind = r.closest_title(uinput, titles) #find index of song based on input
    if songind is not None:
        return alldf.iloc[songind] #return song requested
    else:
        return alldf.iloc[random.randrange(len(titles))] #return random song

def printresults(songy, recs): #pretty print results
    print("\nSome songs you may like based on the song", songy.title, "by", songy.artist, "are:")
    for x in recs.iterrows():
        print("     ", x[1]['title'], "by", x[1]['artist'])

def recommend(): #controller function
    df = load_data()
    recc = r.recommender()
    song = song_in(df)
    recs = recc.recommend(data=df, song=song)
    printresults(song, recs)

#Main:
recommend()





