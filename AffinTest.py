
import json

# initialize afinn sentiment analyzer
from afinn import Afinn

af = Afinn()

# data from TripAdvisor
museum_data_file_path = '/Users/madelineholt/CSclasses/Sentiment-Analysis/Data/review_quotes.json'
with open(museum_data_file_path, 'r') as json_obj:
    museum_reviews = json.loads(json_obj.read())

# compute sentiment scores (polarity) and labels
sentiment_scores = [af.score(reviews) for reviews in museum_reviews]
sentiment_category = ['positive' if score > 0
                      else 'negative' if score < 0
                        else 'neutral'
                            for score in sentiment_scores]

# still need to visualize data here for comaparison