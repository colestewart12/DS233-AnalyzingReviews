import pandas as pd

from homework12_LR import LRsentenceQuality
from homework10 import kNNsentenceQuality

test_data = pd.read_csv('test_data.csv')

lr_model_obj = LRsentenceQuality()
lr_model_obj.trainLR(pd.read_csv('train_data.csv'))

knn_model_obj = kNNsentenceQuality()
knn_model_obj.trainkNN(pd.read_csv('train_data.csv'))

correct_predictions_lr = 0
correct_predictions_knn = 0
total_predictions = len(test_data)
for index, row in test_data.iterrows():
    actual_label = 1 if row['rating'] == 'high' else 0 if row['rating'] == 'medium' else -1
    sentence = row['text']
    
    predicted_label_lr = lr_model_obj.Quality_LR(sentence)
    
    predicted_label_knn = knn_model_obj.Quality_kNN(sentence)
    predicted_label_knn = 1 if predicted_label_knn == 'high' else 0 if predicted_label_knn == 'medium' else -1

    if predicted_label_lr == actual_label:
        correct_predictions_lr += 1
    if predicted_label_knn == actual_label:
        correct_predictions_knn += 1

accuracy_lr = correct_predictions_lr / total_predictions
accuracy_knn = correct_predictions_knn / total_predictions

print(f"Logistic Regression Model Accuracy: {accuracy_lr}")
print(f"k-Nearest Neighbors Model Accuracy: {accuracy_knn}")
