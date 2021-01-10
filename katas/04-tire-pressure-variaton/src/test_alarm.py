import unittest
from unittest.mock import Mock

from src.alarm import Alarm, Display
from src.sensor import Sensor


class AlarmTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_activate_alarm(self):
        attrs = {'pop_next_pressure_psi_value.return_value': 22}
        sensor = Mock(spec=Sensor, **attrs)
        display = Mock(spec=Display)
        self._alarm = Alarm(sensor, display)

        self._alarm.check()

        display.print.assert_called_with("Alarm activated!")

    def test_alarm_no_activated(self):
        attrs = {'pop_next_pressure_psi_value.return_value': 21}
        sensor = Mock(spec=Sensor, **attrs)
        display = Mock(spec=Display)
        self._alarm = Alarm(sensor, display)

        self._alarm.check()

        display.print.assert_not_called()
