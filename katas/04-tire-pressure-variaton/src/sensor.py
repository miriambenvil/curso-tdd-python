from random import Random


class Sensor:

    def __init__(self):
        self.OFFSET = 16

    def pop_next_pressure_psi_value(self):
        pressure_telemetry_value = self._sample_pressure()
        return self.OFFSET + pressure_telemetry_value

    @staticmethod
    def _sample_pressure():
        generator = Random()
        pressure_telemetry_value = 6 * generator.random() * generator.random()
        return pressure_telemetry_value
