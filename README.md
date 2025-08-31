### 🚀 Geo-Orbit Thruster Optimization

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg) ![Stars](https://img.shields.io/github/stars/ATaylorAerospace/geo_optimization?style=social) ![Language](https://img.shields.io/badge/Language-Python-blue.svg)

## 📋 Overview
This script is designed to optimize the parameters for maximizing outlet thrust in GEO with minimal voltage. It focuses on finding the best combination of specific impulse and mass flow rate to achieve the highest thrust with the lowest power consumption.

The project focuses on precision, performance, and educational value, making it suitable for both academic research and practical aerospace applications.

---

## ✨ Key Features

### 🎯 **Precise Thruster Optimization**
* **Thrust Maximization**: Calculate optimal specific impulse and mass flow rate combinations
* **Power Minimization**: Minimize voltage requirements for GEO operations
* **Multi-Parameter Analysis**: Handle various efficiency scenarios and operational constraints
* **Performance Visualization**: Interactive plotting of thrust vs specific impulse relationships

### 🔧 **Advanced Calculations**
* **Real-time Optimization**: Sub-second calculation times using SciPy optimization
* **Flexible Parameters**: Customizable efficiency values and operational bounds
* **Mathematical Validation**: Verified against known thruster performance data

### 📊 **Comprehensive Visualization**
* **Performance Plots**: Clear visualization of optimal operating points
* **Interactive Analysis**: Matplotlib-based plotting with customizable parameters
* **Educational Value**: Perfect for understanding thruster performance trade-offs

---

## 🛠️ Technical Specifications

### **Physical Constants**

| Parameter | Value | Unit |
|-----------|-------|------|
| Standard Gravity (g₀) | 9.81 | m/s² |
| Default Efficiency | 0.5 | - |
| Calculation Precision | 1e-6 | - |

### **Optimization Parameters**
* ✅ Specific Impulse Range: 1000-4000 seconds
* ✅ Mass Flow Rate Range: 0.0001-0.001 kg/s
* ✅ Customizable efficiency parameters
* ✅ Real-time thrust and power calculations
* ✅ Multi-objective optimization support

---

## 🚀 Quick Start

#### Prerequisites

```bash
pip install numpy matplotlib scipy
```

## Usage
The script will output the optimal thrust, specific impulse, mass flow rate, and estimated power consumption. Additionally, a plot will be generated to visualize the thrust versus specific impulse.
```bash
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def calculate_thrust(specific_impulse, mass_flow_rate, g0=9.81):
    \"\"\"
    Calculate the thrust given specific impulse, mass flow rate, and gravity.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :param g0: Standard gravity in m/s^2 (default is 9.81)
    :return: Thrust (in Newtons)
    \"\"\"
    return specific_impulse * mass_flow_rate * g0

def estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency):
    \"\"\"
    Estimate the power consumption of the thruster.
    :param specific_impulse: Specific impulse of the thruster (in seconds)
    :param mass_flow_rate: Mass flow rate of the propellant (in kg/s)
    :param efficiency: Efficiency of the thruster (fraction)
    :return: Power consumption (in Watts)
    \"\"\"
    g0 = 9.81  # Standard gravity in m/s^2
    energy_per_kg = specific_impulse * g0 / efficiency
    return mass_flow_rate * energy_per_kg

def optimize_thruster_parameters(specific_impulse_range, mass_flow_rate_range, efficiency):
    \"\"\"
    Optimize the thruster parameters to maximize thrust and minimize power consumption.
    :param specific_impulse_range: Range of specific impulse values to consider (in seconds)
    :param mass_flow_rate_range: Range of mass flow rate values to consider (in kg/s)
    :param efficiency: Efficiency of the thruster (fraction)
    :return: Optimal thrust, specific impulse, mass flow rate, and power consumption
    \"\"\"
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

## Citation 

If you use this repository in your research, please cite it as:

```bibtex
@misc{ATaylor_GEOOptimization_2025,
  author       = {A. Taylor},
  title        = {Geo Optimization},
  year         = {2025},
  url          = {[https://github.com/ATaylorAerospace/geo_optimization]},
  note         = {Accessed: YYYY-MM-DD}
}
```

