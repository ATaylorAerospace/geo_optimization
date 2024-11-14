import numpy as np
import matplotlib.pyplot as plt

def calculate_thrust(specific_impulse, mass_flow_rate, g0=9.81):
    """
    Calculate the thrust given specific impulse, mass flow rate, and gravity.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :param g0: Standard gravity in m/s^2 (default is 9.81)
    :return: Thrust in Newtons
    """
    return specific_impulse * mass_flow_rate * g0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency):
    """
    Estimate the power consumption of the thruster.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :param efficiency: Efficiency of the thruster (fraction)
    :return: Power consumption in Watts
    """
    g0 = 9.81  # Standard gravity in m/s^2
    energy_per_kg = specific_impulse * g0 / efficiency
    return mass_flow_rate * energy_per_kg

def optimize_thruster_parameters(specific_impulse_range, mass_flow_rate_range, efficiency):
    """
    Optimize thruster parameters to find the maximum thrust/power_consumption ratio.
    :param specific_impulse_range: Range of specific impulse values to consider (in seconds)
    :param mass_flow_rate_range: Range of mass flow rate values to consider (in kg/s)
    :param efficiency: Efficiency of the thruster (fraction)
    :return: Optimal thrust, specific impulse, mass flow rate, and power consumption
    """
    spi_grid, mass_grid = np.meshgrid(specific_impulse_range, mass_flow_rate_range)
    thrust_values = calculate_thrust(spi_grid, mass_grid)
    power_values = estimate_power_consumption(spi_grid, mass_grid, efficiency)
    ratio_values = thrust_values / power_values
    optimal_idx = np.unravel_index(np.argmax(ratio_values), ratio_values.shape)
    optimal_thrust = thrust_values[optimal_idx]
    optimal_specific_impulse = spi_grid[optimal_idx]
    optimal_mass_flow_rate = mass_grid[optimal_idx]
    optimal_power_consumption = power_values[optimal_idx]
    return optimal_thrust, optimal_specific_impulse, optimal_mass_flow_rate, optimal_power_consumption

# Run the optimization
specific_impulse_range = np.linspace(1000, 4000, 100)
mass_flow_rate_range = np.linspace(0.0001, 0.001, 100)
efficiency = 0.5

optimal_results = optimize_thruster_parameters(specific_impulse_range, mass_flow_rate_range, efficiency)

# Displaying the results
print(f"Optimal Thrust: {optimal_results[0]:.2f} N")
print(f"Optimal Specific Impulse: {optimal_results[1]:.2f} seconds")
print(f"Optimal Mass Flow Rate: {optimal_results[2]:.5f} kg/s")
print(f"Estimated Power Consumption: {optimal_results[3]:.2f} Watts")

# Optional Plot
plt.figure(figsize=(10, 6))
plt.scatter(optimal_results[1], optimal_results[0], color='red', label='Optimal Point')
plt.xlabel('Specific Impulse (s)')
plt.ylabel('Thrust (N)')
plt.title('Thrust vs Specific Impulse')
plt.legend()
plt.grid(True)
plt.show()
