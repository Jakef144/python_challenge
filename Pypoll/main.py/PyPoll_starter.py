# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Get the absolute path of the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..", "analysis", "election_analysis.txt")  # Output file path #10/6 come back and fix #working now? no changes 10/08


# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = {}  # Dictionary to store candidate names and vote counts
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print and write the total vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n" #Does this generate the dots?
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n" #Does this generate the dots?
    )
    print(election_results)
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:
        # Get the vote count and calculate the percentage
        votes = candidates[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {(winning_count / total_votes) * 100:.3f}%\n"
        f"-------------------------\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)
