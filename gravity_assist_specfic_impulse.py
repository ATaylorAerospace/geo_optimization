import numpy as np

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
    """Find optimal thruster parameters to maximize thrust and minimize power consumption.
    Parameters:
    - gravity_assist_multiplier: Multiplier to simulate gravity assist effect (dimensionless, default=1.1).
    Returns:
    - Dictionary containing optimal values for thrust, specific impulse, mass flow rate, and power consumption.
    """
    specific_impulse_range = np.linspace(2000, 5000, 10)
    mass_flow_rate_range = np.linspace(0.00005, 0.0005, 10)

    thrusts = calculate_thrust(specific_impulse_range[:, None], mass_flow_rate_range) * gravity_assist_multiplier
    power_consumptions = estimate_power_consumption(specific_impulse_range[:, None], mass_flow_rate_range)

    optimal_index = np.unravel_index(np.argmax(thrusts - power_consumptions), thrusts.shape)
    return {
        "Optimal Thrust": thrusts[optimal_index],
        "Optimal Specific Impulse": specific_impulse_range[optimal_index[0]],
        "Optimal Mass Flow Rate": mass_flow_rate_range[optimal_index[1]],
        "Estimated Power Consumption": power_consumptions[optimal_index]
    }

# Running the optimization
optimal_results = optimize_thruster_parameters()
print(f"Optimal Thrust with Gravity Assist: {optimal_results['Optimal Thrust']} N")
print(f"Optimal Specific Impulse: {optimal_results['Optimal Specific Impulse']} seconds")
print(f"Optimal Mass Flow Rate: {optimal_results['Optimal Mass Flow Rate']} kg/s")
print(f"Estimated Power Consumption: {optimal_results['Estimated Power Consumption']} Watts")
