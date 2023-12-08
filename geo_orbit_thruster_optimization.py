
Certainly! Here's the complete Python script that you can use to optimize the parameters for maximizing outlet thrust in a geostationary orbit (GEO) with minimal voltage:

python
Copy code
import numpy as np
import matplotlib.pyplot as plt

def calculate_thrust(specific_impulse, mass_flow_rate):
    """
    Calculate the thrust given specific impulse and mass flow rate.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :return: Thrust (in Newtons)
    """
    g0 = 9.81  # Standard gravity in m/s^2
    return specific_impulse * mass_flow_rate * g0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency=0.5):
    """
    Estimate the power consumption of the thruster.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :param efficiency: Efficiency of the thruster (fraction)
    :return: Power consumption (in Watts)
    """
    g0 = 9.81  # Standard gravity in m/s^2
    energy_per_kg = specific_impulse * g0 / efficiency
    return mass_flow_rate * energy_per_kg

def optimize_thruster_parameters():
    # Define the parameter ranges
    specific_impulse_range = np.linspace(1000, 4000, 10)  # in seconds
    mass_flow_rate_range = np.linspace(0.0001, 0.001, 10)  # in kg/s

    # Initialize variables to store optimal parameters
    optimal_thrust = 0
    optimal_specific_impulse = 0
    optimal_mass_flow_rate = 0
    optimal_power_consumption = float('inf')

    # Iterate over the parameter ranges to find the optimal set
    for specific_impulse in specific_impulse_range:
        for mass_flow_rate in mass_flow_rate_range:
            thrust = calculate_thrust(specific_impulse, mass_flow_rate)
            power_consumption = estimate_power_consumption(specific_impulse, mass_flow_rate)

            if thrust > optimal_thrust and power_consumption < optimal_power_consumption:
                optimal_thrust = thrust
                optimal_specific_impulse = specific_impulse
                optimal_mass_flow_rate = mass_flow_rate
                optimal_power_consumption = power_consumption

    return (optimal_thrust, optimal_specific_impulse, optimal_mass_flow_rate, optimal_power_consumption)

# Run the optimization
optimal_results = optimize_thruster_parameters()

# Displaying the results
print(f"Optimal Thrust: {optimal_results[0]} N")
print(f"Optimal Specific Impulse: {optimal_results[1]} seconds")
print(f"Optimal Mass Flow Rate: {optimal_results[2]} kg/s")
print(f"Estimated Power Consumption: {optimal_results[3]} Watts")

# Optional Plot
plt.figure(figsize=(10, 6))
plt.scatter(optimal_results[1], optimal_results[0], color='red', label='Optimal Point')
plt.xlabel('Specific Impulse (s)')
plt.ylabel('Thrust (N)')
plt.title('Thrust vs Specific Impulse')
plt.legend()
plt.grid(True)
plt.show()