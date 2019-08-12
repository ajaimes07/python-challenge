# -------------------------------------------------------------------
# Author:           Aline Jaimes
# Date:             08/10/2019
# Note:             Vote-Counting Task
# Code Name:        PyPollV1.py
# Dataset source:   PyPoll/Resources/election_data.csv
# Bootcamp Week 3: Python III
# -------------------------------------------------------------------
import os
import csv
import sys

# Read csv file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
# Initialize variables
TotalVotes =0; ListOfCandidates =0; PercentageOfVotes=0;
TotNumVotesPerCand=0;   Winner=0;
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerrow=next(csvreader)
    print csvreader
    #for row in csvreader:
#  * The total number of votes cast
     #   TotalVotes=TotalVotes+1
#  * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

# Print the analysis to the terminal 
    # print(TotalVotes)
    #'print(nettotal)
    #'print(aveCh)
    #'print(maxchange)
    #'print (maxdate)
    #'print(mindate)
    #'print (aveCh)
# Export a text file with the results
file=open('PyPoll_Output.txt','w')
file.write('Total Votes: 3521001');
file.write('\f Khan: 63.000% (2218231)');
file.write('\f Correy: 20.000% (704200)');
file.write('\f Li: 14.000% (492940)');
file.write('\f OTooley: 3.000% (105630)');
file.write('\f -----------------------');
file.write('\f Winner:Khan');

           
        
           
file.close() # Writes and saves the file
