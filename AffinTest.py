
import json
from colorama import Fore, Back, Style

# initialize afinn sentiment analyzer
from afinn import Afinn

af = Afinn()

# data from TripAdvisor
museum_data_file_path = '/Users/madelineholt/CSclasses/Sentiment-Analysis/Data/review_quotes.json'
with open(museum_data_file_path, 'r') as json_obj:
    museum = json.loads(json_obj.read()).values()
    # convert to list of lists
    museum2 = list(museum)
    # convert to just list of reviews
    museum_reviews = []
    for i in range(len(museum2)):
        for item in museum2[i]:
            museum_reviews.append(item)


# compute sentiment scores (polarity) and labels

sentiment_scores = []
for reviews in museum_reviews:
    sentiment_scores.append(af.score(reviews))
print(type(sentiment_scores[0]))

sentiment_category = ['positive' if score > 0
                      else 'negative' if score < 0
                        else 'neutral'
                            for score in sentiment_scores]

# for i in range(len(museum_reviews)):
#     if sentiment_scores[i] > 0.0:
#         print(Fore.LIGHTGREEN_EX + "Review: " + '"' + str(museum_reviews[i]) + '"' + " Sentiment Score: " + str(sentiment_scores[i]))
#     if sentiment_scores[i] < 0.0:
#         print(Fore.RED + "Review: " + '"' + str(museum_reviews[i]) + '"' + " Sentiment Score: " + str(sentiment_scores[i]))
#     if sentiment_scores[i] == 0.0:
#         print(Fore.WHITE + "Review: " + '"' + str(museum_reviews[i]) + '"' + " Sentiment Score: " + str(
#             sentiment_scores[i]))

for i in sentiment_scores:
    print(i)