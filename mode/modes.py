
def find_Largest(list):
    result = list[0]
    for number in list[1:]:
        if number > result:
            result = number
    return result


def CountFrequency(my_list):
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)
    return freq

def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive

    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies

    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list

    # 3. the index with the highest
    # value in tallies is the mode

    pass