from datetime import datetime

from utils.functions import change_time
import unittest


class TestUtils(unittest.TestCase):
    def test_change_time(self):
        """
        Case: set datetime value and change time there.
        Expect: process finished success.
        """
        now = datetime.utcnow()
        test_time = datetime(now.year, now.month, now.day, 15, 30)
        self.assertEqual(test_time.hour, 15)
        self.assertEqual(test_time.minute, 30)
        new_time = change_time(test_time, hours=2, minutes=10)
        self.assertEqual(new_time.hour, 13)
        self.assertEqual(new_time.minute, 20)

    def test_change_time_wrong_kwargs_key(self):
        """
        Case: set datetime value and change time there with wrong key.
        Expect: process failed.
        """
        now = datetime.utcnow()
        test_time = datetime(now.year, now.month, now.day, 15, 30)
        self.assertEqual(test_time.hour, 15)
        self.assertEqual(test_time.minute, 30)
        with self.assertRaises(TypeError):
            change_time(test_time, _hours=2, _minutes=10)

    def test_change_time_wrong_kwargs_value(self):
        """
        Case: set datetime value and change time there with wrong value.
        Expect: process failed.
        """
        now = datetime.utcnow()
        test_time = datetime(now.year, now.month, now.day, 15, 30)
        self.assertEqual(test_time.hour, 15)
        self.assertEqual(test_time.minute, 30)
        with self.assertRaises(TypeError):
            change_time(test_time, hours='string')
