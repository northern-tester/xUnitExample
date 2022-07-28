from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasSetup = None
        self.wasRun = None
        TestCase.__init__(self, name)

    def setup(self):
        self.wasRun = None
        self.wasSetup = 1

    def testmethod(self):
        self.wasRun = 1
