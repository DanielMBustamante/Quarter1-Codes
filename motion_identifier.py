# Motion Type Identifier Program

# Function Definitions
# func 1: make velocity m/s
def convert_velocity(v_value, v_unit):
    """
    Convert the velocity into meters per second (m/s)
    The supported units are: m/s, ft/s, km/s, mi/s
    """
    # TODO: implement conversion using if-elif-else
    if v_unit == "m/s":
        return v_value
    elif v_unit == "ft/s":
        return v_value * 0.3048
    elif v_unit == "km/s":
        return v_value * 1000
    elif v_unit == "mi/s":
        return v_value * 1609.34
    else:
        raise ValueError("Unsupported velocity unit: {}".format(v_unit))

# func 2: make acceleration m/s²
def convert_acceleration(a_value, a_unit):
    """
    Convert the acceleration into meters per second squared (m/s^2)
    Supported units: m/s^2, ft/s^2, km/s^2, mi/s^2
    """
    # TODO: implement conversion using if-elif-else
    if a_unit == "m/s^2":
        return a_value
    elif a_unit == "ft/s^2":
        return a_value * 0.3048
    elif a_unit == "km/s^2":
        return a_value * 1000
    elif a_unit == "mi/s^2":
        return a_value * 1609.34
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
 
# step 1: input velocity and validate immediately
try:
    v_value = float(input("Enter the velocity: "))
    v_unit = input("Enter the unit for the velocity (m/s, ft/s, km/s, mi/s): ")
    v_si = convert_velocity(v_value, v_unit)  # Validate and convert immediately
except ValueError as e:
    print("Error:", e)
    exit(1)

# step 2: input acceleration and validate immediately
try:
    a_value = float(input("Enter the acceleration: "))
    a_unit = input("Enter the unit for the acceleration (m/s^2, ft/s^2, km/s^2, mi/s^2): ")
    a_si = convert_acceleration(a_value, a_unit)  # Validate and convert immediately
except ValueError as e:
    print("Error:", e)
    exit(1)

# step 3: determine motion type
motion = determine_motion_type(v_si, a_si)

# step 4: display results
print("\n--- Results ---")
print("Velocity = {:.3f} m/s".format(v_si))
print("Acceleration = {:.3f} m/s^2".format(a_si))
print("Motion Type = {}".format(motion))
