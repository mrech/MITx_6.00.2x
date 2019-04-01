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