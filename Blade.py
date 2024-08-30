# Effects of Wind: The Linearized Aerodynamics Model

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

#Define input parameters
wind_speed = 12  # m/s
#wind_speed = [10, 12, 15, 20]  # m/s, different wind speeds to consider
rotor_speed = 15  # RPM
blade_length = 55  # meters
material_density = 7850  # kg/m^3 (steel)
fatigue_strength = 280e6  # Pa
elastic_modulus = 210e9  # Pa
yield_strength = 250e6  # Pa
buckling_load = 550e6  # Pa


#1.This function calculate the values of forces and moments
def calculate_aerodynamic_forces_and_moments(v_wind, v_rotor, yaw_error, vertical_wind_shear, yaw_rate):
    
    rotor_radius = 20  # meters (example value)
    density_air = 1.225  # kg/m^3 (example value)
    area_rotor = np.pi * rotor_radius**2

    # Wind speed components
    v_axial = v_wind * np.cos(yaw_error)
    v_crosswind = v_wind * np.sin(yaw_error) + v_rotor

    # Vertical wind speed correction
    v_vertical = v_wind * vertical_wind_shear

    # Aerodynamic forces
    lift_coefficient = 1.2  # Example lift coefficient
    drag_coefficient = 0.1  # Example drag coefficient
    lift_force = 0.5 * density_air * area_rotor * (v_axial**2) * lift_coefficient
    drag_force = 0.5 * density_air * area_rotor * (v_crosswind**2) * drag_coefficient

    # Aerodynamic moments (for simplicity, assuming only yaw motion)
    rotor_area = np.pi * rotor_radius**2
    yaw_moment_arm = 0.75 * rotor_radius  # Example distance from rotor center to yaw axis
    yaw_moment = 0.5 * density_air * rotor_area * rotor_radius * v_wind * yaw_rate * yaw_moment_arm

    # Additional factors
    # Tip speed ratio (TSR)
    tip_speed_ratio = (v_wind + v_rotor) / (2 * np.pi * rotor_radius)
    # Angle of Attack
    aoa = np.arctan(v_crosswind / v_axial)
    # Blade pitch angle
    blade_pitch_angle = 0.1  # example value
    # Wind turbine power coefficient
    power_coefficient = 0.5  # example value
    # Torque on the rotor
    rotor_torque = 0.5 * density_air * area_rotor * (v_axial**2) * (rotor_radius**2) * power_coefficient

    return lift_force, drag_force, yaw_moment, tip_speed_ratio, aoa, blade_pitch_angle, rotor_torque


#2.Perform stress analysis
def stress_analysis(wind_speed, blade_length, elastic_modulus):
    wind_force = 0.5 * 1.23 * wind_speed**2 * np.pi * blade_length**2  # Assuming blade acts as a flat plate
    stress = wind_force / (blade_length * elastic_modulus)
    return stress

#3.Estimate fatigue life
def fatigue_life(max_stress, fatigue_strength):
    fatigue_life = 1 / (max_stress / fatigue_strength)
    return fatigue_life

#4.Conduct buckling analysis
def buckling_analysis(blade_length, elastic_modulus, buckling_load):
    critical_load = (np.pi**2 * elastic_modulus * blade_length**2) / 4
    if critical_load > buckling_load:
        return "Safe - No buckling expected"
    else:
        return "Critical buckling load exceeded"
    

# Example usage
v_wind = 10  # m/s
v_rotor = 5  # m/s (rotational speed of the rotor)
yaw_error = 0.1  # radians
vertical_wind_shear = 0.05  # example vertical wind shear factor
yaw_rate = 0.1  # rad/s

lift, drag, yaw_moment, tip_speed_ratio, aoa, blade_pitch_angle, rotor_torque = calculate_aerodynamic_forces_and_moments(v_wind,
                                                                                                                         v_rotor, 
                                                                                                                         yaw_error, 
                                                                                                                         vertical_wind_shear, 
                                                                                                                         yaw_rate)


max_stress = stress_analysis(wind_speed, blade_length, elastic_modulus)
life = fatigue_life(max_stress, fatigue_strength)
buckling_result = buckling_analysis(blade_length, elastic_modulus, buckling_load)



print("Maximum stress in the blade:", max_stress, "Pa")
print("Fatigue life of the blade:", life, "cycles")
print("Buckling analysis result:", buckling_result)
print("Lift Force:", lift)
print("Drag Force:", drag)
print("Yaw Moment:", yaw_moment)
print("Tip Speed Ratio:", tip_speed_ratio)
print("Angle of Attack:", aoa)
print("Blade Pitch Angle:", blade_pitch_angle)
print("Rotor Torque:", rotor_torque)




# # Lists to store calculated values for different wind speeds
# lift_forces = []
# drag_forces = []
# yaw_moments = []
# tip_speed_ratios = []
# angles_of_attack = []
# blade_pitch_angles = []
# rotor_torques = []

# # Calculate values for each wind speed
# for wind_speed in wind_speed:
#     lift, drag, yaw_moment, tip_speed_ratio, aoa, blade_pitch_angle, rotor_torque = calculate_aerodynamic_forces_and_moments(
#         wind_speed, v_rotor, yaw_error, vertical_wind_shear, yaw_rate)
    
#     lift_forces.append(lift)
#     drag_forces.append(drag)
#     yaw_moments.append(yaw_moment)
#     tip_speed_ratios.append(tip_speed_ratio)
#     angles_of_attack.append(aoa)
#     blade_pitch_angles.append(blade_pitch_angle)
#     rotor_torques.append(rotor_torque)

# # Plotting
# labels = ['Lift Force', 'Drag Force', 'Yaw Moment', 'Tip Speed Ratio', 'Angle of Attack', 'Blade Pitch Angle', 'Rotor Torque']
# values = [lift_forces, drag_forces, yaw_moments, tip_speed_ratios, angles_of_attack, blade_pitch_angles, rotor_torques]
# colors = ['b', 'g', 'r', 'c']  # Define colors for different wind speeds

# plt.figure(figsize=(12, 8))

# for i, wind_speed in enumerate(wind_speed):
#     plt.bar(np.arange(len(labels)) + i * 0.1, values[i], color=colors[i], width=0.1, label=f'Wind Speed: {wind_speed} m/s')

# plt.xlabel('Parameters')
# plt.ylabel('Values')
# plt.title('Aerodynamic Forces and Moments for Different Wind Speeds')
# plt.xticks(np.arange(len(labels)) + 0.3, labels, rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()