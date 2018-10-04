#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pytotp import (
    Factor,
    Generator,
    Algorithm
)

class GeneratorTest(unittest.TestCase):

    def test_init_factor(self):
        factor = Factor()
        self.assertEqual(factor._digits, 6)
        self.assertEqual(factor._period, 30)
        factor = Factor(digits=4, period=15)
        self.assertEqual(factor._digits, 4)
        self.assertEqual(factor._period, 15)

    def test_init_generator(self):
        factor = Factor(digits=4, period=15)
        generator = Generator(factor, Algorithm.SHA1)
        self.assertIsNotNone(generator._factor)
        self.assertEqual(generator._algorithm, Algorithm.SHA1)
