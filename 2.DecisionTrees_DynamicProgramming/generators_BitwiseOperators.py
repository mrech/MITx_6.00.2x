# generate all combinations of N items
def powerSet(items):
    N = len(items)  # ex. 2
    # enumerate the 2**N possible combinations
    for i in range(2**N):  # in range(4)
        combo = []
        for j in range(N):  # in range(2)
            # test bit jth of integer i
            if (i >> j) % 2 == 1:  # if odds numbers
                combo.append(items[j])
        yield combo  # generator


# Returns x with the bits shifted to the right by y places.
# This is the same as //'ing x by 2**y.
'''
i>>j

0>>0 0
0>>1 0

1>>0 1
1>>1 0

2>>0 0
2>>1 1

3>>0 1
3>>1 1

'''

# In 2 bags there are 3^n combinations
# it can be representing by list of 'trinary' bits
# O neither bag - 1 bag1 - 2 bag2


def YieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    N = len(items)

    # run the powerset
    for bag1 in powerSet(items):
        # find the unused items for each subsetting
        remain = [items[j] for j in range(N) if items[j] not in bag1]
        # calculate the powersets of the unused elements. 
        for bag2 in powerSet(remain): 
            yield bag1, bag2


'''
i>>j
Bag1
0>>0 0      
0>>1 0

Bag2
0>>0 0      
0>>1 0

1>>0 1
1>>1 0

2>>0 0
2>>1 1

3>>0 1
3>>1 1


Bag1
1>>0 1
1>>1 0

Bag2
0>>0 0      
0>>1 0

2>>0 0
2>>1 1
'''

# USED IN THE SUBMIT
def yieldAllCombos(items):
    def PowerSet(items, N):
        for i in range(2**N): # all possible subset
            yield [items[j] for j in range(N) if (i >> j) % 2]

    for bag1 in PowerSet(items, len(items)):
        remain = [items[j] for j in range(len(items)) if items[j] not in bag1]
        for bag2 in PowerSet(remain, len(remain)):
            yield (bag1, bag2)