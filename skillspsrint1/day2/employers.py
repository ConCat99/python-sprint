import  csv
from collections import namedtuple

rows = []

# with open ("employers.csv", "r", newline="") as csvfile:
#
#     csvreader = csv.reader(csvfile) # reading files
#     header = next(csvreader) #establishing what headers are
#     for row in csvreader: # normal loop
#         rows.append(row)
#
# print(f"Headers are : {header}")
# print(rows)

# ## WRITE TO CSV
# # csv writer() -> create the object that we are going to write into the csv for data to be added
#
# header =['Name', 'Age']
# data =[['Alex', 25 ], ['Brad', 30], ['Joey', 18]]
#
# with open ('students_info.csv', 'w', newline="") as csvfile: # we've created the CSV writer object that we can now write to, W flag means we open in write mode
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(header) #method in order to add the header as our first row
#     csvwriter.writerows(data) #writerows to add in our data
#
# ## DICT
# It creates an object that  operates like a regular reader, but maps the information into each row to a dictionary whose keys are  given by the optional field names parameters. So essentially we're representing a slightly different data type

# with open('employers.csv', newline="") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print (row['Name'], row['email']) # now headers are acting like keys in a dict so that we can reference it
#         print(row)

##Write to csv file using Dictwriter
# headers = ['Name', 'Age']
# data = [['Alex', 25 ], ['Brad', 30], ['Joey', 18]]
#
# with open('students_info.csv', 'w', newline=' ') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=headers)
#
#     writer.writeheader()
#     for student in data:
#         writer.writerow({'Name': student[0], 'Age' : student[1] })
#     #transposing the 2D array into a dict format, this is useful for when we don't have control of where the data's coming from

##namedtuple() - when importing a file, we can cast incoming data to it for easier reading (optional). Similar to accessing json files in js
#
# with open('employers.csv', 'r') as csv_file:
#     reader= csv.reader(csv_file)
#     employee = namedtuple('Employee', next(reader), rename=True)
#     for row in reader:
#         employee = employee(*row)
#         print(employee.Name, employee.Position, employee.email)
#

## --------------MVP----------------
# Read the following CSV about Australia states and territories
# Add a new header "Capital" and add the capital city for each state/territory
# write to the same CSV file
# Extra fun: calculate the total population of Australia


