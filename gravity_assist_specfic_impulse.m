% Constants
global G0;
G0 = 9.81; % Standard gravity, m/s^2

% Function to calculate thrust
function thrust = calculate_thrust(specific_impulse, mass_flow_rate)
    % Calculate thrust given specific impulse and mass flow rate
    thrust = specific_impulse * mass_flow_rate * G0;
end

% Function to estimate power consumption
function power = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency)
    % Estimate power consumption based on specific impulse and mass flow rate
    energy_per_kg = specific_impulse * G0 / efficiency;
    power = mass_flow_rate * energy_per_kg;
end

% Function to optimize thruster parameters with gravity assist
function results = optimize_thruster_parameters(gravity_assist_multiplier)
    % Set up parameter ranges
    specific_impulse_range = 2000:500:4000;
    mass_flow_rate_range = 0.00005:0.00005:0.0005;

    % Preallocate thrust and power matrices for better performance
    [spi_grid, mass_grid] = meshgrid(specific_impulse_range, mass_flow_rate_range);
    spi_values = spi_grid(:);
    mass_values = mass_grid(:);
    
    % Vectorized calculation of thrust and power consumption
    thrust_values = arrayfun(@(spi, mass) calculate_thrust(spi, mass) * gravity_assist_multiplier, spi_values, mass_values);
    power_values = arrayfun(@(spi, mass) estimate_power_consumption(spi, mass, 0.9), spi_values, mass_values); % Assuming efficiency of 0.9

    % Calculate thrust-to-power ratio
    ratio_values = thrust_values ./ power_values;
    [~, optimal_idx] = max(ratio_values);

    % Extract optimal parameters
    optimal_spi = spi_values(optimal_idx);
    optimal_mass = mass_values(optimal_idx);
    optimal_thrust = thrust_values(optimal_idx);
    optimal_power = power_values(optimal_idx);

    % Store results in a container
    results = containers.Map('KeyType', 'string', 'ValueType', 'double');
    results('Optimal Thrust') = optimal_thrust;
    results('Optimal Specific Impulse') = optimal_spi;
    results('Optimal Mass Flow Rate') = optimal_mass;
    results('Estimated Power Consumption') = optimal_power;
end

% Running the optimization with gravity assist
gravity_multiplier = input('Enter gravity assist multiplier (usually > 1): ');
results = optimize_thruster_parameters(gravity_multiplier);

% Displaying the results
fprintf('Optimal Thrust with Gravity Assist: %.2f N\n', results('Optimal Thrust'));
fprintf('Optimal Specific Impulse: %.2f s\n', results('Optimal Specific Impulse'));
fprintf('Optimal Mass Flow Rate: %.5f kg/s\n', results('Optimal Mass Flow Rate'));
fprintf('Estimated Power Consumption: %.2f Watts\n', results('Estimated Power Consumption'));

% 2D Plot of Thrust vs. Specific Impulse
figure
scatter(results('Optimal Specific Impulse'), results('Optimal Thrust'), 'r', 'filled');
hold on

% Plotting thrust curves for visualization
for spi = specific_impulse_range
    thrust_curve = arrayfun(@(mass) calculate_thrust(spi, mass), mass_flow_rate_range);
    plot(mass_flow_rate_range, thrust_curve, 'b');
end

xlabel('Mass Flow Rate (kg/s)');
ylabel('Thrust (N)');
title('Thrust vs Mass Flow Rate for Different Specific Impulses');
grid on;
hold off;
