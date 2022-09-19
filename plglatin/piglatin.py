# bondify #
def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    result = " "
    last = name[0] 
    last = last.upper()
    last = result + last

    first = name[0:]
    first = first[0].upper()+first[1:5]+""
    first = result + first
    
    location = name.find (' ')
    first = name[locations+1:].capitalize()
    
    result = result + last + ","+ "" + first + last
    return result

# piglatin #

def piglatin(word):
"""
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words

"""
    if word[0] in "aeiou":
        return word + 'yay'
    else:
        return word[1:] + word[0] + 'ay'

word = input("Enter a word you want to convert to pig latin: ")
print(' '.join(piglatin(word)))
