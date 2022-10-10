# bondify #
def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    result = " "
    last = name[0:] 
    last = last[0].upper()+last[1:5]
    last = result + last

    first = name[0:]
    first = first[0].upper()+first[1:5]+""
    first = result + first
    
    location = name.find (' ')
    first = name[location+1:].capitalize()
    
    result = result + last + ","+ "" + first + last
    return result

#Testing
result = bondify("james bond")
print("james bond --> ",result)

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
 def piglatinify(word):

    first = word[0]
    if first in 'aeiou':
        result = word + 'ay'
    else:
        # move first letter to end and add 'ay'
        result = word[1:]+first+'ay'
    
    return result

#Testing
test_word = "hello"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatinify(test_word)
print(test_word," -> ",result)
