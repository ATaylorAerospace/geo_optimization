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
    specific_impulse_range = 2000:500:5000;
    mass_flow_rate_range = 0.00005:0.00005:0.0005;

    % Calculate thrust and power consumption for each combination
    thrust_matrix = zeros(length(specific_impulse_range), length(mass_flow_rate_range));
    power_matrix = zeros(length(specific_impulse_range), length(mass_flow_rate_range));
    
    for i = 1:length(specific_impulse_range)
        for j = 1:length(mass_flow_rate_range)
            thrust_matrix(i, j) = calculate_thrust(specific_impulse_range(i), mass_flow_rate_range(j)) * gravity_assist_multiplier;
            power_matrix(i, j) = estimate_power_consumption(specific_impulse_range(i), mass_flow_rate_range(j));
        end
    end

    % Find the maximum value in the matrices considering both thrust and power consumption
    [~, idx] = max(thrust_matrix - power_matrix);
    optimal_index = indices(idx);
    
    % Extract the optimal parameters
    results = containers.Map('KeyType', 'string', 'ValueType', 'double');
    results('Optimal Thrust') = thrust_matrix(optimal_index(1), optimal_index(2));
    results('Optimal Specific Impulse') = specific_impulse_range(optimal_index(1));
    results('Optimal Mass Flow Rate') = mass_flow_rate_range(optimal_index(2));
    results('Estimated Power Consumption') = power_matrix(optimal_index(1), optimal_index(2));
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
scatter(results('Optimal Specific Impulse'), results('Optimal Thrust'), 'r', 'MarkerFace', 'filled');
hold on

theta = linspace(0, pi/2);
for i = 1:length(specific_impulse_range)
    plot(specific_impulse_range(i), calculate_thrust(specific_impulse_range(i), mass_flow_rate_range), 'b');
end

xlabel('Specific Impulse (s)');
ylabel('Thrust (N)');
title('Thrust vs Specific Impulse');
grid on;
