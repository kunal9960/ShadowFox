def format_string(num, char):  # 1. Function to format
    formatted_string = format(num, char)
    return formatted_string


# 2. Calculate the area of a circular pond
radius = 84
pi = 3.14
circle_area = pi * radius ** 2

# Bonus: Calculate total water in the pond
water_ps = 1.4
total_water = int(circle_area * water_ps)

# 3. Calculate speed in meters per second
distance = 490
time = 7 * 60  # 7 minutes in seconds
speed = distance / time

# Print results
print("Formatted String:", format_string(145, 'o'))
print("Total water in the pond:", total_water)
print("Speed:", int(speed))
