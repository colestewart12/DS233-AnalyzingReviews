import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('reviews.csv')

rating_counts = df['rating'].value_counts().sort_index()

print(rating_counts)

# Plot the bar chart
plt.figure(figsize=(8, 6))
plt.bar(rating_counts.index, rating_counts.values)
plt.title('Number of Reviews at Each Rating')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.xticks(np.arange(min(rating_counts.index), max(rating_counts.index)+1, 1.0))

plt.show()
