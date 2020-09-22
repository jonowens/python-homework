# The following defined functions are used to assist in the output and calculations for budget metric compilations.
# Please use Python 3.8.5 and import the following library shown below.

from pathlib import Path

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

