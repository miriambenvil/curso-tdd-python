from sensor import Sensor


class Alarm:
    def __init__(self):
        self._LowPressureThreshold = 17
        self._HighPressureThreshold = 21

        self._sensor = Sensor()
        self._display = Display()
        self._alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()

        if (psi_pressure_value < self._LowPressureThreshold) or (self._HighPressureThreshold < psi_pressure_value):
            if not self._is_alarm_on():
                self._alarm_on = True
                self._display.print_message("Alarm activated!")

        else:
            if self._is_alarm_on():
                self._display.print_message("Alarm deactivated!")

    def _is_alarm_on(self):
        return self._alarm_on


class Display:
    def print_message(self, msg):
        print(msg)
