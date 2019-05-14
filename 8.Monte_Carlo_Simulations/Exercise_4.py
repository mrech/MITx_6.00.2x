import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    success = 0

    for _ in range(numTrials):

        bucket = {'green': 3, 'red': 3}
        for _ in range(3):
            ball = random.choice(['green'] * bucket['green'] +
                                 ['red']*bucket['red'])
            bucket[ball] = bucket[ball] - 1

        if bucket['green'] == 0 or bucket['red'] == 0:
            success += 1

    return success/numTrials

def noReplacementSimulationShort(n):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # one line result
    
    return sum((sum(random.sample((0,0,0,1,1,1),3)) in (0, 3)) for _ in range(n)) / n