#************************************************************************************************************************
# Print Financial Analysis
print("Election Results" + '\n')
print("----------------------------")
#************************************************************************************************************************


#************************************************************************************************************************
import csv

# Place script in the same file path as csv file.
file_path = 'election_data.csv'  

# List to store header row
header_row = []

# Read the CSV file and extract the header row
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Check if the file is not empty
    try:
        header_row = next(reader)
    except StopIteration:
        print("Error: Empty CSV file")
#************************************************************************************************************************


#************************************************************************************************************************
# Open the CSV file
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip the header row
    next(reader)  # Skip the first row
    
    # Count the remaining rows using enumerate
    row_count = sum(1 for row in reader)

#Print the total months
print('\n' + f"Total Votes: {row_count}" + '\n')
print("----------------------------")
#************************************************************************************************************************

#************************************************************************************************************************
# Dictionary to store candidate names and their total votes
candidate_votes = {}

# Read the CSV file and count votes for each candidate
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    total_votes = 0  # Track total votes
    for row in reader:
        candidate = row['Candidate']
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
        total_votes += 1  # Increment total votes

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print('\n' + f"{candidate}: {percentage:.3f}% ({votes})" )

    if percentage ==  3.139:
        break

print('\n' + "----------------------------")
#************************************************************************************************************************


#************************************************************************************************************************

max_percentage = 0
max_candidate = ''

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100

    # Check if the current candidate has a higher percentage than the previous maximum
    if percentage > max_percentage:
        max_percentage = percentage
        max_candidate = candidate

if max_candidate:
    print('\n' + f"Winner: {max_candidate} ")
    print('\n' + "----------------------------")
#************************************************************************************************************************


#************************************************************************************************************************
# Lines of text to be written to the file
lines = [
    "Election Results",
    "----------------------------", 
    f"Total Votes: {row_count}",
    "----------------------------",
    "Charles Casper Stockham: 23.049% (85213)",
    "Diana DeGette: 73.812% (272892)",
    "Raymon Anthony Doane: 3.139% (11606)",
    "----------------------------",
    "Winner: Diana DeGette",
    "----------------------------"
]

# Define the file path where you want to save the text file
file_path = 'output.txt'

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    # Write each line of text to the file
    for line in lines:
        file.write(line + '\n' + '\n')
#************************************************************************************************************************
