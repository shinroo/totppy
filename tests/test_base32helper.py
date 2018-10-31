#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from totppy import base32helper

class Base32HelperTest(unittest.TestCase):

    def test_base32encode(self):
        base32_encoded_data = base32helper.encode('testMessage')
        self.assertEqual(base32_encoded_data, b'ORSXG5CNMVZXGYLHMU======')

    def test_base32decode(self):
        base32_encoded_data = base32helper.encode('testMessage')
        self.assertEqual(base32_encoded_data, b'ORSXG5CNMVZXGYLHMU======')
        decoded_str = base32helper.decode(base32_encoded_data)
        self.assertEqual(decoded_str, 'testMessage')
