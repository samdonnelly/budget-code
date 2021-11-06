# Supporting script
# Basic functions used in the "income_spending.py" spreadsheet

from os import path


def working_spreadsheet(year, file_directory, filename_pre, filename_suf):
    while True:
        try:
            confirm = input("\nThis data will be added to 'Living Expenses " + year + ".xlsx'. Is this correct? Y/N: ")

            if confirm.lower() == 'n' or confirm.lower() == 'no':
                year = input("Input the year of the receipts: ")

            elif confirm.lower() == 'y' or confirm.lower() == 'yes':
                pass

            else:
                continue

        except ValueError:
            print("\nInvalid Input")
            continue

        # Check if the file exists or is in the correct directory
        filename = file_directory + filename_pre + year + filename_suf

        if path.exists(filename):
            return filename

        else:
            print("\nThis file does not exist or it is in the wrong directory. Please create the file or "
                  "move it to the correct location.")


def dates(year):
    if year % 4 == 0:
        feb_days = 29
        date_list = [''] * 366
    else:
        feb_days = 28
        date_list = [''] * 365

    month_data = {
        "Jan": ['01', 31],
        "Feb": ['02', feb_days],
        "Mar": ['03', 31],
        "Apr": ['04', 30],
        "May": ['05', 31],
        "Jun": ['06', 30],
        "Jul": ['07', 31],
        "Aug": ['08', 31],
        "Sep": ['09', 30],
        "Oct": ['10', 31],
        "Nov": ['11', 30],
        "Dec": ['12', 31]
    }

    return month_data, date_list


def dates_in_list(month_data, date_list):
    date_count = 0
    for month, items in month_data.items():
        for i in range(0, items[1]):
            # Add a zero to the front of the single digit days
            if len(str(i + 1)) == 1:
                day_of_year = '0' + str(i + 1)
            else:
                day_of_year = str(i + 1)
            date_list[date_count] = items[0] + "-" + day_of_year
            date_count += 1

    return date_list


def close_spreadsheet():
    # Should make this actively check if the file is open already
    while True:
        try:
            spreadsheet_status = input("\nIs the spreadsheet closed? Y/N: ")
            if spreadsheet_status.lower() == 'n' or spreadsheet_status.lower() == 'no':
                print("\nClose the spreadsheet.\n")
                continue
            elif spreadsheet_status.lower() == 'y' or spreadsheet_status.lower() == 'yes':
                break
            else:
                continue

        except ValueError:
            print("\nInvalid Input\n")

    return


def print_sections(sections_string):
    print(sections_string)
    print("\n--------------------------------------------------------------")
    return
