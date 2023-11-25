import csv
import random

# CSV file path
csv_file_path = "medical_info.csv"

# Fixed texts to be added randomly
fixed_texts = ["Craniospinal", "Breast", "Breast Special", "Head & neck", "Abdomen", "Pelvis", "Crane","Lung","Lung special","Whole Brain"]
organs_num = len(fixed_texts)
fixed_numbers_1 = [13, 17, 20, 30]
fixed_numbers_2 = [15, 19, 25, 30]
fixed_numbers_3 = [15, 19, 25, 30]
fixed_numbers_4 = [5, 10, 15, 25,30,33,35]
fixed_numbers_5 = [1,3,5,8,10,12,15,18, 20,30]
fixed_numbers_6 = [1,3,5, 10,15, 22,23,25,28,35]
fixed_numbers_7 = [1,5,10,13,25, 30]
fixed_numbers_8 = [1,5,10, 15, 20,25, 30,33]
fixed_numbers_9 = [3, 5, 8]
fixed_numbers_10 = [5, 10, 12]

# Number of times to add random data
num_iterations = 100
column_index = 1

# Read the existing data from the CSV file
with open(csv_file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the existing data into a list of rows
    rows = list(csv_reader)

for i in range(1, num_iterations+1):
    random_row_index = i
    if rows[random_row_index][column_index] == fixed_texts[0]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_1)
    elif rows[random_row_index][column_index] == fixed_texts[1]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_2)
    elif rows[random_row_index][column_index] == fixed_texts[2]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_3)
    elif rows[random_row_index][column_index] == fixed_texts[3]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_4)
    elif rows[random_row_index][column_index] == fixed_texts[4]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_5)
    elif rows[random_row_index][column_index] == fixed_texts[5]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_6)
    elif rows[random_row_index][column_index] == fixed_texts[6]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_7)
    elif rows[random_row_index][column_index] == fixed_texts[7]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_8)
    elif rows[random_row_index][column_index] == fixed_texts[8]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_9)
    elif rows[random_row_index][column_index] == fixed_texts[9]:
        rows[random_row_index][column_index+1] = random.choice(fixed_numbers_10)







# Write the updated data back to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the updated rows to the CSV file
    csv_writer.writerows(rows)

print(f"Fixed texts added randomly to the CSV file in the same column for {num_iterations} iterations.")
