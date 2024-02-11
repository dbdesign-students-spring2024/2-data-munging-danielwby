import csv
file_path = 'data\clean_data.csv'

# Used to store the sum and count of temperature anomalies for each decade
decade_sums = {}
decade_counts = {}

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row['Year'])
        jd = float(row['J-D'])

        # Temperature anomaly that converts Celsius to Fahrenheit
        jd_f = jd * 9 / 5

        # Calculate the decade
        decade = (year // 10) * 10

        # Accumulate temperature anomalies and counts for each decade
        if decade not in decade_sums:
            decade_sums[decade] = 0
            decade_counts[decade] = 0
        decade_sums[decade] += jd_f
        decade_counts[decade] += 1

# Calculate and print the average temperature anomaly for each decade
for decade in sorted(decade_sums.keys()):
    average_anomaly = decade_sums[decade] / decade_counts[decade]
    print(f"{decade} to {decade + 9}: {average_anomaly:.3f}°F")
