# Main script
# Input receipt data to be sorted into my Excel budget and spending spreadsheet

# Improvments to make
#   1. Change "Parking Date & Location" to "Parking Location" in the parking section 

from sort_list import Receipt
from combine_list import combine
from write_spreadsheet import write
from basic_functions import working_spreadsheet, dates, dates_in_list, \
    close_spreadsheet, print_sections
from file_locations import retrieve_file

from string import ascii_uppercase as c
import datetime


# Define Variables ------------------------------------------------------------------

# Grab current time
current_time = datetime.datetime.now()

# Define section names to be printed
sections_string = "\nSections:\n 1. Income\n 2. Gas\n 3. Car Maintenance\n" + \
    " 4. Living Expenses\n 5. Groceries\n 6. Eating Out\n 7. Flights\n" + \
        " 8. Parking\n 9. Day-to-Day\n 10. Type 'options' to see this menu" + \
            " again \n 11. Type 'exit' to end"

# Establish filename and directory
filename_pre = "Living Expenses "
filename_suf = ".xlsx"
file_directory = retrieve_file(1)

# Define empty lists to be filled later
income_list          = [[]]
gas_list             = [[]]
car_maintenance_list = [[]]
living_expenses_list = [[]]
groceries_list       = [[]]
food_list            = [[]]
flights_list         = [[]]
parking_list         = [[]]
day_list             = [[]]

# Define the columns where data will be stored
col_index = 2
col_increment = 2
income_col          = [c[col_index], c[col_index + 1]]
gas_col             = [c[col_index + 1*col_increment], c[col_index + \
                        (1 + 1*col_increment)]]
car_maintenance_col = [c[col_index + 2*col_increment], c[col_index + \
                        (1 + 2*col_increment)]]
living_expenses_col = [c[col_index + 3*col_increment], c[col_index + \
                        (1 + 3*col_increment)]]
groceries_col       = [c[col_index + 4*col_increment], c[col_index + \
                        (1 + 4*col_increment)]]
food_col            = [c[col_index + 5*col_increment], c[col_index + \
                        (1 + 5*col_increment)]]
flights_col         = [c[col_index + 6*col_increment], c[col_index + \
                        (1 + 6*col_increment)]]
parking_col         = [c[col_index + 7*col_increment], c[col_index + \
                        (1 + 7*col_increment)]]
day_col             = [c[col_index + 8*col_increment], c[col_index + \
                        (1 + 8*col_increment)]]


# Define input prompts and sorting sections
income_data          = ['Income',          'Source: ',                  'Payment ($): ']
gas_data             = ['Gas',             'Source: ',                  'Cost ($): ']
car_maintenance_data = ['Car Maintenance', 'Part & Source: ',           'Cost ($): ']
living_expenses_data = ['Living Expenses', 'Purchase and Source: ',     'Cost ($): ']
groceries_data       = ['Groceries',       'Source: ',                  'Cost ($): ']
food_data            = ['Food & Drink',    'Purchase: ',                'Cost ($): ']
flights_data         = ['Flights',         'Flight Date & Airline: ',   'Cost ($): ']
parking_data         = ['Parking',         'Parking Date & Location: ', 'Cost ($): ']
day_data             = ['Day-to-Day',      'Purchase: ',                'Cost ($): ']


# Establish File Directory ----------------------------------------------------------
filename = working_spreadsheet(str(current_time.year), file_directory, filename_pre, \
    filename_suf)


# Establish Dates in the Year -------------------------------------------------------
month_data, date_list = dates(current_time.year)  # Generate list of dates in the year
date_list = dates_in_list(month_data, date_list)  # Creates list of dates for whole year


# Begin Program ---------------------------------------------------------------------
print_sections(sections_string)  # Print sections menu initially

while True:
    print("\n--------------------------------------------------------------")
    section = input("\nChoose a section: ")
    section = section.lower()

    if section == '1' or section == 'income':
        display_text = income_data

    elif section == '2' or section == 'gas':
        display_text = gas_data

    elif section == '3' or section == 'car maintenance':
        display_text = car_maintenance_data

    elif section == '4' or section == 'living expenses' or section == 'living':
        display_text = living_expenses_data

    elif section == '5' or section == 'groceries':
        display_text = groceries_data
        
    elif section == '6' or section == 'eating out':
        display_text = food_data

    elif section == '7' or section == 'flights':
        display_text = flights_data

    elif section == '8' or section == 'parking':
        display_text = parking_data

    elif section == '9' or section == 'day to day' or section == 'day-to-day' or \
        section == 'day 2 day':
        display_text = day_data

    elif section == '10' or section == 'options':
        print_sections(sections_string)
        continue

    elif section == '11' or section == 'exit':
        break

    else:
        print("\nUnrecognized input\n")
        continue

    print("\nType 'new' at any point to return to section choice")

    while True:
        try:
            date = input("\nDate (MM-DD): ")
            if date.lower() == 'new':
                break
            month = int(date[:2])
            day = int(date[3:])

            source = input(display_text[1])
            if source.lower() == 'new':
                break

            # need to allow for the user to input a number with commas or a $ in 
            # front and not get an error
            cost = input(display_text[2])
            if cost.lower() == 'new':
                break
            cost = float(cost)

            receipt_data = Receipt(date, source, cost)

            if display_text[0] == 'Income':
                income_list = receipt_data.sort(income_list)

            elif display_text[0] == 'Gas':
                gas_list = receipt_data.sort(gas_list)

            elif display_text[0] == 'Car Maintenance':
                car_maintenance_list = receipt_data.sort(car_maintenance_list)

            elif display_text[0] == 'Living Expenses':
                living_expenses_list = receipt_data.sort(living_expenses_list)

            elif display_text[0] == 'Groceries':
                groceries_list = receipt_data.sort(groceries_list)

            elif display_text[0] == 'Food & Drink':
                food_list = receipt_data.sort(food_list)

            elif display_text[0] == 'Flights':
                flights_list = receipt_data.sort(flights_list)

            elif display_text[0] == 'Parking':
                parking_list = receipt_data.sort(parking_list)

            elif display_text[0] == 'Day-to-Day':
                day_list = receipt_data.sort(day_list)

            else:
                print("Invalid Input")
                continue

        except ValueError:
            print("Invalid Input")
            continue


# Checks to see if the spreadsheet has been closed before writing
close_spreadsheet()


# Combine list items and write them to the spreadsheet ------------------------------

if income_list != [[]]:
    if len(income_list) != 1:
        income_list = combine(income_list)
    write(income_list, income_col, date_list, filename)

if gas_list != [[]]:
    if len(gas_list) != 1:
        gas_list = combine(gas_list)
    write(gas_list, gas_col, date_list, filename)

if car_maintenance_list != [[]]:
    if len(car_maintenance_list) != 1:
        car_maintenance_list = combine(car_maintenance_list)
    write(car_maintenance_list, car_maintenance_col, date_list, filename)

if living_expenses_list != [[]]:
    if len(living_expenses_list) != 1:
        living_expenses_list = combine(living_expenses_list)
    write(living_expenses_list, living_expenses_col, date_list, filename)

if groceries_list != [[]]:
    if len(groceries_list) != 1:
        groceries_list = combine(groceries_list)
    write(groceries_list, groceries_col, date_list, filename)

if food_list != [[]]:
    if len(food_list) != 1:
        food_list = combine(food_list)
    write(food_list, food_col, date_list, filename)

if flights_list != [[]]:
    if len(flights_list) != 1:
        flights_list = combine(flights_list)
    write(flights_list, flights_col, date_list, filename)

if parking_list != [[]]:
    if len(parking_list) != 1:
        parking_list = combine(parking_list)
    write(parking_list, parking_col, date_list, filename)

if day_list != [[]]:
    if len(day_list) != 1:
        day_list = combine(day_list)
    write(day_list, day_col, date_list, filename)
