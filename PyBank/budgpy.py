# The following defined functions are used to assist in the output and calculations for budget metric compilations.
# Please use Python 3.8.5 and import the following library shown below.

from pathlib import Path




def summary_output(number_of_months_in_budget, net_total_amount_of_profits_and_losses, average_of_profit_and_losses, 
greatest_change_dictionary, greatest_decrease_of_losses_dictionary):
    """Accepts metric variables and prints a standard output to the screen along with a summary.txt file to a Resources directory.
    The dictionaries must contain 'date' and 'pnl' indecies."""

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
    summary_message += f"Greatest Increase in Profits: {greatest_change_dictionary['date']} (${greatest_change_dictionary['pnl']})\n"
    summary_message += f"Greatest Decrease in Profits: {greatest_decrease_of_losses_dictionary['date']} (${greatest_decrease_of_losses_dictionary['pnl']})\n"
    
    # Outputs summary message to screen
    print(summary_message)

    # Writes summary message to output path
    filewriter.write(summary_message)

    # Closes file
    filewriter.close()




def greatest_increase_or_decrease_in_profits(change_in_profits_and_losses_list, increase_or_decrease):
    """Determine the greatest increase or decrease in profits (date and amount) over the entire period.
    Change_in_profits_and_losses_list must contain dictionaries including 'date" and 'pnl' indicies.
    The increase_or_decrease variable to pass indicates whether to find the greatest 'increase' in profits
    or the greatest 'decrease' in profits."""

    # Value to assign initial greatest increase or decrease in profits or losses
    initial_assignment_performed = 0
    # Stores 'Date' and 'PnL' in dictionary
    greatest_change_dictionary = {}

    # Loop through list of profits and losses
    for a_change_in_profits_and_losses_item in change_in_profits_and_losses_list:
        
        # Assignment of initial value to greatest increase from list
        if initial_assignment_performed == 0:

            # Assignment of dictionary values to variables
            date_value = a_change_in_profits_and_losses_item["date"]
            pnl_value = a_change_in_profits_and_losses_item["pnl"]

            # Initial assignment of values as the greatest change in dictionary
            greatest_change_dictionary["date"] = date_value
            greatest_change_dictionary["pnl"] = pnl_value

            # Initial assignment of greatest change incremented and no longer needs to be performed
            initial_assignment_performed = 1

        # Compare one change value to next value to find the greatest 'increase' in profits
        if greatest_change_dictionary["pnl"] < a_change_in_profits_and_losses_item["pnl"] and increase_or_decrease == "increase":
            
            # Assign profits and losses current item value and date to greatest change dictionary
            greatest_change_dictionary["date"] = a_change_in_profits_and_losses_item["date"]
            greatest_change_dictionary["pnl"] = a_change_in_profits_and_losses_item["pnl"]
    
        # Compare one change value to next value to find the greatest 'decrease' in losses
        elif greatest_change_dictionary["pnl"] > a_change_in_profits_and_losses_item["pnl"] and increase_or_decrease == "decrease":
            
            # Assign profits and losses current item value and date to greatest decrease of losses dictionary
            greatest_change_dictionary["date"] = a_change_in_profits_and_losses_item["date"]
            greatest_change_dictionary["pnl"] = a_change_in_profits_and_losses_item["pnl"]
    
    # Return greatest increase or decrease dictionary
    return greatest_change_dictionary