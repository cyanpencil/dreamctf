import random
import math
# must be up here due to the order things are used
grimeTable = [
  '#+¤x', # 0
  '-:«»~~', # 1
  '##@@£¶',
  '#@£§&¤', # 3
  '@££$$§%%&*¤',
  '%%§$=†**^', # 5
  '†/\\=;:*^', # 6
  '=~~-«»', # 7
  ':,,.^~-', # 8
  '.,¨' # 9
]


def randomGrimer ():
    return random.choice([unstableGrimes, stableGrimes()])

def unstableGrimes (number):
    return grimeTable[number][math.floor(random.random() * len(grimeTable[number]))]

def stableGrimes ():
    localTable = []
    for i in range(10):
      localTable += [grimeTable[i][math.floor(random.random() * len(grimeTable[i]))]]

    return lambda number: localTable[number]

def grimeString (string, grimer):
    out = ''
    for i in range(len(string)):
        out += grimer(int(string[i]))

    return out

def grimerFor(key):
    if (key == 'stable'):
        return stableGrimes() # create a new instance of a stableGrimer

    return unstableGrimes # same function every time (grimer is a function)

def gg(string):
    out = ''
    for i in range(len(string)):
        out += unstableGrimes(int(string[i]))
    return out


print(randomGrimer()(3))
