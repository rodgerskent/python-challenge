#Rodgers PyPoll
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # Stuff that needs to be set outside the for loop
    votescast = 0

    for row in csvreader:
        # First Goal ... Total Number of Votes Cast
        votescast = votescast + 1

        # Second Goal ... Votes cast by candidate
        
        

    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print('Election Results')
    print('------------------------------')
    print('Total Votes: ' +str(votescast))
    print('------------------------------')
    print('Candidate Results - UNDER CONSTRUCTION')
    print('------------------------------')
    print('Winner: - UNDER CONSTRUCTION')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr')


