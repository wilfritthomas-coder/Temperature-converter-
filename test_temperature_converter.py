"""
Unit Tests for Temperature Converter
Tests all conversion functions with standard and edge-case values.
"""

import unittest
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestCelsiusToFahrenheit(unittest.TestCase):

    def test_boiling_point(self):
        """100°C should equal 212°F"""
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0, places=2)

    def test_freezing_point(self):
        """0°C should equal 32°F"""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0, places=2)

    def test_body_temperature(self):
        """37°C should equal 98.6°F"""
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

    def test_absolute_zero(self):
        """-273.15°C should equal -459.67°F"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=1)

    def test_negative_value(self):
        """-40°C should equal -40°F (the crossover point)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0, places=2)

    def test_fractional_value(self):
        """36.6°C should convert correctly"""
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=1)


class TestFahrenheitToCelsius(unittest.TestCase):

    def test_boiling_point(self):
        """212°F should equal 100°C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0, places=2)

    def test_freezing_point(self):
        """32°F should equal 0°C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0, places=2)

    def test_body_temperature(self):
        """98.6°F should equal 37°C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=1)

    def test_negative_value(self):
        """-40°F should equal -40°C (the crossover point)"""
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0, places=2)

    def test_room_temperature(self):
        """72°F (room temp) should be approximately 22.2°C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(72), 22.22, places=1)


class TestRoundTrip(unittest.TestCase):

    def test_c_to_f_and_back(self):
        """Converting C → F → C should return the original value"""
        original = 25.0
        result = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
        self.assertAlmostEqual(result, original, places=5)

    def test_f_to_c_and_back(self):
        """Converting F → C → F should return the original value"""
        original = 77.0
        result = celsius_to_fahrenheit(fahrenheit_to_celsius(original))
        self.assertAlmostEqual(result, original, places=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
