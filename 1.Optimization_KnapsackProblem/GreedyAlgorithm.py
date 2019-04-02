# Data abstraction using classes


class Food(object):
    def __init__(self, n, v, w):
        '''
        Initiate with 3 arguments, n: name - v: value - w: calories
        '''
        # stores attributes
        self.name = n
        self.value = v
        self.calories = w

    # getter functions
    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    # operations to print the values of food
    def __str__(self):
        return self.name + ': <' + str(self.value)\
            + ', ' + str(self.calories) + '>'


# Create a menu
def buildMenu(names, values, calories):
    '''
    Input: names, values, calories lists of same length.
           name a lsit of strings
           values and calories lists of numbers
    Return: list of Foods
    '''
    # Initialize menu
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))

    return menu


def greedy(items, maxCost, keyFunction):
    '''
    Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers
    '''
    # copy items and sort its element
    # O(n log n) (n=len(items))
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    # initiate variables
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):  # Run time complexity: O(n)
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)

# Using greedy


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print(' ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value ot allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))  # get the inverse of cost, less expensive the better

    print('\nUse greedy by density to allocate', maxUnits, 'colories')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)

