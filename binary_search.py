from random import randint as r
from random import sample as s

def binary_search(seq, item):
    """ This seaches an item in sequence of sorted list
    """
    left = 0
    right = len(seq) -1

    while left <= right:
        mid = left + (left + right)//2
#       Because we need integer not a decimal
        mid_val = seq[mid]
        if mid_val == item:
            return mid
        elif item < mid_val:
            right = mid -1
        else:
            left = mid + 1
    return None

""" problem with this algorithm is that the item number can be bigger than
len(sequence) otherwise it will throw an index out of range error as seen below """

sequence = (s(range(1,100),10))
print(sequence)
#item = r(1,100)
item = 99
print(item)

print(binary_search(sequence, item))
