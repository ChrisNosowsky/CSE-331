#!/usr/bin/python3

import unittest

from Lis import *
from Main7 import read_file


class LisTests(unittest.TestCase):

    def test_subseq(self):
        s1 = [0, 2, 4, 5]
        s2 = [0, 4, 5]
        s3 = [0, 2, 4]
        self.assertTrue(verify_subseq(s1, s2))
        self.assertFalse(verify_subseq(s2, s1))
        self.assertTrue(verify_subseq(s1, s3))
        self.assertFalse(verify_subseq(s3, s1))
        self.assertFalse(verify_subseq(s2, s3))
        self.assertFalse(verify_subseq(s3, s2))

        self.assertTrue(verify_subseq(s1, s1))
        self.assertTrue(verify_subseq(s2, s2))
        self.assertTrue(verify_subseq(s3, s3))

        self.assertTrue(verify_subseq(s1, []))
        self.assertTrue(verify_subseq(s2, []))
        self.assertTrue(verify_subseq(s3, []))

    def test_subseq_str(self):
        self.assertTrue(verify_subseq('sale', 'ale'))
        self.assertFalse(verify_subseq('ale', 'sale'))
        self.assertFalse(verify_subseq('kale', 'sale'))
        self.assertFalse(verify_subseq('sale', 'kale'))
        for l in 'sale':
            self.assertTrue(verify_subseq('sale', l))

    def test_increasing(self):
        self.assertTrue(verify_increasing(range(10)))
        self.assertTrue(verify_increasing([]))
        self.assertFalse(verify_increasing(list(reversed(range(10)))))
        self.assertTrue(verify_increasing([2, 4, 6, 8, 10]))
        self.assertFalse(verify_increasing([2, 4, 8, 6, 10]))
        self.assertFalse(verify_increasing([3, 2, 4, 6, 8, 10]))
        self.assertFalse(verify_increasing([2, 4, 6, 8, 10, 9]))
        self.assertFalse(verify_increasing([2, 4, 6, 8, 10, 10]))

    def test_increasing_str(self):
        self.assertTrue(verify_increasing('abcdefg'))
        self.assertTrue(verify_increasing('aceg'))
        self.assertFalse(verify_increasing('gec'))
        self.assertTrue(verify_increasing('g'))
        self.assertTrue(verify_increasing(''))
        self.assertFalse(verify_increasing('abb'))

    def test_lis(self):
        seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        copy = seq[:]
        result = find_lis(seq)
        self.assertListEqual(copy, seq)
        self.assertTrue(verify_increasing(result), str(result))
        self.assertTrue(verify_subseq(seq, result), str(result))
        self.assertEqual(6, len(result), str(result))

    def test_lis_string(self):
        text = 'antidisestablishmentarianism'
        result = find_lis(text)
        self.assertTrue(verify_increasing(result), str(result))
        self.assertTrue(verify_subseq(text, result), str(result))
        self.assertEqual(8, len(result), str(result))
        
    def test_lis_e(self):
        seq = read_file('e.txt')
        copy = seq[:]
        result = find_lis(seq)
        self.assertListEqual(copy, seq)
        self.assertTrue(verify_increasing(result), str(result))
        self.assertTrue(verify_subseq(seq, result), str(result))
        self.assertEqual(6, len(result), str(result))

    def test_lis_pi(self):
        seq = read_file('pi.txt')
        copy = seq[:]
        result = find_lis(seq)
        self.assertListEqual(copy, seq)
        self.assertTrue(verify_increasing(result), str(result))
        self.assertTrue(verify_subseq(seq, result), str(result))
        self.assertEqual(7, len(result), str(result))

    def test_romeo(self):
        seq = read_file('romeo-intro.txt')
        copy = seq[:]
        result = find_lis(seq)
        self.assertListEqual(copy, seq)
        self.assertTrue(verify_increasing(result), str(result))
        self.assertTrue(verify_subseq(seq, result), str(result))
        self.assertEqual(18, len(result), str(result))
        
    def test_large_size(self):
        from random import shuffle
        n = 100
        for i in range(10):
            seq = list(range(n * n + 1))
            shuffle(seq)
            rev = list(reversed(seq))
            result = find_lis(seq)
            self.assertTrue(verify_increasing(result), str(result))
            self.assertTrue(verify_subseq(seq, result), str(result))
            rev_result = find_lis(rev)
            self.assertTrue(verify_increasing(rev_result), str(rev_result))
            self.assertTrue(verify_subseq(rev, rev_result), str(rev_result))
            max_lis = max(len(result), len(rev_result))
            self.assertLessEqual(n + 1, max_lis)


if __name__ == '__main__':
    unittest.main()
