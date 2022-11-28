# I finished the extra- Handle upper and lower case and/or punctuation

f = open('input.txt')
pirate_speak = f.read()
print(pirate_speak)

pirate_speak = pirate_speak.lower()
dictionary = {'hello': "ahoy",
              'matey':"everybody",
              'lucky person': "piston proof",
              'you':"ye",
              'friend':"bucko",
              'clothes':"togs",
              'gift':"booty",
              'surprised' : "ho",
              'my' : "me",
              'money' : "blunt"
              }
print(dictionary)

          
def get_translate(pirate_speak):
    for key in dictionary.keys():
        pirate_speak = pirate_speak.replace(key, dictionary[key])
    return pirate_speak.capitalize()
print(get_translate(pirate_speak))

x = get_translate(pirate_speak)
print( '. '.join(map(lambda s: s.strip().capitalize(), x.split('.'))))