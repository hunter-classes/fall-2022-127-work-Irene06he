import random

f = open('story.py')# extras 1 --> write a story in a file and read it from your program, and I received assistance from Kai Min
story = f.read()
f.close()


hero = ['Charles','Rachael','Joey','Anna','Ben','Ryan','Lawren']
verb = ['plays','works','writes','learns','eats','walks','runs']
noun = ['library','playground','classroom','bedroom','street','hallway']

def gets_newstory (story)  :
    new_story = []
    for word in story.split():
        new_story = new_story +[word.replace('<verb>',random.choice(verb)).replace('<noun>',random.choice(noun))]
        result = " ".join(new_story)
    return result.replace('<hero>',random.choice(hero)) # extras 2--> <HERO> would randomly choose a hero once and then use that name for all instances of <HERO>

print(gets_newstory (story))