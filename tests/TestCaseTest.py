import unittest

from WasRun import WasRun


class TestCaseTest(unittest.TestCase):

    def setup(self):
        self.test = WasRun("testmethod")

    def testrunning(self):
        test = WasRun("testmethod")
        test.run()
        assert test.wasRun

    def testsetup(self):
        test = WasRun("testmethod")
        test.run()
        assert test.wasSetup


TestCaseTest("testrunning").run()

if __name__ == '__main__':
    unittest.main()