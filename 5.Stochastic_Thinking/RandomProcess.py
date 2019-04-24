import random

def rollDie():
    '''
    returns a random int between 1 and 6
    '''
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randrange(0,100,2)

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 20

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''

    return random.randrange(10,22,2)
