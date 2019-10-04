#!/usr/bin/python3

import unittest
import itertools
import math
from TreeSet import TreeSet

def natural_order(x, y):
    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1


def reverse_order(x, y):
    return natural_order(y, x)

tree = TreeSet(natural_order)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
