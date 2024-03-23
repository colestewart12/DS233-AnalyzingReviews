# name 1: Cole Stewart
# name 2: Stuart Gavidia

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class kNNsentenceQuality():
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.kNNmodel = KNeighborsClassifier(n_neighbors=3)

    def trainkNN(self, trainingData):
        texts = trainingData['text'].values
        ratings = trainingData['rating'].map({'low': -1, 'medium': 0, 'high': 1}).values
        
        tfidf_texts = self.vectorizer.fit_transform(texts)
        self.kNNmodel.fit(tfidf_texts, ratings)

    def Quality_kNN(self, sentence):
        tfidf_sentence = self.vectorizer.transform([sentence])
        
        prediction = self.kNNmodel.predict(tfidf_sentence)
        
        return prediction[0]

trainingData = pd.read_csv('train_data.csv')

obj = kNNsentenceQuality()
obj.trainkNN(trainingData)

s = "DATA 233 is a wonderful !"
quality = obj.Quality_kNN(s)

quality_mapping = {-1: 'low', 0: 'medium', 1: 'high'}
print("The final quality for your input using kNN is " + quality_mapping[quality])