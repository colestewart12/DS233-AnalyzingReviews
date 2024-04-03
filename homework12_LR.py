# name 1: Cole Stewart
# name 2: Stuart Gavidia
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


class LRsentenceQuality:
    def __init__(self):
        # Initialize CountVectorizer
        self.vectorizer = CountVectorizer()
        # Initialize Logistic Regression model
        self.lr_model = LogisticRegression()

    def preprocess_data(self, data):
        # Tokenization and building vocabulary
        self.vectorizer.fit(data['text'])

    def trainLR(self, trainingData):
        # Preprocess data
        self.preprocess_data(trainingData)

        # Transform text data into vectors
        X_train = self.vectorizer.transform(trainingData['text'])
        y_train = trainingData['rating']

        # Train the Logistic Regression model
        self.lr_model.fit(X_train, y_train)

    def Quality_LR(self, sentence):
        # Transform input sentence into vector
        sentence_vector = self.vectorizer.transform([sentence])

        # Predict the quality of the sentence
        prediction = self.lr_model.predict(sentence_vector)

        # Map predicted label to output
        if prediction == 'high':
            return 1
        elif prediction == 'medium':
            return 0
        else:
            return -1


# this is for testing only
# Load training data
training_data = pd.read_csv('train_data.csv')

# Instantiate LRsentenceQuality class
obj = LRsentenceQuality()

# Train Logistic Regression model
obj.trainLR(training_data)

# Test the model with a sample sentence
s = "DATA 233 is a wonderful class!"
print("The final quality for your input using LR is " + str(obj.Quality_LR(s)))
