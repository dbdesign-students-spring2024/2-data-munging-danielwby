#1
# Reading file contents
with open("data\GLB.Ts+dSST.txt", "r") as file:
    lines = file.readlines()

# Remove comment lines that start with "#"
cleaned_lines = [line for line in lines if not line.startswith("#")]

# Write the cleaned data to a new file
cleaned_file_path = "f1.txt"
with open(cleaned_file_path, "w") as cleaned_file:
    cleaned_file.writelines(cleaned_lines)

#2
# Reading file contents
with open("f1.txt", "r") as file:
    lines = file.readlines()

# Define the column header row, assuming it appears repeatedly
column_header = "Year   Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec    J-D D-N    DJF  MAM  JJA  SON  Year\n"

# Create a new list, including the first line of the file
cleaned_lines_with_single_header = [lines[0]]  # 假设第一行不是列标题

# Iterate over the rest of the file and add only non-column header rows
for line in lines[1:]:
    if line != column_header:
        cleaned_lines_with_single_header.append(line)

# Write the cleaned data to a new file
cleaned_file_path_with_single_header = "f2.txt"
with open(cleaned_file_path_with_single_header, "w") as cleaned_file:
    cleaned_file.writelines(cleaned_lines_with_single_header)

#3
# Reading file contents
with open("f2.txt", "r") as file:
    lines = file.readlines()

# Filter out blank lines (including lines containing only Spaces)
cleaned_lines_no_empty = [line for line in lines if line.strip()]

# Write the cleaned data to a new file
cleaned_file_path_no_empty = "f3.txt"
with open(cleaned_file_path_no_empty, "w") as cleaned_file:
    cleaned_file.writelines(cleaned_lines_no_empty)

#4
# Reading file contents
with open("f3.txt", "r") as file:
    lines = file.readlines()

# Replace "****" with "NaN" and leave "***" unchanged
cleaned_lines_corrected_missing_values = [line.replace('****', 'NaN') for line in lines]

# Write the processed data to a new file
corrected_file_path = "f4.txt"
with open(corrected_file_path, "w") as corrected_file:
    corrected_file.writelines(cleaned_lines_corrected_missing_values)

###5
# Read the contents of the file after handling missing values
with open("f4.txt", "r") as file:
    lines = file.readlines()

# Process the temperature values on each row, multiply by 0.018, and format the result with one decimal place
scaled_and_formatted_lines = []
for line in lines:
    parts = line.strip().split()
    if len(parts) > 2:  # Make sure there is a temperature value for processing
        # Process the temperature values, leaving the year column unchanged
        processed_temps = []
        for temp in parts[1:-1]:  # Iterate over the temperature values other than the year
            try:  # Try converting and manipulating temperature values
                scaled_temp = float(temp) * 0.018
                formatted_temp = '{:.1f}'.format(scaled_temp)
                processed_temps.append(formatted_temp)
            except ValueError:  # If the conversion fails, the original value is kept
                processed_temps.append(temp)
        processed_line = f"{parts[0]} {' '.join(processed_temps)} {parts[-1]}\n"
    else:
        # If there is no temperature value in the row, it is included as is
        processed_line = line
    scaled_and_formatted_lines.append(processed_line)

# Write the processed data to a new file
processed_file_path = "f5.txt"
with open(processed_file_path, "w") as processed_file:
    processed_file.writelines(scaled_and_formatted_lines)

#6
# Read the contents of a formatted file
with open("f5.txt", "r") as file:
    lines = file.readlines()

# Convert to CSV format, using commas as a separator
csv_lines = []
for line in lines:
    parts = line.strip().split()
    csv_line = ",".join(parts) + "\n"
    csv_lines.append(csv_line)

# Write the CSV data to a new file
csv_file_path = "data\clean_data.csv"
with open(csv_file_path, "w") as csv_file:
    csv_file.writelines(csv_lines)

#Delete files produced by the intermediate process
import os
# Define the path of the file to delete
file_path1 = "f1.txt"
file_path2 = "f2.txt"
file_path3 = "f3.txt"
file_path4 = "f4.txt"
file_path5 = "f5.txt"

try:
    # Call the os module's remove() function to delete the file
    os.remove(file_path1)
    os.remove(file_path2)
    os.remove(file_path3)
    os.remove(file_path4)
    os.remove(file_path5)
except FileNotFoundError:
    print("The specified file does not exist！")
except Exception as e:
    print("Other errors occurred:", str(e))
