# -*- coding: utf8 -*-
__version__ = '1.0'
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

import unittest
from NotGate import NotGate

class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        o = NotGate()
        o.Input = False
        o.execute()
        self.assertTrue(o.Output, "Class NotGate: Testcase 1 failed.")

    def testcase_02(self):
        o = NotGate()
        o.Input = True
        o.execute()
        self.assertFalse(o.Output, "Class NotGate: Testcase 2 failed.")

if __name__ == "__main__":
    unittest.main()