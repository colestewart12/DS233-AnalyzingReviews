class TwitterPositive:
    def __init__(self):
        # do some initialization, optional
        pass

    def evaluateTweet(self, tweet):
        # please implement this function
        # input: any tweet text
        # output: a score [0,1], 0 means it is low quality and negative, 1 means it is high quality and positive

        # Define positive and negative keywords
        positive_words = ['good', 'great', 'excellent', 'awesome', 'fantastic', 'wonderful', 'friendly', 'delicious', 'tasty']
        negative_words = ['bad', 'poor', 'terrible', 'horrible', 'awful', 'gross']

        # Count occurrences of positive and negative words
        num_positive = sum(tweet.lower().count(word) for word in positive_words)
        num_negative = sum(tweet.lower().count(word) for word in negative_words)

        # Calculate the total score
        total_score = num_positive - num_negative

        # Normalize the score to a range between 0 and 1
        if total_score > 0:
            normalized_score = min(1, ((total_score / len(positive_words)) + 0.5))
        elif total_score < 0:
            normalized_score = max(0, total_score / len(negative_words))
        else:
            normalized_score = 0.5  # Neutral if no positive or negative words found

        return normalized_score


def main():
    # this is for testing only
    obj = TwitterPositive()
    if obj.evaluateTweet("DATA 233 is a wonderful class!") >= 0.5:
        print("Great, it is positive")
    else:
        print("negative")


if __name__ == "__main__":
    main()