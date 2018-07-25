from .context import numplot
import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(numplot.hmm())

if __name__ == '__main__':
    unittest.main()
