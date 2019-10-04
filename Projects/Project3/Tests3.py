#!/usr/bin/python3

import unittest
import itertools

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


class TreeSetTests(unittest.TestCase):

    def test_is_empty(self):
        tree = TreeSet(natural_order)
        self.assertTrue(tree.is_empty())
        tree.insert(0)
        self.assertFalse(tree.is_empty())
        tree.remove(0)
        self.assertTrue(tree.is_empty())

    def test_len(self):
        tree = TreeSet(natural_order)
        self.assertEqual(0, len(tree))
        for i in range(0, 10):
            tree.insert(i)
            self.assertEqual(i + 1, len(tree))
        for i in range(0, 10):
            tree.insert(i)
            self.assertEqual(10, len(tree))

    def test_height(self):
        import math
        tree = TreeSet(natural_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        self.assertEqual(-1, tree.height())
        for index, item in enumerate(sequence):
            tree.insert(item)
            self.assertGreaterEqual(index, tree.height())
            self.assertLessEqual(math.floor(math.log2(index + 1)), tree.height())

    def test_insert(self):
        tree = TreeSet(natural_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        for index, item in enumerate(sequence):
            self.assertEqual(index, len(tree))
            self.assertFalse(item in tree, item)
            self.assertTrue(tree.insert(item))
            self.assertTrue(item in tree, item)

        for item in sequence:
            self.assertEqual(len(sequence), len(tree))
            self.assertTrue(item in tree, item)
            self.assertFalse(tree.insert(item))
            self.assertTrue(item in tree, item)

    def test_remove(self):
        tree = TreeSet(natural_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        for item in sequence:
            tree.insert(item)
        self.assertEqual(len(sequence), len(tree))
        for size, item in zip(reversed(range(len(sequence))), range(-5, 20)):
            self.assertTrue(item in tree, item)
            self.assertTrue(tree.remove(item), item)
            self.assertFalse(item in tree, tree)

        for item in range(-5, 20):
            self.assertFalse(tree)
            self.assertFalse(item in tree)
            self.assertFalse(tree.remove(item))
            self.assertFalse(item in tree)

    def test_contains(self):
        tree = TreeSet(natural_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        for item in sequence:
            self.assertFalse(item in tree, item)
            tree.insert(item)
            self.assertTrue(item in tree, item)
        for item in range(-5, 20):
            self.assertTrue(item in tree, item)
            tree.remove(item)
            self.assertFalse(item in tree, item)

    def test_comp(self):
        tree = TreeSet(reverse_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        for i in sequence:
            tree.insert(i)
        self.assertEqual(19, tree.first())
        self.assertEqual(-5, tree.last())

        for x, y in zip(reversed(range(-5, 20)), tree):
            self.assertEqual(x, y)

    def test_first(self):
        tree = TreeSet(natural_order)
        self.assertRaises(KeyError, tree.first)
        tree.insert(5)
        self.assertEqual(5, tree.first())
        tree.insert(7)
        self.assertEqual(5, tree.first())
        tree.insert(3)
        self.assertEqual(3, tree.first())
        tree.insert(6)
        self.assertEqual(3, tree.first())
        tree.insert(4)
        self.assertEqual(3, tree.first())
        tree.insert(8)
        self.assertEqual(3, tree.first())
        tree.insert(9)
        self.assertEqual(3, tree.first())
        tree.insert(2)
        self.assertEqual(2, tree.first())
        tree.insert(1)
        self.assertEqual(1, tree.first())
        tree.insert(0)
        self.assertEqual(0, tree.first())

    def test_last(self):
        tree = TreeSet(natural_order)
        self.assertRaises(KeyError, tree.last)
        tree.insert(5)
        self.assertEqual(5, tree.last())
        tree.insert(7)
        self.assertEqual(7, tree.last())
        tree.insert(3)
        self.assertEqual(7, tree.last())
        tree.insert(6)
        self.assertEqual(7, tree.last())
        tree.insert(4)
        self.assertEqual(7, tree.last())
        tree.insert(8)
        self.assertEqual(8, tree.last())
        tree.insert(9)
        self.assertEqual(9, tree.last())
        tree.insert(2)
        self.assertEqual(9, tree.last())
        tree.insert(1)
        self.assertEqual(9, tree.last())
        tree.insert(0)
        self.assertEqual(9, tree.last())

    def test_clear(self):
        tree = TreeSet(natural_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        for item in sequence:
            tree.insert(item)
        self.assertFalse(tree.is_empty())
        tree.clear()
        self.assertTrue(tree.is_empty())
        self.assertRaises(KeyError, tree.first)
        self.assertRaises(KeyError, tree.last)
        tree.clear()
        for item in sequence:
            self.assertFalse(item in tree)

    def test_iter(self):
        tree = TreeSet(natural_order)
        sequence = [-4, 11, 6, 18, -1, 8, 13, 0, 3, 19, -5, 7, 9, 12, 2, 17, 4, 1, 10, -3, 5, 14, 15, 16, -2]
        for i in sequence:
            tree.insert(i)
        self.assertEqual(len(sequence), len([x for x in tree]))
        for s, t in itertools.zip_longest(range(-5, 20), tree):
            self.assertEqual(s, t)
        for s, t in itertools.zip_longest(range(-5, 20), tree):
            self.assertEqual(s, t)

    def test_disjoint(self):
        tree1 = TreeSet(natural_order)
        tree2 = TreeSet(natural_order)
        tree3 = TreeSet(natural_order)
        sequence = [1,2,3,4,5,6]
        for item in sequence:
            tree1.insert(item)
        sequence = [7,8,9,10,11]
        for item in sequence:
            tree2.insert(item)
        sequence = [6,7,8,9,10]
        for item in sequence:
            tree3.insert(item)
        self.assertTrue(tree1.is_disjoint(tree2))
        self.assertFalse(tree1.is_disjoint(tree3))
        self.assertTrue(tree2.is_disjoint(tree1))
        self.assertFalse(tree3.is_disjoint(tree1))

    def test_sequence(self):
        tree = TreeSet(natural_order)
        self.assertTrue(tree.insert(5))
        self.assertTrue(tree.insert(7))
        self.assertTrue(tree.insert(11))
        self.assertFalse(tree.insert(7))
        self.assertEqual(5, tree.first())
        self.assertEqual(11, tree.last())
        self.assertEqual([5, 7, 11], [x for x in tree])
        self.assertTrue(5 in tree)
        self.assertTrue(7 in tree)
        self.assertTrue(11 in tree)
        self.assertFalse(3 in tree)
        self.assertTrue(tree.remove(7))
        self.assertFalse(7 in tree)
        self.assertFalse(tree.remove(7))
        self.assertEqual(2, len(tree))
        self.assertFalse(7 in tree)
        tree.clear()
        self.assertTrue(tree.is_empty())
        self.assertFalse(5 in tree)
        self.assertTrue(tree.insert(5))
        self.assertEqual(1, len(tree))


if __name__ == '__main__':
    unittest.main()

