# https://aihub.cloud.google.com/u/0/p/products%2F21c6f397-2099-4c54-ba78-0f93cdc13e7b


# negative and positive words are surrounded by synonyms
# ---> find groups of negative or positive words
import json
import multiprocessing
# import Word2Vec as Word2Vec

# data from TripAdvisor
museum_data_file_path = '/Users/madelineholt/CSclasses/Sentiment-Analysis/Data/review_quotes.json'
with open(museum_data_file_path, 'r') as json_obj:
    museum_reviews = json.loads(json_obj.read())


# word2vec used to finding groups of similar words
# w2v_model = Word2Vec(min_count=3,
#                      window=4,
#                      size=300,
#                      sample=1e-5,
#                      alpha=0.03,
#                      min_alpha=0.0007,
#                      negative=20,
#                      workers=multiprocessing.cpu_count()-1)


