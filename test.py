import unittest
from pyls import listout, parse_arguments

class TestPyls(unittest.TestCase):
    def test_parse_arguments(self):
        args = parse_arguments()
        self.assertIsInstance(args, argparse.Namespace)

    def test_listout(self):
        # Mock os.listdir and other os functions to test listout behavior
        pass

if __name__ == "__main__":
    unittest.main()
