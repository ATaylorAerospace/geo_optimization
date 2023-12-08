import unittest
import numpy as np
from geo_orbit_thruster_optimization.py import calculate_thrust, estimate_power_consumption, optimize_thruster_parameters

class TestThrusterOptimization(unittest.TestCase):

    def test_calculate_thrust(self):
        # Test with known values
        specific_impulse = 1000  # seconds
        mass_flow_rate = 0.001  # kg/s
        expected_thrust = 9.81  # Newtons (since g0 is 9.81 m/s^2)
        result = calculate_thrust(specific_impulse, mass_flow_rate)
        self.assertAlmostEqual(result, expected_thrust, places=2)

    def test_estimate_power_consumption(self):
        # Test with known values
        specific_impulse = 1000  # seconds
        mass_flow_rate = 0.001  # kg/s
        efficiency = 0.5
        # Calculate expected power consumption
        g0 = 9.81  # m/s^2
        expected_power = mass_flow_rate * specific_impulse * g0 / efficiency
        result = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency)
        self.assertAlmostEqual(result, expected_power, places=2)

    def test_optimize_thruster_parameters(self):
        # Since the optimization function is complex, we mainly test if it returns the correct tuple structure
        result = optimize_thruster_parameters()
        self.assertEqual(len(result), 4)
        # Check if the types of the returned values are correct
        self.assertIsInstance(result[0], float)  # Thrust
        self.assertIsInstance(result[1], float)  # Specific Impulse
        self.assertIsInstance(result[2], float)  # Mass Flow Rate
        self.assertIsInstance(result[3], float)  # Power Consumption

if __name__ == '__main__':
    unittest.main()