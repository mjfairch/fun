import itertools

'''
This program verifies by brute force the mathematical fact that there is
exactly one other labeling of 2d6 (with face values ranging over 1..11,
allowing repetitions) which shares the probability distribution for the
sum of two normal six-sided dice.

See: https://en.wikipedia.org/wiki/Sicherman_dice
'''

def dist(rolls):
    '''
    Return the distribution for the sum of the given rolls, where each roll
    is simply a list of values.
    '''
    sums = [sum(r) for r in rolls]
    n = dict((s,0) for s in set(sums))
    for s in sums:
        n[s] += 1
    return n

if __name__ == '__main__':
    # Compute the standard 2d6 distribution
    vals = range(1, 7)
    std = dist(itertools.product(vals, vals))
    # "trim" eliminates tuples which differ only in the order of their entries
    trim = lambda x: set(tuple(sorted(y)) for y in x)
    # If m1,M1 and m2,M2 are the minimum,maximum pip values on the dice, then:
    #   Because 2 is possible, we must have m1 = m2 = 1
    #   Because at most 12 is possible, we must have M1, M2 <= 11
    #   Because 12 is possible, must have M2 = 12 - M1
    #   By symmetry, we may restrict M1 to the range 1..6.
    # Enumerate six-sided dice with face values in m1..M1, up to order of faces
    dice1 = trim(itertools.product([1], vals, vals, vals, vals, vals))
    cnt = 0
    for firstDie in dice1:
        # Enumerate all possible six-sided dice with pips in (m2,M2)
        vals = range(1, 12 - max(firstDie) + 1)
        dice2 = trim(itertools.product([1], vals, vals, vals, vals, vals))
        for secondDie in dice2:
            cnt += 1
            d = dist(itertools.product(firstDie, secondDie))
            if (std == d):
                print(firstDie, secondDie, 'has distribution')
                print(d)
    print('Computed the distribution for', cnt, 'configurations')
