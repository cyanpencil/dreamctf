import random
import math as Math
import grimes
import cellular
# let grimes = require('./grimes.js')
# let helpers = require('./helpers.js')
# let cellular = require('./cellular')
# const choice = helpers.choice

def curtainsFor(key):
    if (key == 'none' or key == 'no'):
        return noCurtains
    elif (key == 'glow'):
        return glowCurtains
    elif (key == 'reverseGlow'):
        return reversedGlowCurtains
    elif (key == 'zigzag'):
        return zigzagCurtains()
    elif (key == 'automata'):
        return cellularCurtains()
    elif (key == 'random'):
        return randomCurtains()
    return undefinedCurtains

def randomCurtains ():
    return random.choice([glowCurtains, reversedGlowCurtains, zigzagCurtains(), zigzagCurtains(), cellularCurtains(), cellularCurtains()])

def glowCurtains (grimer):
    bias = Math.floor(random.random() * 5) - 1
    right = ''
    for i in range(10):
        digit = i
        if (bias): digit = digit + bias
        if (digit > 9): digit = 9
        if (digit < 0): digit = 0
        if (bias):
            bias += Math.floor(random.random() * 3) - 1
            if (bias < -1): bias = -1
        right += '' + grimer(digit)
    # left = right[::-1].join('')
    left = right[::-1]
    return ( left, right )

def reversedGlowCurtains (grimer):
    c = glowCurtains(grimer)
    return { left: c.right, right: c.left }

def undefinedCurtains():
    return { left: '~undefined', right: 'undefined~' }

def noCurtains ():
    return { left: '          ', right: '          ' }



z_maxIns = ''
z_dirindex = ''
z_diro = ''
zag = ''


def zigzagCurtains ():
    global z_diro,z_dirindex,z_maxIns, zag
    mina = 11
    maxa = 24
    thisTime = mina + Math.floor(random.random() * (maxa - mina))
    bias = Math.floor(random.random() * 3) - 2
    zag = ''
    for i in range(thisTime):
        digit = i
        if (bias): digit = digit + bias
        if (digit > 9): digit = 9
        if (digit < 0): digit = 0
        if (bias): 
            bias += Math.floor(random.random() * 3) - 1
            if (bias < -1): bias = -1
        zag += '' + str(digit)
    zag += zag

    z_maxIns = thisTime - 10 # curtains are 10 wide
    z_dirindex = Math.floor(random.random() * z_maxIns)
    z_diro = Math.floor(random.random() * 2) == 1
    if (z_dirindex == 0):
        z_diro = False
    elif (z_dirindex == z_maxIns):
        z_diro = True
    reversed = Math.floor(random.random() * 2) == 1

    def lambdata(grimer):
        global z_dirindex, z_diro, zag, z_maxIns
        returnString = grimes.grimeString(zag[z_dirindex:z_dirindex+10], grimer)
        if (z_diro):
            z_dirindex -= 1
            if (z_dirindex <= 0): z_diro = False
        else:
            z_dirindex += 1
            if (z_dirindex >= z_maxIns): z_diro = True

        rev = returnString[::-1]
        if (reversed): return ( rev, returnString)
        return (returnString, rev)
    return lambdata

def randomBinary(length):
    out = ''
    for i in range((length)):
        out += str(int(round(random.random())))
    return out

z_state = ''
def cellularCurtains():
    global z_state
    ruleNumber = random.choice([60, 102, 99, 26, 129]) # nice rules for 1D automata
    # ruleNumber = random.choice(range(128, 256)) # nice rules for 1D automata
    rule = cellular.ruleForInt(ruleNumber)
    # print("rule", rule)
    length = 40 + 2 + 20 # text area + padding + curtain width
    z_state = randomBinary(length) # start seed
    # print(z_state)
    def lambdata(grimer):
        global z_state
        z_state = cellular.iterate(z_state, rule)
        # print("res", z_state)
        dreamified = cellular.translate(z_state, [9, 3]) # which grimes to use
        return (
            grimes.grimeString(dreamified[0:10], grimer),
            grimes.grimeString(dreamified[-10:], grimer)
        )
    return lambdata

def print_curtains():
    grimer = grimes.grimerFor('stable')
    lambdata = cellularCurtains()
    l, r = "", ""
    for i in range(80):
        a, b = lambdata(grimer)
        l += a + "<br/>"
        r += b + "<br/>"
    return [l, r]

