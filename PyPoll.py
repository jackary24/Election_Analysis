# Data needed

#import modules
import csv
import os

file_to_load = os.path.join('desktop','Class Repository','Module 3 Python', 'Election_Analysis','Resources','election_results.csv')

file_to_save = os.path.join('desktop','Class Repository','Module 3 Python', 'Election_Analysis','Resources', 'elec_analysis.txt')

total_vote = 0
candidate_options = []
candidate_votes={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
   
    for row in file_reader:
        total_vote += 1
    
        candidate_name=row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_vote) * 100

        if (votes > winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes}).")
    print(f"-------------------------\nWinner: {winning_candidate}\nWinning Vote Count:{winning_count}\nWinning Vote Percent:{winning_percentage:.1f}%")


#1- Total of votes cast
#2- Complete list of candidates who recieved votes
#3- % of votes per candidate
#4- total # of votes per candidate
#5- The winner of popular vote

#close the file
