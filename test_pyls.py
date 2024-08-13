import unittest
import os
import time
import argparse
from unittest.mock import patch
from pyls import parse_arguments, format_entry, format_long_entry

class TestPyls(unittest.TestCase):
    
    @patch('sys.argv', ['pyls.py'])
    def test_parse_arguments_no_flags(self):
        args = parse_arguments()
        self.assertFalse(args.long)
        self.assertFalse(args.classify)

    @patch('sys.argv', ['pyls.py', '-l'])
    def test_parse_arguments_long_flag(self):
        args = parse_arguments()
        self.assertTrue(args.long)
        self.assertFalse(args.classify)

    @patch('sys.argv', ['pyls.py', '-F'])
    def test_parse_arguments_classify_flag(self):
        args = parse_arguments()
        self.assertFalse(args.long)
        self.assertTrue(args.classify)

    @patch('sys.argv', ['pyls.py', '-l', '-F'])
    def test_parse_arguments_both_flags(self):
        args = parse_arguments()
        self.assertTrue(args.long)
        self.assertTrue(args.classify)

    def test_format_entry_classify_directory(self):
        if os.path.exists('test_dir'):
            os.rmdir('test_dir')
        os.mkdir('test_dir')
        args = argparse.Namespace(long=False, classify=True)
        self.assertEqual(format_entry('test_dir', args), "test_dir/")
        os.rmdir('test_dir')

    def test_format_entry_classify_executable(self):
        open('test_exec', 'w').close()
        os.chmod('test_exec', 0o755)
        args = argparse.Namespace(long=False, classify=True)
        self.assertEqual(format_entry('test_exec', args), "test_exec*")
        os.remove('test_exec')

    def test_format_entry_long(self):
        entry = 'test_file'
        open(entry, 'w').close()
        args = argparse.Namespace(long=True, classify=False)
        formatted_entry = format_entry(entry, args)
        self.assertIn(entry, formatted_entry)
        os.remove(entry)

    def test_format_long_entry(self):
        entry = 'test_file'
        open(entry, 'w').close()
        file_stat = os.stat(entry)
        permissions = oct(file_stat.st_mode)[-3:]
        file_size = file_stat.st_size
        modification_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(file_stat.st_mtime))
        expected_output = f"{permissions} {file_size} {modification_time} {entry}"
        self.assertEqual(format_long_entry(entry), expected_output)
        os.remove(entry)

if __name__ == "__main__":
    unittest.main()
