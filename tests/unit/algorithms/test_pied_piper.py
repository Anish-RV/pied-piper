"""Tests for pied-piper/pied-piper.py."""
import unittest

class TestPiedPiper(unittest.TestCase):

    def test_upper(self): # example of a unit test that tests for if the second argument is capitalized
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()          
    
"""//binary file //text file //both should have repeating non-repeating"""