#!/usr/bin/env python3
import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
        def test_basic(self):
                testCase = [None, "Bree", "Campbell"]
                expected = "breee@abc.edu"
                self.assertEqual(find_email(testCase), expected)

        def test_one_name(self):
                testCase = [None, "John"]
                expected = "Missing Parameters"
                self.assertEqual(find_email(testCase),expected)
        def test_two_name(self):
                testcase = [None, "Roy","Cooper"]
                expected = "No email address found"
                self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
        unittest.main()