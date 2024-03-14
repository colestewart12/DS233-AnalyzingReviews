import csv
import random
from typing import TypeVar, List, Tuple

X = TypeVar('X')  # This is a generic type to represent a data point


def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """This function splits the data into pieces"""
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * prob)
    return data[:cut], data[cut:]


data = [n for n in range(1000)]  # List of values ranging from 0 to 1000
train, test = split_data(data, 0.75)

# Making sure the function does what we intend
# assert len(train) == 750
# assert len(test) == 250
#
# assert sorted(train + test) == data

#####################################
#    Pair input/output variables    #
#####################################

Y = TypeVar('Y')  # Represents output variables


def train_test_split(xs: List[X],
                     ys: List[Y],
                     test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    # Generate indices to be split
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)
    return ([xs[i] for i in train_idxs],
            [xs[i] for i in test_idxs],
            [ys[i] for i in train_idxs],
            [ys[i] for i in test_idxs])


##########################################
#    Making sure the code works right    #
##########################################

xs = [x for x in range(1000)]
ys = [2 * x for x in xs]
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)


# Make sure the datasets are the right lengths
# assert len(x_train) == len(y_train) == 750
# assert len(x_test) == len(y_test) == 250

# Check that data points are paired correctly
# assert all(y == 2 * x for x, y in zip(x_train, y_train))
# assert all(y == 2 * x for x, y in zip(x_test, y_test))


#################################
#    Machine learning basics    #
#################################

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


# Function to read CSV file
def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data



csv_data = read_csv_file("reviews.csv")

texts = [row['text'] for row in csv_data]
ratings = [int(row['rating']) for row in csv_data]

x_trains, x_tests, y_trains, y_tests = train_test_split(texts, ratings, 0.25)

print(x_trains, y_trains, x_tests, y_tests)
