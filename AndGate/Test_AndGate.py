# -*- coding: utf8 -*-
__version__ = '1.0'
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

import unittest
from AndGate import AndGate

class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        o = AndGate()
        o.Input0 = False
        o.Input1 = False
        o.execute()
        self.assertFalse(o.Output, "Class OrGate: Testcase 1 failed.")

    def testcase_02(self):
        o = AndGate()
        o.Input0 = True
        o.Input1 = False
        o.execute()
        self.assertFalse(o.Output, "Class OrGate: Testcase 2 failed.")

    def testcase_03(self):
        o = AndGate()
        o.Input0 = False
        o.Input1 = True
        o.execute()
        self.assertFalse(o.Output, "Class OrGate: Testcase 3 failed.")

    def testcase_04(self):
        o = AndGate()
        o.Input0 = True
        o.Input1 = True
        o.execute()
        self.assertTrue(o.Output, "Class OrGate: Testcase 4 failed.")

if __name__ == "__main__":
    unittest.main()