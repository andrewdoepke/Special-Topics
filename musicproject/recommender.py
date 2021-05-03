def distance(self, songt):
    songt_pt = (songt['nrgy'], songt['dnce'], songt['acous'], songt['spch'], songt['pop'])

def __init__(self, data):
    self.data = data
    self.song = None
    self.song_pt = None

def recommend(self, song):
    self.song = song
    self.song_pt = (song['nrgy'], song['dnce'], song['acous'], song['spch'], song['pop'])

    grouped = self.data.groupby(['index'])




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
