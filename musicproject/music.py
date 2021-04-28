import pandas as pd
import matplotlib as plt
import numpy as np

#load in CSV files
top10 = pd.read_csv("top10s.csv", index_col=0)
megas = pd.read_csv("spotify_mega.csv", index_col=0)

alldf = pd.DataFrame(pd.concat([top10, megas]).reset_index(drop=True))

print(alldf)

