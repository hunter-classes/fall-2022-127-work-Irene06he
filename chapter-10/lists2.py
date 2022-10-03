# exericise 4 #
def average(numlist):

    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)


# exercise 6 #
list = [2,3,4]
def sum_of_squares(xs):
    SumSquares = 0
    for i in xs:
        SumSquares += i ** 2
    return SumSquares

print(sum_of_squares(list))