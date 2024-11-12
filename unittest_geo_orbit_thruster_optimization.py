import unittest
import numpy as np
from scipy.optimize import minimize

# Import the original functions
from your_script import calculate_thrust, estimate_power_consumption, optimize_thruster_parameters

class TestThrusterFunctions(unittest.TestCase):

    def test_calculate_thrust(self):
        # Test nominal values
        self.assertAlmostEqual(calculate_thrust(3000, 0.01), 294.3, places=2)
        self.assertAlmostEqual(calculate_thrust(2000, 0.001), 19.62, places=2)
        # Test zero mass flow rate
        self.assertEqual(calculate_thrust(3000, 0), 0)
        # Test negative inputs
        self.assertRaises(ValueError, calculate_thrust, -3000, 0.01)
        self.assertRaises(ValueError, calculate_thrust, 3000, -0.01)

    def test_estimate_power_consumption(self):
        # Test nominal values
        self.assertAlmostEqual(estimate_power_consumption(3000, 0.01, 0.5), 5886.0, places=2)
        self.assertAlmostEqual(estimate_power_consumption(2000, 0.001, 0.7), 2802.86, places=2)
        # Test zero mass flow rate
        self.assertEqual(estimate_power_consumption(3000, 0, 0.5), 0)
        # Test zero efficiency (should raise an exception due to divide by zero)
        self.assertRaises(ZeroDivisionError, estimate_power_consumption, 3000, 0.01, 0)
        # Test negative inputs
        self.assertRaises(ValueError, estimate_power_consumption, -3000, 0.01, 0.5)
        self.assertRaises(ValueError, estimate_power_consumption, 3000, -0.01, 0.5)
        self.assertRaises(ValueError, estimate_power_consumption, 3000, 0.01, -0.5)

    def test_optimize_thruster_parameters(self):
        # Run optimization and check results
        optimal_thrust, optimal_specific_impulse, optimal_mass_flow_rate, optimal_power_consumption = optimize_thruster_parameters()
        
        # Check if the returned optimal parameters are within expected ranges
        self.assertGreater(optimal_specific_impulse, 1000)
        self.assertLess(optimal_specific_impulse, 4000)
        self.assertGreater(optimal_mass_flow_rate, 0.0001)
        self.assertLess(optimal_mass_flow_rate, 0.001)
        
        # Ensure thrust and power consumption are positive
        self.assertGreater(optimal_thrust, 0)
        self.assertGreater(optimal_power_consumption, 0)

    def test_optimization_with_scipy(self):
        # Test optimization to minimize power consumption per unit thrust
        def objective(params):
            specific_impulse, mass_flow_rate = params
            thrust = calculate_thrust(specific_impulse, mass_flow_rate)
            power = estimate_power_consumption(specific_impulse, mass_flow_rate)
            return power / thrust

        bounds = [(1000, 4000), (0.0001, 0.001)]
        result = minimize(objective, x0=[2000, 0.0005], bounds=bounds)
        
        # Ensure the optimization was successful
        self.assertTrue(result.success)
        
        # Ensure optimized parameters are within expected ranges
        specific_impulse, mass_flow_rate = result.x
        self.assertGreaterEqual(specific_impulse, 1000)
        self.assertLessEqual(specific_impulse, 4000)
        self.assertGreaterEqual(mass_flow_rate, 0.0001)
        self.assertLessEqual(mass_flow_rate, 0.001)

if __name__ == '__main__':
    unittest.main()


