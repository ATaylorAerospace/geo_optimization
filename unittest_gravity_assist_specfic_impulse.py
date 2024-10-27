import unittest
import numpy as np

# Constants for tests
G0 = 9.81  # Standard gravity, m/s^2

def calculate_thrust(specific_impulse, mass_flow_rate):
    return specific_impulse * mass_flow_rate * G0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency=0.7):
    energy_per_kg = specific_impulse * G0 / efficiency
    return mass_flow_rate * energy_per_kg

def optimize_thruster_parameters(gravity_assist_multiplier=1.1):
    specific_impulse_range = np.linspace(2000, 5000, 50)
    mass_flow_rate_range = np.linspace(0.00005, 0.0005, 50)

    spi_grid, mass_grid = np.meshgrid(specific_impulse_range, mass_flow_rate_range)
    spi_values = spi_grid.ravel()
    mass_values = mass_grid.ravel()

    thrust_values = calculate_thrust(spi_values, mass_values) * gravity_assist_multiplier
    power_values = estimate_power_consumption(spi_values, mass_values)

    ratio_values = thrust_values / power_values
    optimal_idx = np.argmax(ratio_values)

    optimal_spi = spi_values[optimal_idx]
    optimal_mass = mass_values[optimal_idx]
    optimal_thrust = thrust_values[optimal_idx]
    optimal_power = power_values[optimal_idx]

    return {
        "Optimal Thrust": optimal_thrust,
        "Optimal Specific Impulse": optimal_spi,
        "Optimal Mass Flow Rate": optimal_mass,
        "Estimated Power Consumption": optimal_power
    }

class TestThrusterCalculations(unittest.TestCase):
    def test_calculate_thrust(self):
        specific_impulse = 2500  # seconds
        mass_flow_rate = 0.0002  # kg/s
        expected_thrust = specific_impulse * mass_flow_rate * G0
        self.assertAlmostEqual(calculate_thrust(specific_impulse, mass_flow_rate), expected_thrust, places=5)

    def test_estimate_power_consumption(self):
        specific_impulse = 2500  # seconds
        mass_flow_rate = 0.0002  # kg/s
        efficiency = 0.75
        energy_per_kg = specific_impulse * G0 / efficiency
        expected_power = mass_flow_rate * energy_per_kg
        self.assertAlmostEqual(estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency), expected_power, places=5)

    def test_optimize_thruster_parameters(self):
        result = optimize_thruster_parameters()
        self.assertGreater(result['Optimal Thrust'], 0)
        self.assertGreater(result['Optimal Specific Impulse'], 0)
        self.assertGreater(result['Optimal Mass Flow Rate'], 0)
        self.assertGreater(result['Estimated Power Consumption'], 0)
        self.assertTrue(result['Optimal Thrust'] > result['Estimated Power Consumption'], "Thrust should be greater than power consumption for optimization to be meaningful.")

if __name__ == '__main__':
    unittest.main()
