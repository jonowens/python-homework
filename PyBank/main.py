# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# -*- coding: utf-8 -*-

# %% [markdown]
# # PyBank Budget Assistance
# 
# ### Description: 
# * The following task is to help PyBank analyze their financial information.  A budget_data.csv file
# has been provided with two sets of data: Date and Profit/Loss for the given month.  The following code 
# below will analyze and calculate various metrics along with providing an output of the analysis to the screen and a summary.txt file found in the Resources directory of the repository.
# 

# %%
# Import necessary libraries
from pathlib import Path
import csv
import budgpy as bgy


# %%
# Initialize data structure to store information from csv
budget = []
# Initialize metric variables
number_of_months = 0
net_total_amount_of_profits_and_losses = 0
change_in_profits_and_losses_list = []
average_of_profit_and_losses = 0
greatest_increase_of_profits_dictionary = {}
greatest_decrease_of_losses_dictionary = {}
number_of_profits_and_losses = 0
net_total_amount_of_profits_and_losses = 0
total_sum_of_profit_and_loss_changes = 0


# %%
# Capture file path to be read
csvpath = Path("./Resources/budget_data.csv")

# Open data in specified path as csv_file 
with open(csvpath, 'r') as csv_file:

    # Read data from csv_file knowing the data is ',' delimited and assign to csvreader variable
    csvreader = csv.reader(csv_file, delimiter=',')

    # Store data header
    header = next(csvreader)

    # Iterate through each line of csvreader
    for row in csvreader:
        # Assign each row to dictionary structure
        first_item = row[0]
        second_item = int(row[1])
        # Assign dictionary data items to budget list
        # "pnl" represents Profit and Loss
        budget.append({'date': first_item, 'pnl': second_item})


# %%
# The total number of months included in the dataset.
number_of_months_in_budget = len(budget)


# %%
# The net total amount of Profit/Losses over the entire period.

# To track the next month count
next_month_index = 1

# Loop through budget list to build change of profit and loss list
for item in budget:
    
    #Determine if there is a next month variable available to compare with current month data
    if next_month_index < len(budget):
    
        # Calculate profit or lose from current month to next month
        change_value = budget[next_month_index]["pnl"] - item["pnl"]

        # Assign profit or loss change to list of dictionaries using 'date' and 'pnl' indicies
        change_in_profits_and_losses_list.append({'date': budget[next_month_index]["date"], 'pnl': change_value})

        # Increment count to track next month place holder
        next_month_index += 1

# Add and accumulate a total of all profit and losses
net_total_amount_of_profits_and_losses = bgy.calculate_sum(budget, "pnl")


# %%
# The average of the changes in Profit/Losses over the entire period.

# Number of profits and losses
number_of_profits_and_losses = len(change_in_profits_and_losses_list)

# Add and accumulate a total running sum of profit and loss changes
total_sum_of_profit_and_loss_changes = bgy.calculate_sum(change_in_profits_and_losses_list, "pnl")

# Calculate the average of profits and losses
average_of_profit_and_losses = total_sum_of_profit_and_loss_changes / number_of_profits_and_losses

# Round the average of profit and losses to two places after the decimal and reassign value
average_of_profit_and_losses = round(average_of_profit_and_losses, 2)


# %%
# Determines the greatest increase in profits (date and amount) over the entire period and assigns the return values
greatest_increase_of_profits_dictionary = bgy.greatest_increase_or_decrease_in_profits(change_in_profits_and_losses_list, "increase")


# %%
# Determine the greatest decrease in losses (date and amount) over the entire period and assigns the return values
greatest_decrease_of_losses_dictionary = bgy.greatest_increase_or_decrease_in_profits(change_in_profits_and_losses_list, "decrease")


# %%
# Pass metric values into summary_output() and output to screen a summary message along with a summary.txt file
bgy.summary_output(number_of_months_in_budget, net_total_amount_of_profits_and_losses, average_of_profit_and_losses, greatest_increase_of_profits_dictionary, greatest_decrease_of_losses_dictionary)


# %%



