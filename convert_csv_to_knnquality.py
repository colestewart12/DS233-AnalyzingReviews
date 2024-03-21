import csv


# Define function to categorize ratings
def categorize_rating(ratings):
    if ratings <= 1.7:
        return 'low'
    elif ratings <= 3.3:
        return 'medium'
    else:
        return 'high'


# Open original CSV file
with open('reviews.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = list(reader)
    header = rows[0]
    data = rows[1:]

# Identify index of the column containing ratings
rating_index = header.index('rating')

# Update ratings and create new rows
updated_rows = []
for row in data:
    rating = float(row[rating_index])
    category = categorize_rating(rating)
    updated_row = row[:rating_index] + [category] + row[rating_index+1:]
    updated_rows.append(updated_row)

# Write updated data to a new CSV file
with open('rating_categories.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(updated_rows)

print("CSV file updated successfully!")
