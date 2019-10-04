#!/usr/bin/python3

import math
import unittest

from Graph import Graph


def read_graph(filename):
    with open(filename, 'r') as reader:
        g = Graph(int(reader.readline()))
        for line in reader:
            (u, v, w) = line.split()
            g.insert_edge(int(u), int(v), float(w))
        return g
        

class TreeSetTests(unittest.TestCase):

    def test_size1(self):
        g = read_graph('g1.txt')
        self.assertEqual(5, g.order)
        self.assertEqual(6, g.size)
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_size2(self):
        g = read_graph('g2.txt')
        self.assertEqual(10, g.order)
        self.assertEqual(12, g.size)
        self.validate_equality(read_graph('g2.txt'), g)

    def test_insert_edge1(self):
        g = read_graph('g1.txt')
        g.insert_edge(2, 4, 3.5)
        self.assertEqual(5, g.order)
        self.assertEqual(7, g.size)
        g.insert_edge(2, 4, 2.5)
        self.assertEqual(5, g.order)
        self.assertEqual(7, g.size)
        self.assertRaises(IndexError, g.insert_edge, 2, 7, 1.0)
        self.assertRaises(IndexError, g.insert_edge, 7, 1, 1.0)
        
    def test_insert_edge2(self):
        g = read_graph('g2.txt')
        g.insert_edge(2, 4, 3.5)
        self.assertEqual(10, g.order)
        self.assertEqual(13, g.size)
        g.insert_edge(2, 4, 2.5)
        self.assertEqual(10, g.order)
        self.assertEqual(13, g.size)
        self.assertRaises(IndexError, g.insert_edge, 2, 10, 1.0)
        self.assertRaises(IndexError, g.insert_edge, 10, 1, 1.0)

    def test_degree1(self):
        g = read_graph('g1.txt')
        self.assertEqual(2, g.degree(0))
        self.assertEqual(3, g.degree(1))
        self.assertEqual(3, g.degree(3))
        self.assertRaises(IndexError, g.degree, 7)
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_degree2(self):
        g = read_graph('g2.txt')
        self.assertEqual(4, g.degree(3))
        self.assertEqual(2, g.degree(0))
        self.assertEqual(2, g.degree(7))
        self.assertRaises(IndexError, g.degree, 10)
        self.validate_equality(read_graph('g2.txt'), g)

    def test_are_connected1(self):
        g = read_graph('g1.txt')
        self.assertTrue(g.are_connected(0, 1))
        self.assertTrue(g.are_connected(4, 1))
        self.assertTrue(g.are_connected(1, 0))
        self.assertTrue(g.are_connected(1, 4))
        self.assertFalse(g.are_connected(0, 4))
        self.assertFalse(g.are_connected(4, 0))
        self.assertFalse(g.are_connected(2, 2))
        self.assertRaises(IndexError, g.are_connected, 2, 7)
        self.assertRaises(IndexError, g.are_connected, 7, 1)
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_are_connected2(self):
        g = read_graph('g2.txt')
        self.assertTrue(g.are_connected(0, 1))
        self.assertTrue(g.are_connected(4, 3))
        self.assertTrue(g.are_connected(9, 7))
        self.assertTrue(g.are_connected(5, 6))
        self.assertFalse(g.are_connected(0, 9))
        self.assertFalse(g.are_connected(2, 1))
        self.assertFalse(g.are_connected(8, 8))
        self.assertRaises(IndexError, g.are_connected, 3, 10)
        self.assertRaises(IndexError, g.are_connected, 10, 0)
        self.validate_equality(read_graph('g2.txt'), g)

    def test_is_path_valid1(self):
        g = read_graph('g1.txt')
        self.assertTrue(g.is_path_valid([0, 2]))
        self.assertTrue(g.is_path_valid([2, 3]))
        self.assertTrue(g.is_path_valid([0, 2, 3]))
        self.assertFalse(g.is_path_valid([4, 2, 0]))
        self.assertTrue(g.is_path_valid([1]))
        self.assertRaises(IndexError, g.is_path_valid, [0, 7, 1])
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_is_path_valid2(self):
        g = read_graph('g2.txt')
        self.assertTrue(g.is_path_valid([0, 2]))
        self.assertTrue(g.is_path_valid([2, 3]))
        self.assertTrue(g.is_path_valid([0, 2, 3]))
        self.assertFalse(g.is_path_valid([0, 1, 8]))
        self.assertFalse(g.is_path_valid([0, 4, 3]))
        self.assertTrue(g.is_path_valid([1]))
        self.assertRaises(IndexError, g.is_path_valid, [0, 10, 1])
        self.validate_equality(read_graph('g2.txt'), g)

    def test_edge_weight1(self):
        import math
        g = read_graph('g1.txt')
        self.assertAlmostEqual(5.0, g.edge_weight(0, 1))
        self.assertAlmostEqual(2.5, g.edge_weight(4, 1))
        self.assertAlmostEqual(math.inf, g.edge_weight(0, 4))
        self.assertAlmostEqual(math.inf, g.edge_weight(4, 2))
        self.assertRaises(IndexError, g.edge_weight, 2, 7)
        self.assertRaises(IndexError, g.edge_weight, 7, 1)
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_edge_weight2(self):
        g = read_graph('g2.txt')
        self.assertAlmostEqual(5.0, g.edge_weight(0, 1))
        self.assertAlmostEqual(6.0, g.edge_weight(4, 1))
        self.assertAlmostEqual(math.inf, g.edge_weight(0, 9))
        self.assertAlmostEqual(math.inf, g.edge_weight(4, 5))
        self.assertRaises(IndexError, g.edge_weight, 2, 10)
        self.assertRaises(IndexError, g.edge_weight, 10, 1)
        self.validate_equality(read_graph('g2.txt'), g)

    def test_path_weight1(self):
        import math
        g = read_graph('g1.txt')
        self.assertAlmostEqual(2.0, g.path_weight([0, 2]))
        self.assertAlmostEqual(2.0, g.path_weight([2, 3]))
        self.assertAlmostEqual(4.0, g.path_weight([0, 2, 3]))
        self.assertAlmostEqual(math.inf, g.path_weight([3, 2, 4, 0]))
        self.assertAlmostEqual(0, g.path_weight([1]))
        self.assertRaises(IndexError, g.path_weight, [0, 7, 1])
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_path_weight2(self):
        g = read_graph('g2.txt')
        self.assertAlmostEqual(10, g.path_weight([0, 2]))
        self.assertAlmostEqual(2.0, g.path_weight([2, 3]))
        self.assertAlmostEqual(12, g.path_weight([0, 2, 3]))
        self.assertAlmostEqual(math.inf, g.path_weight([3, 2, 0, 7]))
        self.assertAlmostEqual(0, g.path_weight([1]))
        self.assertRaises(IndexError, g.path_weight, [0, 10, 1])
        self.validate_equality(read_graph('g2.txt'), g)

    def test_path_exists1(self):
        g = read_graph('g1.txt')
        for v in range(g.order):
            self.assertTrue(g.does_path_exist(v, v))
        self.assertTrue(g.does_path_exist(0, 2))
        self.assertTrue(g.does_path_exist(2, 3))
        self.assertTrue(g.does_path_exist(0, 3))
        self.assertRaises(IndexError, g.does_path_exist, 0, 7)
        self.assertRaises(IndexError, g.does_path_exist, 7, 0)
        self.validate_equality(read_graph('g1.txt'), g)
        
    def test_path_exists2(self):
        g = read_graph('g2.txt')
        for v in range(g.order):
            self.assertTrue(g.does_path_exist(v, v))
        self.assertTrue(g.does_path_exist(0, 2))
        self.assertTrue(g.does_path_exist(2, 3))
        self.assertTrue(g.does_path_exist(0, 3))
        self.assertTrue(g.does_path_exist(7, 9))
        self.assertFalse(g.does_path_exist(0, 9))
        self.assertFalse(g.does_path_exist(6, 7))
        self.assertRaises(IndexError, g.does_path_exist, 0, 10)
        self.assertRaises(IndexError, g.does_path_exist, 10, 0)
        self.validate_equality(read_graph('g2.txt'), g)

    def test_find_min_path1(self):
        g = read_graph('g1.txt')
        for v in range(g.order):
            self.assertAlmostEqual(0.0, g.path_weight(g.find_min_weight_path(v, v)))
        self.assertAlmostEqual(5.0, g.path_weight(g.find_min_weight_path(0, 1)))
        self.assertAlmostEqual(2.0, g.path_weight(g.find_min_weight_path(0, 2)))
        self.assertAlmostEqual(4.0, g.path_weight(g.find_min_weight_path(0, 3)))
        self.validate_equality(read_graph('g1.txt'), g)
    
    def test_find_min_path2(self):
        g = read_graph('g2.txt')
        for v in range(g.order):
            self.assertAlmostEqual(0.0, g.path_weight(g.find_min_weight_path(v, v)))
        self.assertAlmostEqual(5.0, g.path_weight(g.find_min_weight_path(0, 1)))
        self.assertAlmostEqual(10, g.path_weight(g.find_min_weight_path(0, 2)))
        self.assertAlmostEqual(8.0, g.path_weight(g.find_min_weight_path(0, 3)))
        self.assertRaises(ValueError, g.find_min_weight_path, 0, 9)
        self.validate_equality(read_graph('g2.txt'), g)

    def test_large_graph(self):
        g = Graph(101)
        # Path
        for i in range(100):
            g.insert_edge(i, (i + 1), i + 1)

        # Validate
        for i in range(101):
            for j in range(i + 1, 101):
                self.assertEqual((i + 1) == j, g.are_connected(i, j), '{0} -> {1}'.format(i, j))
                if (i + 1) == j:
                    self.assertTrue(g.are_connected(j, i), '{1} -> {0}'.format(i, j))
                else:
                    self.assertFalse(g.are_connected(j, i), '{1} -> {0}'.format(i, j))
                self.assertTrue(g.does_path_exist(i, j), '{0} -> {1}'.format(i, j))
                self.assertTrue(g.does_path_exist(j, i), '{1} -> {0}'.format(i, j))
                p = g.find_min_weight_path(i, j)
                self.assertEqual(j - i, len(p) - 1, '{0} -> {1}'.format(i, j))
        self.assertEqual(5050, g.path_weight(g.find_min_weight_path(0, 100)))

    def validate_equality(self, g1, g2):
        self.assertEqual(g1.order, g2.order)
        self.assertEqual(g1.size, g2.size)
        for i in range(g1.order):
            for j in range(g2.order):
                self.assertEqual(g1.are_connected(i, j), g2.are_connected(i, j), '{0}->{1}'.format(i, j))
                if g1.are_connected(i, j):
                    self.assertEqual(g1.edge_weight(i, j), g2.edge_weight(i, j), '{0}->{1}'.format(i, j))
                    
    def test_bipartite(self):
        g = read_graph('g1.txt')
        self.assertFalse(g.is_bipartite(), g)
        g = read_graph('g2.txt')
        self.assertFalse(g.is_bipartite(), g)
        g = read_graph('unicycle.txt')
        self.assertTrue(g.is_bipartite(), g)
        g = read_graph('tree.txt')
        self.assertTrue(g.is_bipartite(), g)
        g = read_graph('path.txt')
        self.assertTrue(g.is_bipartite(), g)


if __name__ == '__main__':
    unittest.main()
