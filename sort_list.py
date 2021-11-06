# Supporting script
# Record and sort receipt data


class Receipt:

    def __init__(self, date, source, cost):
        self.date = date
        self.source = source
        self.cost = cost

    def sort(self, total_list):
        insert_list = [self.date, self.source, self.cost]

        # Date of new entry to list
        month_insert = int(self.date[:2])
        day_insert = int(self.date[3:])

        # If it's the first entry in the list
        if total_list == [[]]:
            total_list[0] = insert_list
            return total_list

        else:
            length = len(total_list)
            # Find where to put new item in list
            for i in range(0, length):  # total_list:
                # Date of current list entry being checked
                date_other = total_list[i][0]
                month_other = int(date_other[:2])
                day_other = int(date_other[3:])

                # If month is greater than it comes after the current entry
                if month_insert > month_other:
                    # Check is it's the last iteration
                    if i == length - 1:  # len(total_list) - 1:
                        total_list.append(insert_list)
                        return total_list

                # If months are equal then days must be checked
                elif month_insert == month_other:
                    # If day is greater then it comes after this entry
                    if day_insert > day_other:
                        if i == length - 1:  # len(total_list) - 1:
                            total_list.append(insert_list)
                            return total_list

                    # If days are equal they will be combined later
                    elif day_insert == day_other:
                        total_list.insert(i, insert_list)
                        return total_list

                    # If day is less then it takes the position of this entry
                    else:
                        total_list.insert(i, insert_list)
                        return total_list

                # If the month is less than it takes the position of this entry
                else:
                    total_list.insert(i, insert_list)
                    return total_list
