# Write a function to find the smallest value in a listKfind smallest in a list of items
listKfind = [2,17,18,4,1,30,65]
result = min(listKfind)
print('The smallest value is ',result)

# Write a function that returns a new list that contains
# all the odd items in the original list

# Write a function that takes a string and returns a new string where
# all the words are capitalized.
def capitalized(word):
    result = word.title()
    return result
# Testing
print(capitalized('my life is beautiful.'))

# Write a function that takes a string and returns a new string with
# every word that's longer than 5 character turned into upper case
def uppercase(word):
    if len(word) > 5 :
        result = word.upper
    else :
        result = word
    return result

# Write a function that takes a list of numbers and returns a new list
# with each item squared
def squared(aList):
    for position in range(len(aList)):
        aList[position] =aList[position] ** 2
mylist = [4, 5, 6]
print(mylist)
squared(mylist)
print(mylist)


# Write a function that takes two lists of numbers and returns a new
# list where each item is the corresponding values of the original
# lists added together. Ex [1,2,3] and [10,20,30] would return the
# list [11,22,33]


# exercise 10 #
# Count how many words in a list have length 5.
def countWord(word):
    for position in range(len(word)):
        word[position] =word[position] 

# exercise 11 #

# exercise 12 #