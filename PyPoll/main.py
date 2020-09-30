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
    print('Candidate Results as follows')
    print(f'Khan: ' + str(round((khanpercent*100),1)) + '%   ' + str(khancounter) + '   Votes')
    print(f'Correy: ' + str(round((correypercent*100),1)) + '%   ' + str(correycounter)+ '   Votes')
    print(f'Li: ' + str(round((lipercent*100),1)) +'%        ' + str(licounter)+ '   Votes')
    print(f'OTooley: ' + str(round((tooleypercent*100),1)) + '%   ' + str(otooleycounter) + '   Votes')
    print('------------------------------')
    print('Winner Is: ' + str(winnername) + '  with  ' + str(winnervotes) + '   Votes')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr')

    output=(f'Election Results')
    
    print(output)
    
    # Specify the file to write to
    output_path = os.path.join('Analysis', 'PyPollKMR.txt')
    #Open the output file to be written to as a text file; then write
    with open(output_path, "w") as txt_file:
        txt_file.write(output)
