import unittest

from WasRun import WasRun
from tests.TestCase import TestCase


class TestCaseTest(TestCase):
    def testrunning(self):
        test = WasRun("testmethod")
        assert (not test.wasRun)
        test.run()
        assert test.wasRun


TestCaseTest("testrunning").run()

if __name__ == '__main__':
    unittest.main()
