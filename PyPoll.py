# Add dependencies.
import csv
import os
# Assign variables to load and save files.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Set up candidate options, votes, results.
candidate_options = []
candidate_votes = {}
candidate_results = ""
# Set up county options, votes, results.
county_options = []
county_votes = {}
county_results = f"County Votes:"
# Winning candidate and county variables.
winning_candidate = ""
winning_county = ""
winning_count = 0
winning_percentage = 0

# Open election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Skip header row.
    headers = next(file_reader)

    for row in file_reader:
        # Count total votes.
        total_votes += 1
        # Update the candidate list and candidate votes.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        # Update the county list and county votes.
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

    for candidate_name in candidate_votes:
        # Retrieve candidate vote count, calculate vote percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Save candidate results.
        candidate_results += f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        # Update winning count, percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Winning candidate summary.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    winning_count = 0
    winning_percentage = 0
    for county_name in county_votes:
        # Retrieve county vote count, calculate vote percentage.
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Save county results.
        county_results += f"\n{county_name}: {vote_percentage:.1f}% ({votes:,})"
        # Find highest turnout county.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage            
            winning_county = f"{county_name}"

# Save election results to text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"{county_results}\n"
        f"-------------------------\n" 
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"        
        f"{candidate_results}"
        f"{winning_candidate_summary}")
    txt_file.write(election_results)

# Print election results in terminal.
print(election_results)