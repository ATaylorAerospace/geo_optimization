import unittest
import numpy as np
from thruster_optimization import calculate_thrust, estimate_power_consumption, optimize_thruster_parameters

class TestThrusterOptimization(unittest.TestCase):

    def test_calculate_thrust(self):
        specific_impulse = 3000
        mass_flow_rate = 0.0002
        expected_thrust = 58.86
        actual_thrust = calculate_thrust(specific_impulse, mass_flow_rate)
        self.assertEqual(actual_thrust, expected_thrust)

    def test_estimate_power_consumption(self):
        specific_impulse = 4500
        mass_flow_rate = 0.0003
        expected_power_consumption = 19543.333333333332
        actual_power_consumption = estimate_power_consumption(specific_impulse, mass_flow_rate)
        self.assertEqual(actual_power_consumption, expected_power_consumption)

    def test_optimize_thruster_parameters(self):
        expected_optimal_thrust = 154.8549
        expected_optimal_specific_impulse = 4000
        expected_optimal_mass_flow_rate = 0.0003
        expected_optimal_power_consumption = 14645.555555555554
        actual_optimal_results = optimize_thruster_parameters()
        actual_optimal_thrust, actual_optimal_specific_impulse, actual_optimal_mass_flow_rate, actual_optimal_power_consumption = actual_optimal_results
        self.assertEqual(actual_optimal_thrust, expected_optimal_thrust)
        self.assertEqual(actual_optimal_specific_impulse, expected_optimal_specific_impulse)
        self.assertEqual(actual_optimal_mass_flow_rate, expected_optimal_mass_flow_rate)
        self.assertEqual(actual_optimal_power_consumption, expected_optimal_power_consumption)

if __name__ == '__main__':
    unittest.main()
