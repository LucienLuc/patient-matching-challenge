import algorithm
import csv

data = []
with open("Patient Matching Data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

data = data[1:-1]
#Returns array of groups where each group is an array of matching patients 
result = algorithm.groupByConfidenceScore(data,0.68)

#Output formatted as <Our Group#>:<PatientID>
counter = 1
for groups in result:
    for patient in groups:
        print("Group" + str(counter) + ": " + patient[1])
    counter += 1
