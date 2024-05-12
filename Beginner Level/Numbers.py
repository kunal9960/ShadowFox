# 1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.

def format_string(num, char):
    formatted_str = "{}{}".format(num, char)
    return formatted_str


result = format_string(145, 'o')
print(result)

# 2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

radius = 84
pi = 3.14
pond_area = pi * radius ** 2

water = 1.4
total_water = pond_area * water

print("Pond area:", pond_area, "square meters")
print("Total amount of water in the pond:", int(total_water), "liters")

# 3. If you cross a 490meter long street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. Hint: Speed = Distance / Time

distance = 490
time = 7 * 60

speed = distance / time

print(int(speed), "meters per second")
