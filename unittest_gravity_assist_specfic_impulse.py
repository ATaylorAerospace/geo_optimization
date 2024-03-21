import unittest
import numpy as np
from gravity_assist_specific_impulse import calculate_thrust, estimate_power_consumption, optimize_thruster_parameters

class TestGravityAssistSpecificImpulse(unittest.TestCase):

    def test_calculate_thrust(self):
        """Test the calculate_thrust function."""
        specific_impulse = 300  # seconds
        mass_flow_rate = 0.5  # kg/s
        expected_thrust = specific_impulse * mass_flow_rate * 9.81
        self.assertAlmostEqual(calculate_thrust(specific_impulse, mass_flow_rate), expected_thrust)

    def test_estimate_power_consumption(self):
        """Test the estimate_power_consumption function."""
        specific_impulse = 300  # seconds
        mass_flow_rate = 0.5  # kg/s
        efficiency = 0.7
        expected_power = (specific_impulse * 9.81 / efficiency) * mass_flow_rate
        self.assertAlmostEqual(estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency), expected_power)

    def test_optimize_thruster_parameters(self):
        """Test the optimize_thruster_parameters function."""
        results = optimize_thruster_parameters()
        self.assertIsInstance(results, dict)
        self.assertTrue("Optimal Thrust" in results)
        self.assertTrue("Optimal Specific Impulse" in results)
        self.assertTrue("Optimal Mass Flow Rate" in results)
        self.assertTrue("Estimated Power Consumption" in results)

if __name__ == '__main__':
    unittest.main()
