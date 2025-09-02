import csv

## Read the following CSV about Australia states and territories
# Add a new header "Capital" and add the capital city for each state/territory
# write to the same CSV file
# Extra fun: calculate the total population of Australia

rows = []
with open("australia.csv", "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(rows)

## add new header
header=['Capital']
cities = ['Melbourne', 'Sydney', 'Adelaide', 'Perth', 'Hobart','Brisbane', 'Canberra', 'Darwin']

with open('australia.csv', 'w', newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()

    for capital in cities:
        writer.writerow({'Capital': cities[1]})


