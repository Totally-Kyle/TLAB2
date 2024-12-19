
def filter_nondigits(data: list) -> list:
    filtered_list = []
    #create a new list named dr_house to store heart rate samples

    for num in data:
        #loop through the list, strip the \n, determin if it's a digit.

        if num.strip().isdigit() == True:
            num = num.strip()

            filtered_list.append(int(num))

         # convert string to int and then append to dr_house

    return filtered_list



"""
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
pass


def filter_outliers(data: list) -> list:
    no_outliers = []
    for beat in data:
        if beat > 30 and beat < 250:
            no_outliers.append(beat)

    return no_outliers



    pass
