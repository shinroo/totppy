#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
from pytotp import (
    Token,
    Generator,
    Factor,
    Algorithm,
    base32helper
)

class TokenTest(unittest.TestCase):

    def test_init(self):
        factor = Factor(6, 10)
        secret = base32helper.encode('secret')
        generator = Generator(factor, Algorithm.SHA1, secret)
        token = Token(generator, 'name', 'issuer')
        self.assertIsNotNone(token)
        self.assertEqual(token._generator, generator)
        self.assertEqual(token._name, 'name')
        self.assertEqual(token._issuer, 'issuer')
