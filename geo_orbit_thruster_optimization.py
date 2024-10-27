import numpy as np
import matplotlib.pyplot as plt

def calculate_thrust(specific_impulse, mass_flow_rate):
    """
    Calculate the thrust given specific impulse and mass flow rate.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant
    :return: Thrust in Newtons
    """
    g0 = 9.81  # Standard gravity in m/s^2
    return specific_impulse * mass_flow_rate * g0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency=0.5):
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

def optimize_thruster_parameters():
    specific_impulse_range = np.linspace(1000, 4000, 50)  # Increased resolution in seconds
    mass_flow_rate_range = np.linspace(0.0001, 0.001, 50)  # Increased resolution in kg/s

    spi_grid, mass_grid = np.meshgrid(specific_impulse_range, mass_flow_rate_range)
    spi_values = spi_grid.ravel()
    mass_values = mass_grid.ravel()

    # Vectorized calculation of thrust and power consumption
    thrust_values = calculate_thrust(spi_values, mass_values)
    power_values = estimate_power_consumption(spi_values, mass_values)

    # Calculate thrust-to-power ratio and find the optimal index
    ratio_values = thrust_values / power_values
    optimal_idx = np.argmax(ratio_values)

    # Extract optimal parameters
    optimal_thrust = thrust_values[optimal_idx]
    optimal_specific_impulse = spi_values[optimal_idx]
    optimal_mass_flow_rate = mass_values[optimal_idx]
    optimal_power_consumption = power_values[optimal_idx]

    return optimal_thrust, optimal_specific_impulse, optimal_mass_flow_rate, optimal_power_consumption

# Run the optimization
optimal_results = optimize_thruster_parameters()

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
