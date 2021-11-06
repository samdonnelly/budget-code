# Supporting script
# Combine terms with the same date into lists


def combine(total_list):
    length = len(total_list)
    deduction = 0  # used to subtract from the total length of total_list when an entry is removed

    for i in range(0, length):
        # Get the date of the current list item
        date = total_list[i][0]
        day = int(date[3:])
        month = int(date[:2])

        counter = 1  # used to iterate through total_list and check against the current value

        while True:
            # If at the end of the dates in the list
            if i+counter == (length - deduction):
                break

            date_check = total_list[i+counter][0]
            day_check = int(date_check[3:])
            month_check = int(date_check[:2])

            # CHeck if the entries are the same and combine if they are
            if day == day_check and month == month_check:
                total_list[i][1] = total_list[i][1] + ", " + total_list[i+counter][1]
                total_list[i][2] = "=" + str(total_list[i][2]) + "+" + str(total_list[i+counter][2])
                total_list.remove(total_list[i+counter])

                deduction += 1

            # If the next entry is not equal then the other won't be either so we break the loop
            else:
                break

        # Return once whole list it iterated
        if i+counter == (length - deduction):
            return total_list
