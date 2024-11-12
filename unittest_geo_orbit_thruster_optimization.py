import unittest
from geo_orbit_thruster_optimization import (
    calculate_thrust,
    estimate_power_consumption,
    optimize_thruster_parameters,
)

class TestGeoOrbitThrusterOptimization(unittest.TestCase):

    def setUp(self):
        """Initialize common variables for the tests."""
        self.specific_impulse = 250  # in seconds
        self.mass_flow_rate = 0.01   # in kg/s
        self.efficiency = 0.5        # dimensionless

    def test_calculate_thrust(self):
        """Test the calculate_thrust function with predefined inputs."""
        expected_thrust = 9.81 * self.specific_impulse * self.mass_flow_rate
        actual_thrust = calculate_thrust(self.specific_impulse, self.mass_flow_rate)
        self.assertAlmostEqual(actual_thrust, expected_thrust, places=3)

    def test_estimate_power_consumption(self):
        """Test the estimate_power_consumption function with predefined inputs."""
        expected_power = (
            (0.5 * (self.mass_flow_rate * (9.81 * self.specific_impulse) ** 2)) / self.efficiency
        )
        actual_power = estimate_power_consumption(
            self.specific_impulse, self.mass_flow_rate, self.efficiency
        )
        self.assertAlmostEqual(actual_power, expected_power, places=0)

    def test_optimize_thruster_parameters(self):
        """Test the optimize_thruster_parameters function for valid output ranges."""
        optimal_thrust, optimal_si, optimal_mfr, optimal_pc = optimize_thruster_parameters()
        # Ensure that the returned values meet expected criteria
        self.assertGreater(optimal_thrust, 0)
        self.assertTrue(1000 <= optimal_si <= 4000)
        self.assertTrue(0.0001 <= optimal_mfr <= 0.001)
        self.assertGreater(optimal_pc, 0)

if __name__ == '__main__':
    unittest.main()

