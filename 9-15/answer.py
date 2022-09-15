# exercise 7.7 #

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# exercise 7.8 #

def is_odd(n):
    if n%2 + 1 == 0 :
        return True
    else:
        return False

# exercise 7.10 #
def isRightAngle(a,b,c):
    return a*a + b*b == c*c

def isRightAngle2(a,b,c):
    return isRightAngle(a,b,c) or \
            isRightAngle(b,c,a) or \
            isRightAngle(a,c,b)

print(isRightAngle2(5,3,4))


# exercise 7.11 #
from test import testEqual

def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)


# hello_name #
def hello_name(name):
   return "Hello"+" " + name +"!"
  
# make_out_world #
def make_out_word(out, word):
  return out [:2] + word + out [2:]

# first_two #
def first_two(str):
  return str [0:2]