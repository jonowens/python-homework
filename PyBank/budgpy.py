# The following defined functions are used to assist in the output and calculations for budget metric compilations.
# Please use Python 3.8.5 and import the following library shown below.

from pathlib import Path


# Accepts metric variables and prints a standard output to the screen along with a summary.txt file to a Resources directory.
# The dictionaries must contain 'Date" and 'PnL" indecies.
def summary_output(number_of_months_in_budget, net_total_amount_of_profits_and_losses, 
average_of_profit_and_losses, greatest_increase_of_profits_dictionary, greatest_decrease_of_losses_dictionary):
    # Capture file path to be written
    output_path = Path("./Output/summary.txt")

    # Open output path 
    filewriter = open(output_path, 'w+')

    # Formatting individual rows for summary output and concatinates each string
    summary_message = "" 
    summary_message += "Financial Analysis\n"
    summary_message += "----------------------------\n"
    summary_message += f"Total Months: {number_of_months_in_budget}\n"
    summary_message += f"Total: ${net_total_amount_of_profits_and_losses}\n"
    summary_message += f"Average Change: ${average_of_profit_and_losses}\n"
    summary_message += f"Greatest Increase in Profits: {greatest_increase_of_profits_dictionary['Date']} (${greatest_increase_of_profits_dictionary['PnL']})\n"
    summary_message += f"Greatest Decrease in Profits: {greatest_decrease_of_losses_dictionary['Date']} (${greatest_decrease_of_losses_dictionary['PnL']})\n"
    
    # Outputs summary message to screen
    print(summary_message)

    # Writes summary message to output path
    filewriter.write(summary_message)

    # Closes file
    filewriter.close()


# Determine the greatest increase or decrease in profits (date and amount) over the entire period.
def greatest_increase_or_decrease
# Value to assign initial greatest increase or decrease in profits or losses
initial_assignment_of_profits = 0

# Loop through list of profits and losses
for a_change_in_profits_and_losses_item in change_in_profits_and_losses_list:
    
    # Assignment of initial value to greatest increase from list
    if initial_assignment_of_profits == 0:

        # Assignment of dictionary values to variables
        date_value = a_change_in_profits_and_losses_item["Date"]
        pnl_value = a_change_in_profits_and_losses_item["PnL"]

        # Assignment of values as the greatest increase in profits dictionary
        greatest_increase_of_profits_dictionary["Date"] = date_value
        greatest_increase_of_profits_dictionary["PnL"] = pnl_value

        # Initial assignment of greatest increase in profits is complete and no longer needs to be performed
        initial_assignment_of_profits = 1

    # Compare one profit or loss value to next value
    if greatest_increase_of_profits_dictionary["PnL"] < a_change_in_profits_and_losses_item["PnL"]:
        
        # Assign profits and losses current item value and date to greatest increase of profits dictionary
        greatest_increase_of_profits_dictionary["Date"] = a_change_in_profits_and_losses_item["Date"]
        greatest_increase_of_profits_dictionary["PnL"] = a_change_in_profits_and_losses_item["PnL"]
