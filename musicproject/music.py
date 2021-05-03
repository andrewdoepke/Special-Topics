import pandas as pd
import recommender as r

#load in CSV files
top10 = pd.read_csv("top10s.csv", index_col=0)
megas = pd.read_csv("spotify_mega.csv", index_col=0)

alldf = pd.DataFrame(pd.concat([top10, megas]).reset_index(drop=True))
songy = alldf.iloc[2]

recc = r.recommender()

recs = recc.recommend(data=alldf, song=songy)

#print(recs[['title', 'artist']].to_string(index=False))
print("\nSome songs you may like based on the song", songy.title, "by", songy.artist, "are:")
for r in recs.iterrows():
    print("     ",r[1]['title'], "by", r[1]['artist'])





