% Function to calculate thrust
function thrust = calculate_thrust(specific_impulse, mass_flow_rate, g0)
    % Calculate the thrust given specific impulse, mass flow rate, and gravity.
    % Inputs:
    %   specific_impulse: Specific impulse of the thruster (s)
    %   mass_flow_rate: Mass flow rate of the propellant (kg/s)
    %   g0: Standard gravity in m/s^2 (default is 9.81)
    % Output:
    %   thrust: Thrust in Newtons
    if nargin < 3
        g0 = 9.81; % Standard gravity in m/s^2
    end
    thrust = specific_impulse * mass_flow_rate * g0;
end

function power = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency)
    % Estimate the power consumption of the thruster.
    % Inputs:
    %   specific_impulse: Specific impulse of the thruster (s)
    %   mass_flow_rate: Mass flow rate of the propellant (kg/s)
    %   efficiency: Efficiency of the thruster (fraction)
    % Output:
    %   power: Power consumption in Watts
    g0 = 9.81; % Standard gravity in m/s^2
    energy_per_kg = specific_impulse * g0 / efficiency;
    power = mass_flow_rate * energy_per_kg;
end

function [optimal_thrust, optimal_spi, optimal_mass, optimal_power] = optimize_thruster_parameters(efficiency)
    % Optimize thruster parameters to find the maximum thrust/power_consumption ratio
    specific_impulse_range = linspace(1000, 4000, 100); % Increased resolution
    mass_flow_rate_range = linspace(0.0001, 0.001, 100); % Increased resolution
    
    % Vectorized optimization for better performance
    [spi_grid, mass_grid] = meshgrid(specific_impulse_range, mass_flow_rate_range);
    spi_values = spi_grid(:);
    mass_values = mass_grid(:);
    
    thrust_values = calculate_thrust(spi_values, mass_values);
    power_values = estimate_power_consumption(spi_values, mass_values, efficiency);
    
    % Find the optimal parameters
    [optimal_thrust, idx] = max(thrust_values ./ power_values);
    optimal_spi = spi_values(idx);
    optimal_mass = mass_values(idx);
    optimal_power = power_values(idx);
end

% Run the optimization
efficiency = input('Enter thruster efficiency (between 0 and 1): ');
[optimal_thrust, optimal_spi, optimal_mass, optimal_power] = optimize_thruster_parameters(efficiency);

% Displaying the results
fprintf('Optimal Thrust: %.2f N\n', optimal_thrust);
fprintf('Optimal Specific Impulse: %.2f s\n', optimal_spi);
fprintf('Optimal Mass Flow Rate: %.5f kg/s\n', optimal_mass);
fprintf('Estimated Power Consumption: %.2f Watts\n', optimal_power);

% Optional Plot
figure;
scatter(optimal_spi, optimal_thrust, 'r', 'filled');
xlabel('Specific Impulse (s)');
ylabel('Thrust (N)');
title('Thrust vs Specific Impulse');
grid on;
hold on;

% Plot thrust curves for visualization
[specific_impulse_range, mass_flow_rate_range] = meshgrid(linspace(1000, 4000, 50), linspace(0.0001, 0.001, 50));
thrust_values = calculate_thrust(specific_impulse_range, mass_flow_rate_range);
contour(specific_impulse_range, mass_flow_rate_range, thrust_values, 20, 'b');
legend('Optimal Point', 'Thrust Contours');
hold off;
