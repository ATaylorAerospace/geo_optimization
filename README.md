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
To run the script, execute it in a Python environment:

The script will output the optimal thrust, specific impulse, mass flow rate, and estimated power consumption. Additionally, a plot will be generated to visualize the thrust versus specific impulse.
```bash
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
```


## Contributing
Contributions to this project are welcome. Please ensure to follow the best practices for code style and commit messages.

## License
[MIT License](LICENSE)

## Contact
For any inquiries or contributions, please contact [Your Name / Your Contact Information].
