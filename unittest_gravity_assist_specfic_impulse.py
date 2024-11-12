import unittest
import numpy as np

# Import the functions from the script
# Assuming the script is saved as 'thruster_module.py'
# If the script is in the same file, you can omit the import statements
from thruster_module import (
    calculate_thrust,
    estimate_power_consumption,
    optimize_thruster_parameters,
    G0
)

class TestThrusterCalculations(unittest.TestCase):

    def test_calculate_thrust(self):
        """Test the calculate_thrust function with known values."""
        specific_impulse = 3000  # seconds
        mass_flow_rate = 0.0001  # kg/s
        expected_thrust = specific_impulse * mass_flow_rate * G0
        result = calculate_thrust(specific_impulse, mass_flow_rate)
        self.assertAlmostEqual(result, expected_thrust, places=6)

    def test_estimate_power_consumption(self):
        """Test the estimate_power_consumption function with known values."""
        specific_impulse = 3000  # seconds
        mass_flow_rate = 0.0001  # kg/s
        efficiency = 0.7
        V_e = specific_impulse * G0
        expected_power = 0.5 * mass_flow_rate * V_e**2 / efficiency
        result = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency)
        self.assertAlmostEqual(result, expected_power, places=6)

    def test_optimize_thruster_parameters(self):
        """Test the optimize_thruster_parameters function for expected output."""
        results = optimize_thruster_parameters()
        # Check if all expected keys are in the result dictionary
        expected_keys = {
            "Optimal Thrust",
            "Optimal Specific Impulse",
            "Optimal Mass Flow Rate",
            "Estimated Power Consumption"
        }
        self.assertTrue(expected_keys.issubset(results.keys()))
        # Check if the values are within expected ranges
        self.assertGreater(results["Optimal Thrust"], 0)
        self.assertGreater(results["Optimal Specific Impulse"], 0)
        self.assertGreater(results["Optimal Mass Flow Rate"], 0)
        self.assertGreater(results["Estimated Power Consumption"], 0)

    def test_efficiency_effect(self):
        """Test the effect of efficiency on power consumption."""
        specific_impulse = 3000  # seconds
        mass_flow_rate = 0.0001  # kg/s
        efficiency_low = 0.5
        efficiency_high = 0.9
        power_low_eff = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency_low)
        power_high_eff = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency_high)
        self.assertGreater(power_low_eff, power_high_eff)

    def test_gravity_assist_multiplier(self):
        """Test the gravity assist multiplier effect in optimize_thruster_parameters."""
        results_no_assist = optimize_thruster_parameters(gravity_assist_multiplier=1.0)
        results_with_assist = optimize_thruster_parameters(gravity_assist_multiplier=1.1)
        self.assertGreater(
            results_with_assist["Optimal Thrust"],
            results_no_assist["Optimal Thrust"]
        )

if __name__ == "__main__":
    unittest.main()
