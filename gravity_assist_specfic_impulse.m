% Function to calculate thrust
function thrust = calculate_thrust(specific_impulse, mass_flow_rate, g0)
   % Calculate thrust given specific impulse, mass flow rate, and gravity.
   thrust = specific_impulse * mass_flow_rate * g0;
end

function power = estimate_power_consumption(specific_impulse, mass_flow_rate, efficiency, g0)
   % Estimate power consumption based on specific impulse, mass flow rate, efficiency, and gravity.
   energy_per_kg = specific_impulse * g0 / efficiency;
   power = mass_flow_rate * energy_per_kg;
end

function results = optimize_thruster_parameters(gravity_assist_multiplier, efficiency, g0)
   % Set up parameter ranges
   specific_impulse_range = 2000:500:4000;
   mass_flow_rate_range = 0.00005:0.00005:0.0005;
   
   % Vectorized calculation of thrust and power consumption
   [spi_grid, mass_grid] = meshgrid(specific_impulse_range, mass_flow_rate_range);
   thrust_values = calculate_thrust(spi_grid, mass_grid, g0) * gravity_assist_multiplier;
   power_values = estimate_power_consumption(spi_grid, mass_grid, efficiency, g0);
   
   % Calculate thrust-to-power ratio
   ratio_values = thrust_values ./ power_values;
   [~, optimal_idx] = max(ratio_values);
   
   % Extract optimal parameters
   optimal_spi = spi_grid(optimal_idx);
   optimal_mass = mass_grid(optimal_idx);
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
efficiency = 0.9; % Assuming 90% efficiency
g0 = 9.81; % Standard gravity in m/s^2
results = optimize_thruster_parameters(gravity_multiplier, efficiency, g0);

% Displaying the results
fprintf('Optimal Thrust with Gravity Assist: %.2f N\n', results('Optimal Thrust'));
fprintf('Optimal Specific Impulse: %.2f s\n', results('Optimal Specific Impulse'));
fprintf('Optimal Mass Flow Rate: %.5f kg/s\n', results('Optimal Mass Flow Rate'));
fprintf('Estimated Power Consumption: %.2f Watts\n', results('Estimated Power Consumption'));

% Optional Plot
figure
scatter(results('Optimal Specific Impulse'), results('Optimal Thrust'), 'r', 'filled');
hold on
for spi = 2000:500:4000
   thrust_curve = cellfun(@(mass) calculate_thrust(spi, mass, g0), num2cell(0.00005:0.00005:0.0005));
   plot(0.00005:0.00005:0.0005, thrust_curve, 'b');
end
xlabel('Mass Flow Rate (kg/s)');
ylabel('Thrust (N)');
title('Thrust vs Mass Flow Rate for Different Specific Impulses');
grid on;
hold off;
