#Rodgers PyPoll September 2020

# Import required operating system and formats
import os
import csv

# Import the election data file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
 
    # Build a list of candidates to ensure we know full list and format issues that may exist
    namelist = []
    for candidatexx in csvreader:
        if not candidatexx[2] in namelist: 
            namelist.append(candidatexx[2])
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print('Candidate list ...')
    print(namelist)
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    
    # Run each line through a loop to capture votes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    # Capture variables
    votescast = 0
    khancounter = 0
    correycounter = 0
    licounter = 0
    otooleycounter = 0

    for row in csvreader:
        # Tally votes cast
        votescast = votescast + 1
        otooleycounter = votescast - khancounter - correycounter - licounter
        # Capture vote tally by candidate
        if str(row[2])== 'Khan':
            khancounter = khancounter + 1
        if str(row[2])== 'Correy':
            correycounter = correycounter + 1
        if str(row[2])== 'Li':
            licounter = licounter + 1
        
    # Tally vote percentage    
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
    
    # Terminal report-out section
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print('Election Results')
    print('------------------------------')
    print('Total Votes: ' +str(votescast))
    print('------------------------------')
    print('Candidate Results as follows:')
    print(f'Khan: ' + str(round((khanpercent*100),1)) + '%   ' + str(khancounter) + '   Votes')
    print(f'Correy: ' + str(round((correypercent*100),1)) + '%   ' + str(correycounter)+ '   Votes')
    print(f'Li: ' + str(round((lipercent*100),1)) +'%        ' + str(licounter)+ '   Votes')
    print(f'OTooley: ' + str(round((tooleypercent*100),1)) + '%   ' + str(otooleycounter) + '   Votes')
    print('------------------------------')
    print('Winner Is: ' + str(winnername) + '  with  ' + str(winnervotes) + '   Votes')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr~~terminal')

    # Text file report-out section
    output=(
    f'Election Results\n'
    f'------------------------------\n'
    f'Total Votes: {str(votescast)} \n'
    f'------------------------------\n'
    f'Candidate Results as follows:\n'
    f'Khan: {str(round((khanpercent*100),1))} % {str(khancounter)} Votes \n'
    f'Correy: {str(round((correypercent*100),1))} % {str(correycounter)}   Votes\n'
    f'Li: {str(round((lipercent*100),1))} %  {str(licounter)} Votes\n'
    f'OTooley: {str(round((tooleypercent*100),1))} % {str(otooleycounter)} Votes\n'
    f'------------------------------\n'
    f'Winner Is: {str(winnername)} with {str(winnervotes)} Votes\n'
    f' \n'
    f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~kmr~~textfile')
    
    print(output)
    
    # Specify the file to write to
    output_path = os.path.join('Analysis', 'PyPollKMR.txt')
    #Open the output file to be written to as a text file; then write
    with open(output_path, "w") as txt_file:
        txt_file.write(output)

    # kmr PyPoll end
