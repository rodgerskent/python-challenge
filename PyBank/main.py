#Rodgers PyBank

#Import the operating sytem
import os
#Import the csv module
import csv

# Path to collect file from resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open file for interpretation and calculations 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    count = 0
    netprofit = 0
    bestmonth = 0
    worstmonth= 0
    
    #Loop through rows to compare and calculate    
    for row in csvreader:
        #print(row)
        count = count + 1
        monthlyprofit = int(row[1])
        netprofit = netprofit + monthlyprofit
        if int(row[1]) > bestmonth:
            bestmonth = int(row[1])
        if int(row[1]) < worstmonth:
            worstmonth = int(row[1])


    #Output section     
    print('  ')
    print('  ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(count))
    print('Total Profit for Period: $' + str(netprofit))
    print('Average Monthly Change: $ ... UNDER CONSTRUCTION')
    print('Greatest Increase in Profits: $' + str(bestmonth))
    print('Greatest Decrease in Profits: $' + str(worstmonth))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr")
    print('  ')
    print('  ')
     