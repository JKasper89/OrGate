import unittest

from Logfunc2 import OrGate


class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        a = OrGate()

        a.input0 = False

        a.input1 = False

        a.execute()

        self.assertFalse(a.output, "AndGate, Testcase 01 failed!")

    def testcase_02(self):
        a = OrGate()

        a.input0 = True

        a.input1 = False

        a.execute()

        self.assertTrue(a.output, "AndGate, Testcase 02 failed!")

    def testcase_03(self):
        a = OrGate()

        a.input0 = False

        a.input1 = True

        a.execute()

        self.assertTrue(a.output, "AndGate, Testcase 03 failed!")

    def testcase_04(self):
        a = OrGate()

        a.input0 = True

        a.input1 = True

        a.execute()

        self.assertTrue(a.output, "AndGate, Testcase 04 failed!")


if __name__ == "__maiWn__":
    unittest.main()