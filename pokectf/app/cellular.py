def ruleForInt(ruleNumber):
    binary = bin(ruleNumber)[2:]
    # print(binary)
    return ("00000000" + binary)[-8:]

def iterate(previous, rule):
    output = ''
    for i in range(len(previous)):
        mask = 0;
        if (previous[(i + len(previous) - 1) % len(previous)] == '1'): mask += 4
        if (previous[i] == '1'): mask += 2
        if (previous[(i + len(previous) + 1) % len(previous)] == '1'): mask += 1
        output += str(rule[mask])
        # print(i, output)
    # print(rule, mask)
    return output

# lookup table for what to give to the grimer. automata uses 0 or 1 for state, so we can use an array here
# with a number in the 0th and 1st positions.
def translate(input, table):
    output = ''
    for i in range(len(input)):
        output += str(table[int(input[i])])
    return output
