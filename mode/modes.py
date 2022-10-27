
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