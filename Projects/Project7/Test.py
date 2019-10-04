
import unittest

from Lis import *
from Main7 import read_file


if __name__ == '__main__':
    seq = read_file('romeo-intro.txt')
    copy = seq[:]
    result = find_lis(seq)
    print(verify_increasing(result))





