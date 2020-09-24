# The following defined functions are used to assist in the output and calculations for data analysis.
# Please use Python 3.8.5 and import library 'myfunctions' to use the functions shown below.

from pathlib import Path
import csv



def import_csv_data(file_name, delimiter_separator):
    '''Reads data from a .csv file and creates a list of dictionaries with the data.
        The function accepts two attributes per row with the second attribute being an
        integer.
    
    Args: 
        file_name (str): Name of data file (Example: "data.csv")
        delimiter_separator (str): Character(s) separating values in csv file

    Returns: 
        A list of dictionaries with assigned values from csv file
    '''    
    # Initialize variables
    csvpath = ""
    temp_list = []

    # Capture file path to be read
    csvpath = Path("./Resources/" + file_name)

    # Open data in specified path as csv_file 
    with open(csvpath, 'r') as csv_file:

        # Read data from csv_file knowing the data is ',' delimited and assign to csvreader variable
        csvreader = csv.reader(csv_file, delimiter=delimiter_separator)

        # Store data header and go to next line
        header = next(csvreader)

        # Iterate through each line of csvreader
        for row in csvreader:

            # Assign each row to dictionary structure
            first_item = row[0]
            second_item = int(row[1])

            # Assign dictionary data items to budget list
            # "pnl" represents Profit and Loss
            temp_list.append({header[0]: first_item, header[1]: second_item})

    return temp_list


def summary_output(number_of_months_in_budget, net_total_amount_of_profits_and_losses, average_of_profit_and_losses, 
greatest_increase_date, greatest_increase_number, greatest_decrease_date, greatest_decrease_number):
    """Accepts metric variables and prints a standard output to the screen along with a summary.txt file to a Resources directory.
    The dictionaries must contain 'date' and 'pnl' indecies.
    
    Args:
        number_of_months_in_budget (int): The number of months in the budget
        net_total_amount_of_profits_and_losses (int): The total amount of combined profits and losses.
        average_of_profit_and_losses (int): The average value of profits and losses.
        greatest_increase_date (str): The greatest increase date
        greatest_increase_number (int): The greatest increase number
        greatest_decrease_date (str): The greatest loss date
        greatest_decrease_number (int): The greatest loss number

    Output:
        Outputs summary message to screen and ./Output/summary.txt
    """

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
    summary_message += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_number})\n"
    summary_message += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_number})\n"
    
    # Outputs summary message to screen
    print(summary_message)

    # Writes summary message to output path
    filewriter.write(summary_message)

    # Closes file
    filewriter.close()




def greatest_increase_or_decrease_in_profits(change_in_profits_and_losses_list, increase_or_decrease, key_1, key_2):
    """Determine the greatest increase or decrease in profits (date and amount) over the entire period.
    Change_in_profits_and_losses_list must contain dictionaries including 'Date" and 'Profit/Losses' indicies.

    Args:
        change_in_profits_and_losses_list (dict): Changes in profits and losses containing a 'Date' and 'Profit/Losses'
            key.
        increase_or_decrease (str): Indication to find the greatest "increase" in profits or 
            the greatest "decrease" in profits.
        key_1 (str): Name of key 1.  Usually a "Date"
        key_2 (str): name of key 2.  Usually a "Profit/Losses" or "Value"

    Returns:
        A dictionary of the greatest change with a 'Date' and 'Profit/Losses' (profit and loss) index
    """

    # Value to assign initial greatest increase or decrease in profits or losses
    initial_assignment_performed = "no"
    # Stores 'Date' and 'PnL' in dictionary
    greatest_change_dictionary = {}

    # Loop through list of profits and losses
    for a_change_in_profits_and_losses_item in change_in_profits_and_losses_list:
        
        # Assignment of initial value to greatest increase from list
        if initial_assignment_performed == "no":

            # Assignment of dictionary values to variables
            date_value = a_change_in_profits_and_losses_item[key_1]
            pnl_value = a_change_in_profits_and_losses_item[key_2]

            # Initial assignment of values as the greatest change in dictionary
            greatest_change_dictionary[key_1] = date_value
            greatest_change_dictionary[key_2] = pnl_value

            # Initial assignment of greatest change incremented and no longer needs to be performed
            initial_assignment_performed = "yes"

        # Compare one change value to next value to find the greatest 'increase' in profits
        if greatest_change_dictionary[key_2] < a_change_in_profits_and_losses_item[key_2] and increase_or_decrease == "increase":
            
            # Assign profits and losses current item value and date to greatest change dictionary
            greatest_change_dictionary[key_1] = a_change_in_profits_and_losses_item[key_1]
            greatest_change_dictionary[key_2] = a_change_in_profits_and_losses_item[key_2]
    
        # Compare one change value to next value to find the greatest 'decrease' in losses
        elif greatest_change_dictionary[key_2] > a_change_in_profits_and_losses_item[key_2] and increase_or_decrease == "decrease":
            
            # Assign profits and losses current item value and date to greatest decrease of losses dictionary
            greatest_change_dictionary[key_1] = a_change_in_profits_and_losses_item[key_1]
            greatest_change_dictionary[key_2] = a_change_in_profits_and_losses_item[key_2]
    
    # Return greatest increase or decrease dictionary
    return greatest_change_dictionary




def calculate_sum(list_of_dictionaries, key_name):
    """Accepts a list of dictionaries and loops through the list adding each key value.
    
    Args:
        list_of_dictionaries (list): A list of dictionaries
        key_name (str): The name of the key in the dictionaries to sum

    Returns:
        The sum of all the specified key values in the list.
    """

    # Initialize variables
    sum = 0

    # Loop through list
    for a_dictionary in list_of_dictionaries:

        # Add key values to sum variable
        sum += a_dictionary[key_name]
        
    return sum
