#************************************************************************************************************************
# Print Financial Analysis
print("Financial Analysis" + '\n')
print("----------------------------")
#************************************************************************************************************************


#************************************************************************************************************************
import csv

# Place script in the same file path as csv file.
file_path = 'budget_data.csv'  

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
print('\n' + f"Total Months: {row_count}"+ '\n')
#************************************************************************************************************************


#************************************************************************************************************************
column_number_to_sum = 1  # Column number to sum (starting from the first column with a value)

# Read the file and calculate the sum of the specified column excluding the header row
with open(file_path, 'r') as file:
    lines = file.readlines()

    # Remove the header row
    header = lines[0]
    data_rows = lines[1:]

    # Extract values from the specified column and calculate the sum
    column_values = [row.strip().split(',')[column_number_to_sum] for row in data_rows]
    column_sum = sum(map(int, column_values))  # Convert strings to integers and sum them

print(f"Total: ${column_sum}" + '\n')
#************************************************************************************************************************


#************************************************************************************************************************
# Read the file and calculate the changes in profit/losses
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    values = [int(row['Profit/Losses']) for row in reader]

# Calculate the changes in profit/losses between consecutive months
changes = [values[i + 1] - values[i] for i in range(len(values) - 1)]

# Calculate the average of the changes
average_change = sum(changes) / len(changes)

# Print the average change
print(f"Average Change: ${average_change:.2f}" + '\n')
#************************************************************************************************************************

#************************************************************************************************************************
# Initialize variables to store greatest increase details
greatest_increase = 0
greatest_increase_date = ""
previous_profit = None

# Read the file and find the greatest increase in profits
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        profit = int(row['Profit/Losses'])
        if previous_profit is not None:
            increase = profit - previous_profit # Calculate increase
            
            # Check if the current increase is greater than the previous greatest increase
            if increase > greatest_increase:
                greatest_increase = increase
                greatest_increase_date = row['Date']
        
        previous_profit = profit

# Print the greatest increase in profits (date and amount)
print(f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})" + '\n')
#************************************************************************************************************************

#************************************************************************************************************************
# Initialize variables to store greatest decrease details
greatest_decrease = 0
greatest_decrease_date = ""
previous_profit = None

# Read the file and find the greatest decrease in profits
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    #previous_profit = next(reader)[1]

    for row in reader:
        profit = int(row['Profit/Losses'])
        if previous_profit is not None:
            decrease = previous_profit - profit  # Calculate decrease
            
            # Check if the current decrease is greater than the previous greatest decrease
            if decrease > greatest_decrease:
                greatest_decrease = decrease
                greatest_decrease_date = row['Date']
        
        previous_profit = profit

# Print the greatest decrease in profits (date and amount)
print(f"Greatest Decrease in Profits:  {greatest_decrease_date} (${greatest_decrease})" + '\n')
#************************************************************************************************************************

#************************************************************************************************************************
# Lines of text to be written to the file
lines = [
    "Financial Analysis",
    "----------------------------", 
    f"Total Months: {row_count}",
    f"Total: ${column_sum}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits:  {greatest_increase_date} (${greatest_increase})",
    f"Greatest Decrease in Profits:  {greatest_decrease_date} (${greatest_decrease})"
]

# Define the file path where you want to save the text file
file_path = 'output.txt'

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    # Write each line of text to the file
    for line in lines:
        file.write(line + '\n' + '\n')
#************************************************************************************************************************
