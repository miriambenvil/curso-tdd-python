from sensor import Sensor


class Display:
    def print(self, msg):
        print(msg)


class Alarm:
    def __init__(self, sensor=Sensor(), display=Display()):
        self._LowPressureThreshold = 17
        self._HighPressureThreshold = 21

        self._sensor = sensor
        self._display = display
        self._alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()

        if (psi_pressure_value < self._LowPressureThreshold) or (self._HighPressureThreshold < psi_pressure_value):
            if not self._is_alarm_on():
                self._alarm_on = True
                self._display.print("Alarm activated!")

        else:
            if self._is_alarm_on():
                self._display.print("Alarm deactivated!")

    def _is_alarm_on(self):
        return self._alarm_on
