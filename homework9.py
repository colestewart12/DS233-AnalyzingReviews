import csv
import random
from typing import TypeVar, List, Tuple

X = TypeVar('X')  # Generic type to represent a data point
Y = TypeVar('Y')  # Represents output variables

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Splits data into two parts: a training set and a testing set."""
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * prob)
    return data[:cut], data[cut:]

def train_test_split(xs: List[X], ys: List[Y], test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    """Splits both input (X) and output (Y) data into training and testing sets based on test_pct."""
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)
    return ([xs[i] for i in train_idxs],
            [xs[i] for i in test_idxs],
            [ys[i] for i in train_idxs],
            [ys[i] for i in test_idxs])

def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total


# assert accuracy(70, 4930, 13930, 981070) == 0.98114


def precision(tp: int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp + fp)


# assert precision(70, 4930, 13930, 981070) == 0.014


def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp + fn)

# assert recall(70, 4930, 13930, 981070) == 0.005

def read_csv_file(filename: str) -> Tuple[List[str], List[int]]:
    texts = []
    ratings = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            texts.append(row['text'])
            ratings.append(int(row['rating']))
    return texts, ratings

csv_data = read_csv_file("rating_categories.csv")

texts = [row['text'] for row in csv_data]
ratings = [(row['rating']) for row in csv_data]

x_trains, x_tests, y_trains, y_tests = train_test_split(texts, ratings, 0.25)


# Write train data to CSV
with open('train_data.csv', 'w', newline='', encoding='utf-8') as train_csv_file:
    writer = csv.writer(train_csv_file)
    writer.writerow(['text', 'rating'])  # Write header
    for text, rating in zip(x_trains, y_trains):
        writer.writerow([text, rating])

# Write test data to CSV
with open('test_data.csv', 'w', newline='', encoding='utf-8') as test_csv_file:
    writer = csv.writer(test_csv_file)
    writer.writerow(['text', 'rating'])  # Write header
    for text, rating in zip(x_tests, y_tests):
        writer.writerow([text, rating])

print("CSV files created successfully.")
