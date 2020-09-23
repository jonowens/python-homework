# The following defined functions are used to assist in the output and calculations for budget metric compilations.
# Please use Python 3.8.5 and import the following library shown below.

from pathlib import Path



def import_csv_data()
    '''

    '''
    # Capture file path to be read
    csvpath = Path("./Resources/budget_data.csv")

    # Open data in specified path as csv_file 
    with open(csvpath, 'r') as csv_file:

        # Read data from csv_file knowing the data is ',' delimited and assign to csvreader variable
        csvreader = csv.reader(csv_file, delimiter=',')

        # Store data header and go to next line
        header = next(csvreader)
        print(header)
        # Iterate through each line of csvreader
        for row in csvreader:
            # Assign each row to dictionary structure
            first_item = row[0]
            second_item = int(row[1])
            # Assign dictionary data items to budget list
            # "pnl" represents Profit and Loss
            budget.append({'date': first_item, 'pnl': second_item})




def summary_output(number_of_months_in_budget, net_total_amount_of_profits_and_losses, average_of_profit_and_losses, 
greatest_change_dictionary, greatest_decrease_of_losses_dictionary):
    """Accepts metric variables and prints a standard output to the screen along with a summary.txt file to a Resources directory.
    The dictionaries must contain 'date' and 'pnl' indecies.
    
    Args:
        number_of_months_in_budget (int): The number of months in the budget
        net_total_amount_of_profits_and_losses (int): The total amount of combined profits and losses.
        average_of_profit_and_losses (int): The average value of profits and losses.
        greatest_change_dictionary (dict): The greatest change with a 'date' and 'pnl' (profit and loss) index
        greatest_decrease_of_losses_dictionary (dict):  The greatest decrease of losses with a 'date' and 'pnl' (profit and loss) index

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

    Args:
        change_in_profits_and_losses_list (dict): Changes in profits and losses containing a 'date' and 'pnl'
            (profit and loss) index.
        increase_or_decrease (str): Indication to find the greatest "increase" in profits or 
            the greatest "decrease" in profits.

    Returns:
        A dictionary of the greatest change with a 'date' and 'pnl' (profit and loss) index
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
            date_value = a_change_in_profits_and_losses_item["date"]
            pnl_value = a_change_in_profits_and_losses_item["pnl"]

            # Initial assignment of values as the greatest change in dictionary
            greatest_change_dictionary["date"] = date_value
            greatest_change_dictionary["pnl"] = pnl_value

            # Initial assignment of greatest change incremented and no longer needs to be performed
            initial_assignment_performed = "yes"

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
