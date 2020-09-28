#Rodgers PyBank

#Import the operating sytem
import os
#Import the csv module
import csv

# Path to collect file from resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Something to know that I can actually bring the file contents into Python
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    print("---k----k----k----k----k----k----k------")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    print("These months are included in the profit analysis:")
    for row in csvreader:
        print(row[0])
        #months = [row[0]]
        #for month in months
            #print(value)
            #print("Total Months: " + str(len(months)) + " ")

    print("---k----k----k----k----k----k----k------")

     