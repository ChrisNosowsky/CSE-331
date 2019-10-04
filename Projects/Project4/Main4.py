#!/usr/bin/python3

import unittest

from Heap import Heap, find_median


def main(filename):
    '''
        with open(filename, 'r') as reader:
        text = [line.strip() for line in reader]
        median = find_median(text)
        print('Median:', median)
    :param filename:
    :return:
    '''
heap = Heap(lambda a, b: a < b)
sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
heap.extend(sequence)
for result, item in zip(range(5), range(5, 10)):
    print(result)
    print(heap.replace(item))
for item in range(5):
    print(item)
    print(heap.replace(item))

if __name__ == '__main__':
    main('alphabet.txt')
