# This code calculates the maximum bending stress on the tower due to wind load and 
# compares it with the yield strength of the steel material with a safety factor. 


#this code assumes a simplified linear elastic behavior of the material 
#and neglects other potential factors such as fatigue, non-linear behavior, and dynamic effects, 
#which would require more complex analysis.
import math

# Material properties of steel
yield_strength_steel = 250 * 10**6  # Yield strength of steel in Pascals
safety_factor = 1.5  # Safety factor

# Tower dimensions
tower_height = 80  # Height of the tower in meters
tower_diameter = 4  # Diameter of the tower in meters

# Load on the tower (for example, wind load)
wind_load = 100000  # Wind load in Newtons

# Calculate the area moment of inertia of the tower cross-section
def calculate_moment_of_inertia(diameter):
    return math.pi * (diameter ** 4) / 64

moment_of_inertia = calculate_moment_of_inertia(tower_diameter)

# Calculate the maximum bending stress on the tower
def calculate_bending_stress(load, height, moment_of_inertia):
    return (load * height) / (2 * moment_of_inertia)

bending_stress = calculate_bending_stress(wind_load, tower_height, moment_of_inertia)

# Calculate the safety margin
def calculate_safety_margin(yield_strength, stress):
    return yield_strength / (safety_factor * stress)

safety_margin = calculate_safety_margin(yield_strength_steel, bending_stress)

print("Maximum bending stress on the tower:", bending_stress, "Pascals")
print("Safety margin:", safety_margin)
