import numpy as np

g0 = 9.81  # Pre-calculate standard gravity

def calculate_thrust(specific_impulse, mass_flow_rate):
    """Calculate thrust given specific impulse and mass flow rate."""
    return specific_impulse * mass_flow_rate * g0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency=0.7):
    """Estimate power consumption of the thruster."""
    energy_per_kg = specific_impulse * g0 / efficiency
    return mass_flow_rate * energy_per_kg

def optimize_thruster_parameters(gravity_assist_multiplier=1.1):
    """Find optimal thruster parameters efficiently."""
    specific_impulse_range = np.linspace(2000, 5000, 10)
    mass_flow_rate_range = np.linspace(0.00005, 0.0005, 10)

    # Vectorized calculations for efficiency
    thrusts = calculate_thrust(specific_impulse_range[:, None], mass_flow_rate_range) * gravity_assist_multiplier
    power_consumptions = estimate_power_consumption(specific_impulse_range[:, None], mass_flow_rate_range)

    # Find optimal indices using vectorized operations
    optimal_index = np.unravel_index(np.argmax(thrusts - power_consumptions), thrusts.shape)

    # Extract optimal values using indices
    optimal_thrust = thrusts[optimal_index]
    optimal_specific_impulse = specific_impulse_range[optimal_index[0]]
    optimal_mass_flow_rate = mass_flow_rate_range[optimal_index[1]]
    optimal_power_consumption = power_consumptions[optimal_index]

    return optimal_thrust, optimal_specific_impulse, optimal_mass_flow_rate, optimal_power_consumption

# Run the optimization and display results
optimal_results = optimize_thruster_parameters()
print(f"Optimal Thrust with Gravity Assist: {optimal_results[0]} N")
print(f"Optimal Specific Impulse: {optimal_results[1]} seconds")
print(f"Optimal Mass Flow Rate: {optimal_results[2]} kg/s")
print(f"Estimated Power Consumption: {optimal_results[3]} Watts")
