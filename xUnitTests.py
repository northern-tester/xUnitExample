import unittest

from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testrunning(self):
        test = WasRun("testmethod")
        assert (not test.wasRun)
        test.run()
        assert test.wasRun


TestCaseTest("testrunning").run()

if __name__ == '__main__':
    unittest.main()
