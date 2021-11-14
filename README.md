# Election Analysis

## Project Overview
An employee from the Colorado Board of Elections has given the following tasks to complete the election audit of a recent local congressional elections. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes recieved by each candidate. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visula Studio Code, 1.38.1

## Summary
The analysis of the election:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockton
    - Diana DeGette
    - Raymon Anthony Doane

- The Counties voting were:
    - Araphoe, with 24,801 voters (6.7% of the total vote).
    - Denver, with 306,055 voters (82.8% of the total vote).
    - Jefferson, with 38,855 voters (10.5% of the total vote).
    
- The individual candidate results were:
    - Charles Casper Stockton recieved 23.0% of the total vote, 85,213 votes in total.
    - Diana DeGette recieved 73.8% of the total vote, 272,892 votes in total.
    - Raymon Anthony Doane recieved 3.1% of the total vote, 11,606 votes in total.
    
- The winner of the election was:
    - Candidate Diana DeGette, who recieved 73.8% of the total vote, 272,892 votes in total.

## Challenge Summary

   This code can be expanded from its current version, and used in any number of election, from schoolboard to presidential. The use of for loops to determine the county name, candidate name, and total votes means that we could cover large data sets, without knowing all participants in the race, or even counties participating. Additionally the speed at which python is able to analyze such a large data set with accuracy (and without bias) make it an ideal tool to adopt in an election of any kind. 
   
   One potential change they are able to make would having a conditional if statement included in case, like in this race, one candidate pulls away and is a clear winner. This could potentially reduce the amount of time the code needs to run, making it more efficient. Another addition to the code would be to include the percentage each candidate recieved per county. This could help determine the issues each individual county cares about, by seeing which candidate they support, helping determine those issues that affect residents of those counties.  
