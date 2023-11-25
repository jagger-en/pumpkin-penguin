import csv
import random

# CSV file path
csv_file_path = "medical_info.csv"

# Fixed texts to be added randomly
fixed_texts = ["Craniospinal", "Breast", "Breast Special", "Head & neck", "Abdomen", "Pelvis", "Crane","Lung","Lung special","Whole Brain"]

# Number of times to add random data
num_iterations = 100

# Read the existing data from the CSV file
with open(csv_file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the existing data into a list of rows
    rows = list(csv_reader)

# Assume you want to add data to the second column (index 1) in each row
column_index = 1

# Perform the addition in a loop for the specified number of iterations
for i in range(1, num_iterations+1):
    # Choose a random fixed text
    random_text = random.choice(fixed_texts)
    random_row_index = i
    # Add the random text to the specified column in the chosen row
    rows[random_row_index][column_index] = random_text

# Write the updated data back to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the updated rows to the CSV file
    csv_writer.writerows(rows)

print(f"Fixed texts added randomly to the CSV file in the same column for {num_iterations} iterations.")

import csv
import random

# CSV file path
csv_file_path = "medical_info.csv"

# Fixed texts to be added randomly with associated probabilities
fixed_texts_and_probabilities = [
    ("Craniospinal", 0.01),
    ("Breast", 0.25),
    ("Breast Special", 0.05),
    ("Head & neck", 0.1),
    ("Abdomen", 0.1),
    ("Pelvis", 0.18),
    ("Crane", 0.04),
    ("Lung", 0.12),
    ("Lung special", 0.05),
    ("Whole Brain", 0.1)
]

# Number of rows in the CSV file
num_rows = 100

# Read the existing data from the CSV file
with open(csv_file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the existing data into a list of rows
    rows = list(csv_reader)

# Assume you want to add data to the second column (index 1) in each row
column_index = 1

# Perform the addition for each row
for row_index in range(1,num_rows):
    # Choose randomly between fixed texts with specified probabilities
    random_data = random.choices(
        population=[text for text, _ in fixed_texts_and_probabilities],
        weights=[probability for _, probability in fixed_texts_and_probabilities]
    )[0]

    # Add the random data to the specified column in the current row
    rows[row_index][column_index] = str(random_data)

# Write the updated data back to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the updated rows to the CSV file
    csv_writer.writerows(rows)

print(f"Texts added randomly to the CSV file in the same column for each of the {num_rows} rows.")



