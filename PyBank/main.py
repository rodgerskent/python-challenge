#Rodgers PyBank September 2020

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
        
    # Counters for average monthly gain or loss
    month2month = 0
    priormonth = 0
       
    # Counters for greatest/worst gain/loss
    greatestname = 'Winner'
    worstname = 'Losser'
       
    #Loop through rows to compare and calculate    
    for row in csvreader:
        count = count + 1
        monthlyprofit = int(row[1])
        netprofit = netprofit + monthlyprofit

        if count == 1:
            # Average monthly change counters
            month2month = 0
            priormonth = int(row[1])
            
            # Greatest monthly change counters
            greatestprior = int(row[1])
            greatestgain = 0
            greatestaward = 0

            # Worst monthly change counters
            worstprior = int(row[1])
            worstgain = 0
            worstaward = 0

        if count >1:
            month2month = month2month + int(row[1]) - priormonth
            priormonth = int(row[1]) 

        if count >1: 
            greatestgain = int(row[1]) - greatestprior 
            greatestprior = int(row[1])
            if greatestgain > greatestaward:
                greatestaward = greatestgain
                greatestname = str(row[0])               

        if count >1: 
            worstgain = int(row[1]) - worstprior 
            worstprior = int(row[1])
            if worstgain < worstaward:
                worstaward = worstgain
                worstname = str(row[0])

    #Report-out section     
    print('  ')
    print('  ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(count))
    print('Total Profit for Period: $' + str(netprofit))
    print(f'Average Monthly Change: $' + str(month2month/(count-1)))
    print(f'Greatest Increase in Profits: $' + str(greatestaward) + ' in ' + greatestname)
    print(f'Greatest Decrease in Profits: $' + str(worstaward) + ' in ' + worstname)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr")
    print('  ')
    print('  ')


    # Lines to push the text information out to a text file
    # Specify what it is we want to output
    output=(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    f'Financial Analysis\n'
    f'----------------------------'
    f'Total Months: ${str(count)} \n'
    f'Total Profit for Period: ${str(netprofit)} \n'
    f'Average Monthly Change: ${str(month2month/(count-1))} \n'
    f'Greatest Increase in Profits: ${str(greatestaward)}  in {greatestname} \n'
    f'Greatest Decrease in Profits: ${str(worstaward)} in {worstname} \n'
    f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr')
        
    print(output)
    
    # Specify the file to write to
    output_path = os.path.join('Analysis', 'PyBankKMR.txt')
    #Open the output file to be written to as a text file; then write
    with open(output_path, "w") as txt_file:
        txt_file.write(output)

    # kmr End