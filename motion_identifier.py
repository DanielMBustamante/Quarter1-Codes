# Motion Type Identifier Program

# Function Definitions
# func 1: make velocity m/s
def convert_velocity(value, unit):
    """
    Convert the velocity into meters per second (m/s)
    The supported units are: m/s, ft/s, km/s, mi/s
    """
    # TODO: implement conversion using if-elif-else
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value * 0.3048
    elif unit == "km/s":
        return value * 1000
    elif unit == "mi/s":
        return value * 1609.34
    else:
        raise ValueError("Unsupported velocity unit: {}".format(v_unit))

# func 2: make acceleration m/s²
def convert_acceleration(value, unit):
    """
    Convert the acceleration into meters per second squared (m/s^2)
    Supported units: m/s^2, ft/s^2, km/s^2, mi/s^2
    """
    # TODO: implement conversion using if-elif-else
    if unit == "m/s^2":
        return value
    elif unit == "ft/s^2":
        return value * 0.3048
    elif unit == "km/s^2":
        return value * 1000
    elif unit == "mi/s^2":
        return value * 1609.34
    else:
        raise ValueError("Unsupported acceleration unit: {}".format(a_unit))
 
# func 3: determine motion type
def determine_motion_type(v, a):
    """
    Determine what the type of motion is, based on velocity and acceleration.
    Rules:
    - v > 0 and a == 0 → "Uniform Motion"
    - v > 0 and a > 0 → "Accelerated Motion"
    - v > 0 and a < 0 → "Decelerated Motion"
    - v == 0 → "At Rest"
    """
    # TODO: implement selection structure to return motion type
    if v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    elif v == 0:
        return "At Rest"
    else:
        raise ValueError("Unknown motion type for the given velocity ({}) and acceleration ({}) values.".format(v, a))

# --- Main Program ---
 
# step 1: input velocity
v_value = float(input("Enter the velocity: "))
v_unit = input("Enter the unit for the velocity (m/s, ft/s, km/s, mi/s): ") 

# step 2: input acceleration
a_value = float(input("Enter the acceleration: "))
a_unit = input("Enter the unit for the acceleration (m/s^2, ft/s^2, km/s^2, mi/s^2): ") 

# step 3: convert to SI units
v_si = convert_velocity(v_value, v_unit)      # TODO: Call the conversion function
a_si = convert_acceleration(a_value, a_unit)  # TODO: Call the conversion function
 
# step 4: determine motion type
motion = determine_motion_type(v_si, a_si)    # TODO: Call the motion type function
 
# step 5: display results
print("\n--- Results ---")
print(f"Velocity = {v_si:.3f} m/s")
print(f"Acceleration = {a_si:.3f} m/s^2")
print(f"Motion Type = {motion}")
