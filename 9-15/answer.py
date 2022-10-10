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
def isRightAngle(a,b,c):
    return a*a + b*b == c*c

def isRightAngle2(a,b,c):
    return isRightAngle(a,b,c) or \
            isRightAngle(b,c,a) or \
            isRightAngle(a,c,b)

print(isRightAngle2(5,3,4))


# hello_name #
def hello_name(name):
   return "Hello"+" " + name +"!"
  
# make_out_world #
def make_out_word(out, word):
  return out [:2] + word + out [2:]

# first_two #
def first_two(str):
  return str [0:2]