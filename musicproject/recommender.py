# Class for Popularity based Recommender System modelclass popularity_recommender_py():
def __init__(self, data, song):
    self.data = None
    self.song = None

def recommend(self, song, data):
    self.song = song
    self.data = data



# Create the popularity based recommender system model
#def create(self, train_data, user_id, item_id):

    # Get a count of user_ids for each unique song as   recommendation score
    #train_data_grouped = train_data.groupby([self.item_id]).agg({self.user_id: 'count'}).reset_index()
    #train_data_grouped.rename(columns={'user_id': 'score'}, inplace=True)
    # Sort the songs based upon recommendation score
    #train_data_sort = train_data_grouped.sort_values(['score', self.item_id], ascending=[0, 1])
    # Generate a recommendation rank based upon score
    #train_data_sort['Rank'] = train_data_sort['score'].rank(ascending=0, method='first')
    # Get the top 10 recommendations
    #self.popularity_recommendations = train_data_sort.head(10)
