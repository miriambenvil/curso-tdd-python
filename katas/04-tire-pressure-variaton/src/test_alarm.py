import unittest

from src.alarm import Alarm


class AlarmTest(unittest.TestCase):
    def setUp(self):
        self._alarm = Alarm()

    def test_run_alarm(self):
        self._alarm.check()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
