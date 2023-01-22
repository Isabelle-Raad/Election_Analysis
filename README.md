# Election_Analysis

## Overview of Election Audit
In this project, we analyze a set of data for a US congressional precinct in Colorado. The generated report will:

1. find the total number of votes.
2. list the number of votes and percentage of total votes from each county.
3. report the county with the highest turnout.
4. list the number of votes and percentage of total votes for each candidate.
5. report the winning candidate, vote count, and vote percent.

The code used to generate this report can then be repurposed in order to analyze the data from and determine the results for future elections.

## Election-Audit Results
* 369,711 votes were cast during this election.
* Residents of Jefferson county cast 38,855 votes, 10.5% of the total. Residents of Denver county cast 306,055 votes, 82.8% of the total. Residents of Arapahoe county cast 24,801 votes, 6.7% of the total.
* Denver county had the highest turnout.
* Charles Casper Stockham recieved 85,213 votes, 23.0% of the total. Diana DeGette recieved 272,892 votes, 73.8% of the total. Raymon Anthony Doane recieved 11,606 votes, 3.1% of the total.
* Diana DeGette won the election with a majority of 73.8% of all votes (272,892 votes).

## Election-Audit Summary
The code used to analyze this election data can continue to be modified and repurposed for any future elections. If we were to run an analysis for a national election and wanted data on a sata-by-state basis, any instance of "county" in the code would simply need to be replaced by "state." When repurposing this script, be sure to look at the csv file that the data is being pulled from. It is imperative that the indexes of candidate and region names in the code matches the indexes of candidate and region names in the csv file.