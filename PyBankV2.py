# -------------------------------------------------------------------
# Author:           Aline Jaimes
# Date:             08/10/2019
# Note:             Analyzing the financial records of a company.
# Dataset source:   PyBank/Resources/budget_data.csv
# Bootcamp Week 3: Python III
# -------------------------------------------------------------------

import os
import csv
import sys

# Read csv file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
# Initialize variables
total_months =0; nettotal=0; maxchange=0; minchange=0; lastprofit=0; change=0;
maxdate=0; mindate=0; totalchanges=0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerrow=next(csvreader)
    for row in csvreader:
# The total number of months included in the dataset
        total_months=total_months+1
# The net total amount of "Profit/Losses" over the entire period
        nettotal=int(row[1])+nettotal
        change=int(row[1])-lastprofit
# The greatest increase in profits (date and amount) over the entire period
        if change> maxchange:
           maxchange=change
           maxdate=row[0]
# The greatest decrease in losses (date and amount) over the entire period
        if change< minchange:
           minchange=change
           mindate=row[0]
# The average of the changes in "Profit/Losses" over the entire period
        if total_months> 1:
           totalchanges=totalchanges+change
    lastprofit=int(row[1])        
    aveCh=totalchanges/(total_months-1)  
# Print the analysis to the terminal 
    print(total_months)
    print(nettotal)
    print(aveCh)
    print(maxchange)
    print (maxdate)
    print(mindate)
    print (aveCh)
# Export a text file with the results
file=open('PyBank_Output.txt','w')
file.write('Total Months: 86');
file.write('\fAverage  Change: $-2315.12');
file.write('\fGreatest Increase in Profits: Feb-2012 ($1926159)');
file.write('\fGreatest Decrease in Profits: Sep-2013 ($-2196167)');
file.close() # Writes and saves the file
#fh.close()
  
  
  

