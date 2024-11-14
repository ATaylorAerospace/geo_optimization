# Geo-Orbit Thruster Optimization 

## Overview
This script is designed to optimize the parameters for maximizing outlet thrust in GEO with minimal voltage. It focuses on finding the best combination of specific impulse and mass flow rate to achieve the highest thrust with the lowest power consumption.

- Visualization of the thrust vs specific impulse relationship.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## Installation
1. Ensure that Python 3.x is installed on your system.
2. Install the required Python packages (if not already installed):
```bash
pip install numpy matplotlib
```

## Usage
The script will output the optimal thrust, specific impulse, mass flow rate, and estimated power consumption. Additionally, a plot will be generated to visualize the thrust versus specific impulse.
```bash
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def calculate_thrust(specific_impulse, mass_flow_rate, g0=9.81):
    """
    Calculate the thrust given specific impulse, mass flow rate, and gravity.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :param g0: Standard gravity in m/s^2 (default is 9.81)
    :return: Thrust (in Newtons)
    """
    return specific_impulse * mass_flow_rate * g0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency):
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

def optimize_thruster_parameters(specific_impulse_range, mass_flow_rate_range, efficiency):
    """
    Optimize the thruster parameters to maximize thrust and minimize power consumption.
    :param specific_impulse_range: Range of specific impulse values to consider (in seconds)
    :param mass_flow_rate_range: Range of mass flow rate values to consider (in kg/s)
    :param efficiency: Efficiency of the thruster (fraction)
    :return: Optimal thrust, specific impulse, mass flow rate, and power consumption
    """
    def objective_function(params):
        specific_impulse, mass_flow_rate = params
        thrust = calculate_thrust(specific_impulse, mass_flow_rate)
        power_consumption = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency)
        return -thrust + power_consumption

    initial_guess = [2000, 0.0005]  # Initial guess for specific impulse and mass flow rate
    bounds = [(1000, 4000), (0.0001, 0.001)]  # Bounds for specific impulse and mass flow rate
    res = minimize(objective_function, initial_guess, bounds=bounds)

    optimal_specific_impulse, optimal_mass_flow_rate = res.x
    optimal_thrust = calculate_thrust(optimal_specific_impulse, optimal_mass_flow_rate)
    optimal_power_consumption = estimate_power_consumption(optimal_specific_impulse, optimal_mass_flow_rate, efficiency)

    return optimal_thrust, optimal_specific_impulse, optimal_mass_flow_rate, optimal_power_consumption

# Run the optimization
specific_impulse_range = np.linspace(1000, 4000, 100)
mass_flow_rate_range = np.linspace(0.0001, 0.001, 100)
efficiency = 0.5

optimal_results = optimize_thruster_parameters(specific_impulse_range, mass_flow_rate_range, efficiency)

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
```


## Contributing
atayloraerospace

## Updates
10 Nov 2024
The calculate_thrust function has been updated to accept a custom gravity value, offering more flexibility.
The estimate_power_consumption function has been updated to use a more accurate efficiency parameter.

## License
[MIT License](LICENSE)

## Contact

