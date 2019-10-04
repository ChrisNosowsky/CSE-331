#!/usr/bin/python3

import unittest

from Heap import Heap, find_median


class TreeSetTests(unittest.TestCase):

    def test_len(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        self.assertEqual(0, len(heap))
        for index, item in enumerate(sequence):
            heap.insert(item)
            self.assertEqual(index + 1, len(heap))

    def test_peek(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        min_items = [5, 5, 3, 3, 3, 2, 0, 0, 0, 0]
        self.assertRaises(IndexError, heap.peek)
        for item, min_item in zip(sequence, min_items):
            heap.insert(item)
            self.assertEqual(min_item, heap.peek())

    def test_insert(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        min_items = [5, 5, 3, 3, 3, 2, 0, 0, 0, 0]
        self.assertRaises(IndexError, heap.peek)
        for index, (item, min_item) in enumerate(zip(sequence, min_items)):
            heap.insert(item)
            self.assertEqual(index + 1, len(heap))
            self.assertEqual(min_item, heap.peek())

    def test_extract(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        self.assertRaises(IndexError, heap.extract)
        for item in sequence:
            heap.insert(item)
        for index in range(len(sequence)):
            self.assertEqual(index, heap.extract())
        self.assertRaises(IndexError, heap.extract)

    def test_extend(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        copy = [x for x in sequence]
        heap.extend(sequence)
        self.assertEqual(10, len(heap))
        heap.extend(sequence)
        self.assertEqual(20, len(heap))
        for i in range(10):
            self.assertEqual(i, heap.peek())
            self.assertEqual(i, heap.extract())
            self.assertEqual(20 - 2 * i - 1, len(heap))
            self.assertEqual(i, heap.peek())
            self.assertEqual(i, heap.extract())
            self.assertEqual(20 - 2 * i - 2, len(heap))
            self.assertEqual(copy, sequence)

    def test_median(self):
        self.assertRaises(IndexError, find_median, [])
        sequence = [5, 9, 3, 4, 6, 2, 8, 7, 1]
        copy = [x for x in sequence]
        self.assertEqual(5, find_median(sequence))
        self.assertEqual(copy, sequence)

        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        copy = [x for x in sequence]
        self.assertIn(find_median(sequence), [4, 5])
        self.assertEqual(copy, sequence)

    def test_max(self):
        heap = Heap(lambda a, b: a >= b)
        sequence = [5, 3, 4, 6, 2, 0, 8, 9, 7, 1]
        max_items = [5, 5, 5, 6, 6, 6, 8, 9, 9, 9]
        self.assertRaises(IndexError, heap.peek)
        for item, max_item in zip(sequence, max_items):
            heap.insert(item)
            self.assertEqual(max_item, heap.peek())

    def test_clear(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        heap.extend(sequence)
        self.assertFalse(heap.is_empty())
        heap.clear()
        self.assertTrue(heap.is_empty())
        self.assertRaises(IndexError, heap.peek)
        self.assertRaises(IndexError, heap.extract)
        heap.insert(9)
        self.assertEqual(1, len(heap))
        self.assertEqual(9, heap.peek())
        self.assertEqual(9, heap.extract())
        self.assertTrue(heap.is_empty())

    def test_iter(self):
        heap = Heap(lambda a, b: a <= b)
        sequence = [5, 9, 3, 4, 6, 2, 0, 8, 7, 1]
        heap.extend(sequence)
        dump = [x for x in heap]
        self.assertEqual(len(sequence), len(dump))
        self.assertEqual(0, dump[0])
        self.assertEqual(set(sequence), set(dump))


if __name__ == '__main__':
    unittest.main()
