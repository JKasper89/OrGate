import unittest

from Logfunc import AndGate


class AndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = AndGate()

        a.input0 = False

        a.input1 = False

        a.execute()

        self.assertFalse(a.output, "AndGate, Testcase 01 failed!")

    def testcase_02(self):
        a = AndGate()

        a.input0 = True

        a.input1 = False

        a.execute()

        self.assertFalse(a.output, "AndGate, Testcase 02 failed!")

    def testcase_03(self):
        a = AndGate()

        a.input0 = False

        a.input1 = True

        a.execute()

        self.assertFalse(a.output, "AndGate, Testcase 03 failed!")

    def testcase_04(self):
        a = AndGate()

        a.input0 = True

        a.input1 = True

        a.execute()

        self.assertTrue(a.output, "AndGate, Testcase 04 failed!")


if __name__ == "__main__":
    unittest.main() 