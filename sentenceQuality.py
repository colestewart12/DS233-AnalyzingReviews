# name 1: Cole Stewart
# name 2: Stuart Gavidia

from textblob import TextBlob


class sentenceQuality():
    def __init__(self):
        # do some initialization, optional
        pass

    def calculateScores(self, tweet):
        # please implement this function input: any tweet text output: a list of scores for the tweet,
        # it must include: score for length, score for Polarity, score for Subjectivity, and at least one score of
        # the following: https://en.wikipedia.org/wiki/Automated_readability_index
        # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
        # https://en.wikipedia.org/wiki/Gunning_fog_index https://en.wikipedia.org/wiki/SMOG
        # https://en.wikipedia.org/wiki/Fry_readability_formula
        # https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index You should implement at least one score
        blob = TextBlob(tweet)
        characters = 0
        words = len(blob.words)
        sentences = len(blob.sentences)
        for char in tweet:
            characters += 1
        readability = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
        l = (characters / words) * 100
        s = (sentences / words) * 100
        coleman_liau_index = 0.0588 * l - 0.296 * s - 15.8
        subjectivity = blob.sentiment.subjectivity
        polarity = blob.sentiment.polarity
        return [readability, subjectivity, polarity, words, coleman_liau_index]

    def calculateQuality(self, scores):
        # please implement this function to calculate a final quality score between 0 and 1
        # Input: a list of scores, which is the output of calculateScores
        # output: 0 means low quality, 1 mean high quality

        readability = scores[0]
        subjectivity = scores[1]
        polarity_score = scores[2]
        # Get value between 0 and 1
        polarity = (polarity_score + 1.0) / 2.0
        words = scores[3]
        coleman_liau_index = scores[4]

        # High school level
        max_readability = 10
        max_subjectivity = 1.0
        max_polarity = 1.0
        max_coleman_liau_index = 20.0  # most values will be under 20
        # Maxes out at 100 words, everything higher will get 100
        max_words = 100.0

        normalized_readability = min(max(readability / max_readability, 0), 1)
        normalized_subjectivity = min(max(subjectivity / max_subjectivity, 0), 1)
        normalized_polarity = min(max(polarity / max_polarity, 0), 1)
        normalized_words = min(max(words / max_words, 0), 1)
        normalized_coleman_liau_index = min(max(coleman_liau_index / max_coleman_liau_index, 0), 1)

        weight_readability = 0.2
        weight_subjectivity = 0.3
        weight_polarity = 0.2
        weight_words = 0.1
        weight_coleman_liau_index = 0.2

        overall_score = (
                weight_readability * normalized_readability +
                weight_subjectivity * normalized_subjectivity +
                weight_polarity * normalized_polarity +
                weight_words * normalized_words +
                weight_coleman_liau_index * normalized_coleman_liau_index
        )

        return overall_score


# this is for testing only
obj = sentenceQuality()
s = "DATA 233 is a wonderful class!"

print("The scores for your input is " + str(obj.calculateScores(s)))

print("The final quality for your input is " + str(obj.calculateQuality(obj.calculateScores(s))))
