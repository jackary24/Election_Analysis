# Data needed

#import modules
import csv
import os

file_to_load = os.path.join('desktop','Class Repository','Module 3 Python', 'Election_Analysis','Resources','election_results.csv')

file_to_save = os.path.join('desktop','Class Repository','Module 3 Python', 'Election_Analysis','Resources', 'elec_analysis.txt')

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
        #print(row)

#1- Total of votes cast
#2- Complete list of candidates who recieved votes
#3- % of votes per candidate
#4- total # of votes per candidate
#5- The winner of popular vote

#close the file
