#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
from pytotp import (
    Factor,
    Generator,
    Algorithm,
    base32helper
)

class GeneratorTest(unittest.TestCase):

    def test_init_factor(self):
        factor = Factor()
        self.assertEqual(factor._digits, 6)
        self.assertEqual(factor._period, 30)
        factor = Factor(digits=4, period=15)
        self.assertEqual(factor._digits, 4)
        self.assertEqual(factor._period, 15)

    def test_init_generator_success(self):
        factor = Factor(digits=6, period=15)
        generator = Generator(factor, Algorithm.SHA1, base32helper.encode('data'))
        self.assertIsNotNone(generator._factor)
        self.assertEqual(generator._algorithm, Algorithm.SHA1)

    def test_init_generator_fail(self):
        factor = Factor(digits=4, period=15)
        with pytest.raises(Exception) as exception:
            Generator(factor, Algorithm.SHA1, base32helper.encode('data'))
        assert str(exception.value) == 'Invalid given factor'
