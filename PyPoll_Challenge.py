"""PyPoll Homework Challenge Solution."""

import csv
import os

file_to_load = os.path.join('desktop','Class Repository','Module 3 Python', 'Election_Analysis','Resources','election_results.csv')
file_to_save = os.path.join('desktop','Class Repository','Module 3 Python', 'Election_Analysis','Resources', 'elec_analysis.txt')

total_votes = 0
candidate_options = []
candidate_votes = {}
county_list= []
county_votes={}
largest_county=""
largest_county_count=0
largest_county_percent = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1

        candidate_name = row[2]

        county_name = row[1]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        if county_name not in county_list:

            county_list.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        cvotes = county_votes[county_name]
        cpercentage= float(cvotes)/float(total_votes)*100

        county_results=(f'{county_name}: {cpercentage:.1f}% ({cvotes:,})\n')

        print(county_results)
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cvotes > largest_county_count) and (cpercentage > largest_county_percent):
            largest_county_count = cvotes
            largest_county_percent = cpercentage
            largest_county = county_name

        largest_county_summary= (
            f"---------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"---------------------------\n"
        )
    print(largest_county_summary)
    txt_file.write(largest_county_summary)
    
    for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
