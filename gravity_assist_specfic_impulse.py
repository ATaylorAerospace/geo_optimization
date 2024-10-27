# import numpy as np

# Constants
G0 = 9.81  # Standard gravity, m/s^2

def calculate_thrust(specific_impulse, mass_flow_rate):
    """Calculate thrust given specific impulse and mass_flow_rate.
    Parameters:
    - specific_impulse: Specific impulse of the thruster (s).
    - mass_flow_rate: Mass flow rate of the propellant (kg/s).
    Returns:
    - Thrust produced by the thruster (N).
    """
    return specific_impulse * mass_flow_rate * G0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency=0.7):
    """Estimate power consumption of the thruster based on its specific impulse and mass flow rate.
    Parameters:
    - specific_impulse: Specific impulse of the thruster (s).
    - mass_flow_rate: Mass flow rate of the propellant (kg/s).
    - efficiency: Efficiency of the thruster (dimensionless, default=0.7).
    Returns:
    - Estimated power consumption (W).
    """
    energy_per_kg = specific_impulse * G0 / efficiency
    return mass_flow_rate * energy_per_kg

def optimize_thruster_parameters(gravity_assist_multiplier=1.1):
    """Find optimal thruster parameters to maximize thrust-to-power ratio.
    Parameters:
    - gravity_assist_multiplier: Multiplier to simulate gravity assist effect (dimensionless, default=1.1).
    Returns:
    - Dictionary containing optimal values for thrust, specific impulse, mass flow rate, and power consumption.
    """
    specific_impulse_range = np.linspace(2000, 5000, 50)
    mass_flow_rate_range = np.linspace(0.00005, 0.0005, 50)

    spi_grid, mass_grid = np.meshgrid(specific_impulse_range, mass_flow_rate_range)
    spi_values = spi_grid.ravel()
    mass_values = mass_grid.ravel()

    # Vectorized calculation of thrust and power consumption
    thrust_values = calculate_thrust(spi_values, mass_values) * gravity_assist_multiplier
    power_values = estimate_power_consumption(spi_values, mass_values)

    # Calculate thrust-to-power ratio and find the optimal index
    ratio_values = thrust_values / power_values
    optimal_idx = np.argmax(ratio_values)

    # Extract optimal parameters
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

# Running the optimization
optimal_results = optimize_thruster_parameters()
print(f"Optimal Thrust with Gravity Assist: {optimal_results['Optimal Thrust']} N")
print(f"Optimal Specific Impulse: {optimal_results['Optimal Specific Impulse']} seconds")
print(f"Optimal Mass Flow Rate: {optimal_results['Optimal Mass Flow Rate']} kg/s")
print(f"Estimated Power Consumption: {optimal_results['Estimated Power Consumption']} Watts")
