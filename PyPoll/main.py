#Rodgers PyPoll
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # Stuff that needs to be set outside the for loop
    votescast = 0
    khancounter = 0
    correycounter = 0
    licounter = 0
    otooleycounter = 0
    
    for row in csvreader:
        # First Goal ... Total Number of Votes Cast
        votescast = votescast + 1
        otooleycounter = votescast - khancounter - correycounter - licounter
        # Second Goal ... Complete list of candidates with votes
        if str(row[2])== 'Khan':
            khancounter = khancounter + 1
        if str(row[2])== 'Correy':
            correycounter = correycounter + 1
        if str(row[2])== 'Li':
            licounter = licounter + 1
        
    # Vote percentage calculations    
    khanpercent = khancounter / votescast
    correypercent = correycounter / votescast
    lipercent = licounter / votescast
    tooleypercent = otooleycounter / votescast

    # Winner confirmation logic
    winnervotes = 0
    winnername = 'Kent'

    if khancounter > winnervotes:
        winnervotes = khancounter
        winnername = 'Khan'
    if correycounter > winnervotes:
        winnervotes = correycounter
        winnername = 'Correy'
    if licounter > winnervotes:
        winnervotes = licounter
        winnername = "Li"
    if otooleycounter > winnervotes:
        winnervotes = otooleycounter
        winnername = 'OTooley'
    # Really should have logic in here to deal with a tie
         


    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print('Election Results')
    print('------------------------------')
    print('Total Votes: ' +str(votescast))
    print('------------------------------')
    print('Candidate Results - UNDER CONSTRUCTION')
    print(f'Khan: ' + (str(khanpercent))+ '%        ' + str(khancounter) + '   Votes')
    print(f'Correy: ' + str(correypercent) + '%        ' + str(correycounter)+ '   Votes')
    print(f'Li: ' + str(lipercent) +'%        ' + str(licounter)+ '   Votes')
    print(f'OTooley: ' +str(tooleypercent) + '%        ' + str(otooleycounter) + '   Votes')
    print('------------------------------')
    print('Winner Is: ' + str(winnername) + '  with  ' + str(winnervotes) + '   Votes')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr')


