# exercise 5 #
def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

# exercise 7 #
import random

def countOdd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd

# make a random list to test the function
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))


# exercise 8 #
def is_even(x):
    # if the remainder (modulo) is 0 then it's evenly divisible by 2 => even
    return x % 2 == 0  

def sum_of_evens(it):
    return sum(filter(is_even, it))