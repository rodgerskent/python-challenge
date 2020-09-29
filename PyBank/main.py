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
    bestname = 'Kent'
    worstname = 'Matthew'
    month2month = 0
    priormonth = 0
    
    #Loop through rows to compare and calculate    
    for row in csvreader:
        #print(row)
        count = count + 1
        monthlyprofit = int(row[1])
        netprofit = netprofit + monthlyprofit

        if count == 1:
            month2month = 0
            priormonth = int(row[1])
        
        if count >1:
            month2month = month2month + int(row[1]) - priormonth
            priormonth = int(row[1]) 
            
        if int(row[1]) > bestmonth:
            bestmonth = int(row[1])
            bestname = str(row[0])
        if int(row[1]) < worstmonth:
            worstmonth = int(row[1])
            worstname = str(row[0])

    #Output section     
    print('  ')
    print('  ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(count))
    print('Total Profit for Period: $' + str(netprofit))
    print(f'Average Monthly Change: $' + str(month2month/(count-1)))
    print(f'Greatest Increase in Profits: $' + str(bestmonth) + ' in ' + bestname)
    print(f'Greatest Decrease in Profits: $' + str(worstmonth) + ' in ' + worstname)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr")
    print('  ')
    print('  ')
     